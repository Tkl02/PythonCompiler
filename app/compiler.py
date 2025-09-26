from app.opcodes import OpCode
from app.bytecode import Chunk
from src.token import TokenType
import src.ast_nodes as ast

class Compiler:
    # metodos de inicialização
    def __init__(self):
        self.chunk = Chunk()
        
    def compile(self, node):
        if node is None:
            return None

        self.visit(node)
        self.emit_return()

        return self.chunk

    # metodos visit
    def visit(self, node):
        method_name =f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    # metodos emição de byte code
    
    def emit_byte(self, opcode: OpCode, line: int):
        self.chunk.write(opcode,0, line-line)
        
    def emit_constant(self, value:any, line: int):
        const_index = self.chunk.add_constant(value)
        self.chunk.write(OpCode.OP_LOAD_CONST, const_index,line=line)
    
    def emit_return(self,):
        self.chunk.write(OpCode.OP_RETURN,0,line=-1)
        
    # Metodo visita literais
    
    def visit_NumberNode(self, node: ast.NumberNode):
        self.emit_constant(node.value, node.token.lineno)
    
    def visit_StringNode(self, node: ast.StringNode):
        self.emit_constant(node.value, node.token.lineno)
        
    def visit_BooleanNode(self, node: ast.BooleanNode):
        if node.value:
            self.emit_byte(OpCode.OP_LOAD_TRUE, node.token.lineno)
        else:
            self.emit_byte(OpCode.OP_LOAD_FALSE, node.token.lineno)
    
    def visit_CompoundNode(self, node: ast.CompoundNode):
        for child in node.children:
            self.visit(child)
            
            is_expression_statement = isinstance(child, (ast.BinOpNode, ast.UnaryOpNode,ast.NumberNode,ast.StringNode,ast.BooleanNode, ast.VarAccessNode))
            
            if is_expression_statement:
                line = -1
                if hasattr(child, 'token'):
                    line=child.token.lineno
                elif hasattr(child, 'op_token'):
                    line= child.op_token.lineno
                self.emit_byte(OpCode.OP_POP, line)
            
    def visit_UnaryOpNode(self, node: ast.UnaryOpNode):
        self.visit(node.expr_node)
        
        op_type = node.op_token.type
        line = node.op_token.lineno
        
        if op_type == TokenType.MINUS:
            self.emit_byte(OpCode.OP_NEGATE, line)
        elif op_type == TokenType.NOT:
            self.emit_byte(OpCode.OP_NOT, line)
    
    def visit_BinOpNode(self, node:ast.BinOpNode):
        self.visit(node.left_node)
        self.visit(node.right_node)
        
        op_type =node.op_token.type
        line = node.op_token.lineno
        
        if op_type == TokenType.PLUS: self.emit_byte(OpCode.OP_ADD, line)
        if op_type == TokenType.MINUS: self.emit_byte(OpCode.OP_SUB, line)
        if op_type == TokenType.MULTIPLY: self.emit_byte(OpCode.OP_MUL, line)
        if op_type == TokenType.DIVIDE: self.emit_byte(OpCode.OP_DIV, line)
        if op_type == TokenType.EQ: self.emit_byte(OpCode.OP_EQUAL, line)
        if op_type == TokenType.NEQ: self.emit_byte(OpCode.OP_NOT_EQUAL, line)
        if op_type == TokenType.GT: self.emit_byte(OpCode.OP_GREATER, line)
        if op_type == TokenType.LT: self.emit_byte(OpCode.OP_LESS, line)