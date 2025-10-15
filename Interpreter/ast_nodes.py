class NumberNode:
    # Representa um nó de número na AST
    def __init__(self, token):
        # Inicializa o nó de número com o token correspondente
        self.token = token
        self.value = token.value
    def __repr__(self):
        # Retorna a representação em string do valor numérico
        return f'{self.value}'

class StringNode:
    # Representa um nó de string na AST
    def __init__(self, token):
        # Inicializa o nó de string com o token correspondente
        self.token = token
        self.value = token.value
    def __repr__(self):
        # Retorna a representação em string do valor da string
        return f'"{self.value}"'

class BooleanNode:
    # Representa um nó booleano na AST
    def __init__(self, token):
        # Inicializa o nó booleano com o token correspondente
        self.token = token
        self.value = True if token.type.name == 'TRUE' else False
    def __repr__(self):
        # Retorna a representação em string do valor booleano
        return "true" if self.value else "false"

class BinOpNode:
    # Representa uma operação binária na AST
    def __init__(self, left_node, op_token, right_node):
        # Inicializa o nó de operação binária com operandos e operador
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node
    def __repr__(self):
        # Retorna a representação em string da operação binária
        return f'({self.left_node} {self.op_token.type.name} {self.right_node})'

class UnaryOpNode:
    # Representa uma operação unária na AST
    def __init__(self, op_token, expr_node):
        # Inicializa o nó de operação unária com operador e expressão
        self.op_token = op_token
        self.expr_node = expr_node
    def __repr__(self):
        # Retorna a representação em string da operação unária
        return f'({self.op_token.type.name} {self.expr_node})'

class VarAssignNode:
    # Representa uma atribuição de variável na AST
    def __init__(self, var_name_token, value_node):
        # Inicializa o nó de atribuição com nome da variável e valor
        self.var_name_token = var_name_token
        self.value_node = value_node
    def __repr__(self):
        # Retorna a representação em string da atribuição
        return f'(ASSIGN {self.var_name_token.value} = {self.value_node})'

class VarAccessNode:
    # Representa o acesso a uma variável na AST
    def __init__(self, var_name_token):
        # Inicializa o nó de acesso à variável
        self.var_name_token = var_name_token
    def __repr__(self):
        # Retorna a representação em string do acesso à variável
        return f'(VAR {self.var_name_token.value})'

class CompoundNode:
    # Representa um bloco de comandos na AST
    def __init__(self):
        # Inicializa o nó composto com uma lista de filhos
        self.children = []
    def __repr__(self):
        # Retorna a representação em string do bloco de comandos
        if not self.children: return '{}'
        return '{\n  ' + ';\n  '.join(map(repr, self.children)) + '\n}'

class IfNode:
    # Representa uma estrutura condicional (if-else) na AST
    def __init__(self, condition_node, then_block, else_block=None):
        # Inicializa o nó if com condição, bloco then e opcional else
        self.condition_node = condition_node
        self.then_block = then_block
        self.else_block = else_block
    def __repr__(self):
        # Retorna a representação em string da estrutura if-else
        result = f'IF ({self.condition_node}) THEN {self.then_block}'
        if self.else_block:
            result += f' ELSE {self.else_block}'
        return result

class WhileNode:
    # Representa um laço de repetição while na AST
    def __init__(self, condition_node, body_node):
        # Inicializa o nó while com condição e corpo
        self.condition_node = condition_node
        self.body_node = body_node
    def __repr__(self):
        # Retorna a representação em string do laço while
        return f'WHILE ({self.condition_node}) DO {self.body_node}'

class PrintNode:
    # Representa um comando de impressão na AST
    def __init__(self, expr_node):
        # Inicializa o nó print com a expressão a ser impressa
        self.expr_node = expr_node
    def __repr__(self):
        # Retorna a representação em string do comando print
        return f'(PRINT {self.expr_node})'

class BreakNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self):
        return "(BREAK)"