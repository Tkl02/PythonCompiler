from .token import TokenType
from .ast_nodes import *
from .types import Integer, Float, String

class Interpreter:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        if node is None: return None
        method_name = f'visit_{type(node).__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)
    
    def generic_visit(self, node):
        raise Exception(f'Nenhum método visit_{type(node).__name__} definido')

    def visit_NumberNode(self, node: NumberNode):
        if node.token.type == TokenType.INTEGER:
            return Integer(int(node.value))
        elif node.token.type == TokenType.FLOAT:
            return Float(float(node.value))

    def visit_StringNode(self, node: StringNode):
        return String(node.value)

    def visit_BinOpNode(self, node: BinOpNode):
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)
        op_type = node.op_token.type
        error_msg = None

        if op_type == TokenType.PLUS:
            result, error_msg = left.__add__(right)
        elif op_type == TokenType.MINUS:
            result, error_msg = left.__sub__(right)
        # Adicione aqui a lógica para MULTIPLY e DIVIDE dentro das classes de tipo
        # e chame-as aqui, como __mul__ e __div__.
        
        # Operadores de Comparação
        elif op_type in (TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            if not isinstance(left, (Integer, Float)) or not isinstance(right, (Integer, Float)):
                error_msg = "TypeError: Operadores de comparação só podem ser usados com números."
            else:
                if op_type == TokenType.EQ:  result = Integer(1) if left.value == right.value else Integer(0)
                if op_type == TokenType.NEQ: result = Integer(1) if left.value != right.value else Integer(0)
                if op_type == TokenType.LT:  result = Integer(1) if left.value <  right.value else Integer(0)
                if op_type == TokenType.GT:  result = Integer(1) if left.value >  right.value else Integer(0)
                if op_type == TokenType.LTE: result = Integer(1) if left.value <= right.value else Integer(0)
                if op_type == TokenType.GTE: result = Integer(1) if left.value >= right.value else Integer(0)

        if error_msg:
            raise Exception(f"Erro na linha {node.op_token.lineno}: {error_msg}")
        return result

    def visit_UnaryOpNode(self, node: UnaryOpNode):
        number = self.visit(node.expr_node)
        if node.op_token.type == TokenType.MINUS:
            if isinstance(number, (Integer, Float)):
                number.value = -number.value
                return number
        elif node.op_token.type == TokenType.PLUS:
            if isinstance(number, (Integer, Float)):
                return number
        raise Exception(f"Erro na linha {node.op_token.lineno}: Operador unário inválido para o tipo {type(number).__name__}")
    
    def visit_VarAssignNode(self, node: VarAssignNode):
        var_name = node.var_name_token.value
        value = self.visit(node.value_node)
        self.symbol_table[var_name] = value
        return value
    
    def visit_VarAccessNode(self, node: VarAccessNode):
        var_name = node.var_name_token.value
        value = self.symbol_table.get(var_name)
        if value is None:
            raise NameError(f"Erro na linha {node.var_name_token.lineno}: Variável '{var_name}' não definida.")
        return value
        
    def visit_CompoundNode(self, node: CompoundNode):
        last_result = None
        for child in node.children:
            last_result = self.visit(child)
        return last_result

    def visit_IfNode(self, node: IfNode):
        condition = self.visit(node.condition_node)
        is_true = condition and condition.value != 0 and condition.value != ""
        if is_true:
            return self.visit(node.then_block)
        elif node.else_block is not None:
            return self.visit(node.else_block)
        return None
        
    def visit_WhileNode(self, node: WhileNode):
        while True:
            condition = self.visit(node.condition_node)
            is_true = condition and condition.value != 0 and condition.value != ""
            if is_true:
                self.visit(node.body_node)
            else:
                break
        return None
    
    def visit_PrintNode(self, node: PrintNode):
        value_to_print = self.visit(node.expr_node)
        print(value_to_print.value)
        return None
    
    def interpret(self, tree):
        return self.visit(tree)