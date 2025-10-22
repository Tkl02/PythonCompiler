from .token import TokenType
from .ast_nodes import *
from .types import Integer, Float, String, Boolean

class BreakException(Exception):
    pass

class Interpreter:
    # Metodo De Contrução
    def __init__(self):
        # Inicializa a tabela de símbolos para armazenar variáveis
        self.symbol_table = {}
    
    def interpret(self, tree):
        # Inicia a interpretação da árvore sintática
        return self.visit(tree)
    
    # Métodos de Visit

    def visit(self, node):
        # Despacha a visita para o método específico de cada tipo de nó
        if node is None: return None
        method_name = f'visit_{type(node).__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)
    
    def generic_visit(self, node):
        # Lança exceção quando não há método de visita definido para o nó
        raise Exception(f'Nenhum método visit_{type(node).__name__} definido')

    # visits e declarações
    
    def visit_CompoundNode(self, node: CompoundNode):
        # Executa uma sequência de comandos e retorna o resultado do último
        last_result = None
        for child in node.children:
            last_result = self.visit(child)
        return last_result

    def visit_IfNode(self, node: IfNode):
        # Avalia a condição e executa o bloco then ou else conforme o resultado
        condition = self.visit(node.condition_node)
        is_true = condition and hasattr(condition, 'value') and condition.value
        if is_true:
            return self.visit(node.then_block)
        elif node.else_block is not None:
            return self.visit(node.else_block)
        return None

    def visit_WhileNode(self, node: WhileNode):
        # Executa o corpo do loop enquanto a condição for verdadeira
        while True:
            condition = self.visit(node.condition_node)
            is_true = condition and hasattr(condition, 'value') and condition.value
            if is_true:
                try:
                    self.visit(node.body_node)
                except BreakException:
                    break
            else:
                break
        return None

    def visit_PrintNode(self, node: PrintNode):
        # Avalia a expressão e imprime seu valor na saída padrão
        value_to_print = self.visit(node.expr_node)
        print(repr(value_to_print))
        return None
    
    def visit_BreakNode(self, node: BreakNode):
        # Lança exceção para interromper a execução de um loop
        raise BreakException()

    # visits e expressões literais
    
    def visit_BinOpNode(self, node: BinOpNode):
        # Executa operações binárias entre dois operandos
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)
        op_type = node.op_token.type
        result, error_msg = None, None

        if op_type == TokenType.PLUS: result, error_msg = left.__add__(right)
        elif op_type == TokenType.MINUS: result, error_msg = left.__sub__(right)
        elif op_type == TokenType.MULTIPLY: result, error_msg = left.__mul__(right)
        elif op_type == TokenType.DIVIDE: result, error_msg = left.__truediv__(right)
        elif op_type == TokenType.AND:
            if not isinstance(left, Boolean) or not isinstance(right, Boolean): error_msg = "TypeError: Operador 'and' só pode ser usado com booleanos."
            else: result = Boolean(left.value and right.value)
        elif op_type == TokenType.OR:
            if not isinstance(left, Boolean) or not isinstance(right, Boolean): error_msg = "TypeError: Operador 'or' só pode ser usado com booleanos."
            else: result = Boolean(left.value or right.value)
        elif op_type in (TokenType.EQ, TokenType.NEQ):
            result = Boolean(left.value == right.value if op_type == TokenType.EQ else left.value != right.value)
        elif op_type in (TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            if type(left) != type(right) or not isinstance(left, (Integer, Float, String)):
                error_msg = f"TypeError: Não é possível comparar {type(left).__name__} com {type(right).__name__}"
            else:
                if op_type == TokenType.LT:  result = Boolean(left.value <  right.value)
                elif op_type == TokenType.GT:  result = Boolean(left.value >  right.value)
                elif op_type == TokenType.LTE: result = Boolean(left.value <= right.value)
                elif op_type == TokenType.GTE: result = Boolean(left.value >= right.value)

        if error_msg: raise Exception(f"Erro na linha {node.op_token.lineno}: {error_msg}")
        return result
    
    def visit_UnaryOpNode(self, node: UnaryOpNode):
        # Executa operações unárias sobre um único operando
        operand = self.visit(node.expr_node)
        op_type = node.op_token.type
        if op_type == TokenType.MINUS:
            if isinstance(operand, (Integer, Float)): operand.value = -operand.value; return operand
        elif op_type == TokenType.PLUS:
            if isinstance(operand, (Integer, Float)): return operand
        elif op_type == TokenType.NOT:
            is_true = operand and operand.value; return Boolean(not is_true)
        raise Exception(f"Erro na linha {node.op_token.lineno}: Operador unário '{op_type.name}' inválido para o tipo {type(operand).__name__}")
    
    def visit_NumberNode(self, node: NumberNode):
        # Converte um nó numérico em Integer ou Float conforme o tipo
        if node.token.type == TokenType.INTEGER: return Integer(int(node.value))
        elif node.token.type == TokenType.FLOAT: return Float(float(node.value))
    
    def visit_StringNode(self, node: StringNode):
        # Cria um objeto String a partir do valor do nó
        return String(node.value)

    def visit_BooleanNode(self, node: BooleanNode):
        # Cria um objeto Boolean a partir do valor do nó
        return Boolean(node.value)

    def visit_VarAssignNode(self, node: VarAssignNode):
        # Atribui um valor a uma variável na tabela de símbolos
        var_name = node.var_name_token.value
        value = self.visit(node.value_node)
        self.symbol_table[var_name] = value
        return value
    
    def visit_VarAccessNode(self, node: VarAccessNode):
        # Recupera o valor de uma variável da tabela de símbolos
        var_name = node.var_name_token.value
        value = self.symbol_table.get(var_name)
        if value is None:
            raise NameError(f"Erro na linha {node.var_name_token.lineno}: Variável '{var_name}' não definida.")
        return value