from .token import TokenType
from .ast_nodes import *

class Interpreter():
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)
    
    def generic_visit(self, node):
        raise Exception(f'Nenhum método visit_{type(node).__name__} definido')

    def visit_NumberNode(self, node: NumberNode):
        return float(node.value)
    
    def visit_BinaryOperationNode(self, node: BinaryOperationNode):
        
        left_val = self.visit(node.left_node)
        right_val = self.visit(node.right_node)

        operation = node.operation_token.type

        if operation == TokenType.PLUS:
            return left_val + right_val
        elif operation == TokenType.MINUS:
            return left_val - right_val
        elif operation == TokenType.MULTIPLY:
            return left_val * right_val
        elif operation == TokenType.DIVIDE:
            # Tratamento de erro para divisão por zero
            if right_val == 0:
                raise ZeroDivisionError("Erro em tempo de execução: Divisão por zero.")
            return left_val / right_val
        
        if operation == TokenType.EQ:  return 1.0 if left_val == right_val else 0.0
        if operation == TokenType.NEQ: return 1.0 if left_val != right_val else 0.0
        if operation == TokenType.LT:  return 1.0 if left_val < right_val else 0.0
        if operation == TokenType.GT:  return 1.0 if left_val > right_val else 0.0
        if operation == TokenType.LTE: return 1.0 if left_val <= right_val else 0.0
        if operation == TokenType.GTE: return 1.0 if left_val >= right_val else 0.0
    
    def visit_VarAssignNode(self, node: VarAssignNode):
        var_name = node.var_name_token.value
        value = self.visit(node.value_node)
        self.symbol_table[var_name] = value
        return value
    
    def visit_VarAccessNode(self, node: VarAccessNode):
        var_name = node.var_name_token.value
        value = self.symbol_table.get(var_name)
        if value is None:
            raise NameError(f"Variável '{var_name}' não definida.")
        return value
        
    def visit_CompoundNode(self, node: CompoundNode):
        last_result = None
        for child in node.children:
            last_result = self.visit(child)
        return last_result

    def visit_IfNode(self, node: IfNode):
        condition_value = self.visit(node.condition_node)
        
        if condition_value != 0:
            return self.visit(node.then_block)
        elif node.else_block is not None:
            return self.visit(node.else_block)
        
    def visit_UnaryOpNode(self, node: UnaryOpNode):
        number = self.visit(node.expr_node)

        if node.op_token.type == TokenType.MINUS:
            return -number
        elif node.op_token.type == TokenType.PLUS:
            return +number
    
    def interpret(self, tree):
        if tree is None: 
            return 0
        return self.visit(tree)