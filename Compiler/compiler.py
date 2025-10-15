from Compiler.opcodes import OpCode
from Compiler.bytecode import Chunk
import Interpreter.ast_nodes as ast
from Interpreter.token import TokenType

class Compiler:
    def __init__(self):
        self.chunk = Chunk()
        self.loop_contexts: list[list[int]] = [] 

    def compile(self, node):
        if node is None: return None
        self.visit(node)
        self.emit_return()
        return self.chunk

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def emit_byte(self, opcode: OpCode, line: int):
        self.chunk.write(opcode, 0, line=line)

    def emit_constant(self, value: any, line: int):
        const_index = self.chunk.add_constant(value)
        self.chunk.write(OpCode.OP_LOAD_CONST, const_index, line=line)
        
    def emit_return(self):
        self.chunk.write(OpCode.OP_RETURN, 0, line=-1)

    def emit_jump(self, opcode: OpCode, line: int) -> int:
        self.chunk.write(opcode, 0xFFFF, line)
        return len(self.chunk.code) - 1

    def patch_jump(self, offset: int):
        jump = len(self.chunk.code) - offset - 1
        opcode, _ = self.chunk.code[offset]
        self.chunk.code[offset] = (opcode, jump)

    def visit_CompoundNode(self, node: ast.CompoundNode):
        for child in node.children:
            self.visit(child)
            is_expression_statement = isinstance(child, (ast.BinOpNode, ast.UnaryOpNode, ast.NumberNode, ast.StringNode, ast.BooleanNode, ast.VarAccessNode))
            if is_expression_statement:
                line = -1
                if hasattr(child, 'token'): line = child.token.lineno
                elif hasattr(child, 'op_token'): line = child.op_token.lineno
                self.emit_byte(OpCode.OP_POP, line)

    def visit_NumberNode(self, node: ast.NumberNode): self.emit_constant(node.value, node.token.lineno)
    def visit_StringNode(self, node: ast.StringNode): self.emit_constant(node.value, node.token.lineno)
    def visit_BooleanNode(self, node: ast.BooleanNode):
        if node.value: self.emit_byte(OpCode.OP_LOAD_TRUE, node.token.lineno)
        else: self.emit_byte(OpCode.OP_LOAD_FALSE, node.token.lineno)

    def visit_UnaryOpNode(self, node: ast.UnaryOpNode):
        self.visit(node.expr_node)
        op_type, line = node.op_token.type, node.op_token.lineno
        if op_type == TokenType.MINUS: self.emit_byte(OpCode.OP_NEGATE, line)
        elif op_type == TokenType.NOT: self.emit_byte(OpCode.OP_NOT, line)

    def visit_BinOpNode(self, node: ast.BinOpNode):
        self.visit(node.left_node); self.visit(node.right_node)
        op_type, line = node.op_token.type, node.op_token.lineno
        if op_type == TokenType.PLUS:     self.emit_byte(OpCode.OP_ADD, line)
        elif op_type == TokenType.MINUS:    self.emit_byte(OpCode.OP_SUBTRACT, line)
        elif op_type == TokenType.MULTIPLY: self.emit_byte(OpCode.OP_MULTIPLY, line)
        elif op_type == TokenType.DIVIDE:   self.emit_byte(OpCode.OP_DIVIDE, line)
        elif op_type == TokenType.EQ:    self.emit_byte(OpCode.OP_EQUAL, line)
        elif op_type == TokenType.NEQ:      self.emit_byte(OpCode.OP_NOT_EQUAL, line)
        elif op_type == TokenType.GT:       self.emit_byte(OpCode.OP_GREATER, line)
        elif op_type == TokenType.LT:       self.emit_byte(OpCode.OP_LESS, line)
        elif op_type == TokenType.GTE:       self.emit_byte(OpCode.OP_GREATER_EQUAL, line)
        elif op_type == TokenType.LTE:       self.emit_byte(OpCode.OP_LESS_EQUAL, line)

    def visit_VarAssignNode(self, node: ast.VarAssignNode):
        self.visit(node.value_node)
        var_name = node.var_name_token.value
        const_index = self.chunk.add_constant(var_name)
        self.chunk.write(OpCode.OP_STORE_GLOBAL, const_index, node.var_name_token.lineno)

    def visit_VarAccessNode(self, node: ast.VarAccessNode):
        var_name = node.var_name_token.value
        const_index = self.chunk.add_constant(var_name)
        self.chunk.write(OpCode.OP_LOAD_GLOBAL, const_index, node.var_name_token.lineno)

    def visit_PrintNode(self, node: ast.PrintNode):
        self.visit(node.expr_node)
        line = -1 
        if hasattr(node.expr_node, 'token'): line = node.expr_node.token.lineno
        elif hasattr(node.expr_node, 'op_token'): line = node.expr_node.op_token.lineno
        self.emit_byte(OpCode.OP_CALL_PRINT, line)

    def visit_IfNode(self, node: ast.IfNode):
        self.visit(node.condition_node)
        line = node.condition_node.op_token.lineno if hasattr(node.condition_node, 'op_token') else -1
        then_jump = self.emit_jump(OpCode.OP_JUMP_IF_FALSE, line)
        self.visit(node.then_block)
        else_jump = self.emit_jump(OpCode.OP_JUMP_FORWARD, line)
        self.patch_jump(then_jump)
        if node.else_block is not None: self.visit(node.else_block)
        self.patch_jump(else_jump)

    def visit_WhileNode(self, node: ast.WhileNode):
        
        self.loop_contexts.append([])

        loop_start = len(self.chunk.code)
        self.visit(node.condition_node)
        line = node.condition_node.op_token.lineno if hasattr(node.condition_node, 'op_token') else -1
        exit_jump = self.emit_jump(OpCode.OP_JUMP_IF_FALSE, line)
        self.visit(node.body_node)
        jump_offset = len(self.chunk.code) - loop_start + 1
        self.chunk.write(OpCode.OP_JUMP_BACKWARD, jump_offset, line)
        self.patch_jump(exit_jump)

        break_to_patch = self.loop_contexts.pop()
        for break_jump in break_to_patch:
            self.patch_jump(break_jump)
    
    def visit_BreakNode(self, node: ast.BreakNode):
        if not self.loop_contexts:
            raise Exception(f"Erro na linha {node.token.lineno}: 'Break' so pode ser usado dentro de um laço")

        jump = self.emit_jump(OpCode.OP_JUMP_FORWARD, node.token.lineno)
        self.loop_contexts[-1].append(jump)