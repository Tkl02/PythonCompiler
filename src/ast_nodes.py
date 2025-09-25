class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value
    def __repr__(self):
        return f'{self.value}'

class StringNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value
    def __repr__(self):
        return f'"{self.value}"'

class BooleanNode:
    def __init__(self, token):
        self.token = token
        self.value = True if token.type.name == 'TRUE' else False
    def __repr__(self):
        return "true" if self.value else "false"

class BinOpNode:
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node
    def __repr__(self):
        return f'({self.left_node} {self.op_token.type.name} {self.right_node})'

class UnaryOpNode:
    def __init__(self, op_token, expr_node):
        self.op_token = op_token
        self.expr_node = expr_node
    def __repr__(self):
        return f'({self.op_token.type.name} {self.expr_node})'

class VarAssignNode:
    def __init__(self, var_name_token, value_node):
        self.var_name_token = var_name_token
        self.value_node = value_node
    def __repr__(self):
        return f'(ASSIGN {self.var_name_token.value} = {self.value_node})'

class VarAccessNode:
    def __init__(self, var_name_token):
        self.var_name_token = var_name_token
    def __repr__(self):
        return f'(VAR {self.var_name_token.value})'

class CompoundNode:
    def __init__(self):
        self.children = []
    def __repr__(self):
        if not self.children: return '{}'
        return '{\n  ' + ';\n  '.join(map(repr, self.children)) + '\n}'

class IfNode:
    def __init__(self, condition_node, then_block, else_block=None):
        self.condition_node = condition_node
        self.then_block = then_block
        self.else_block = else_block
    def __repr__(self):
        result = f'IF ({self.condition_node}) THEN {self.then_block}'
        if self.else_block:
            result += f' ELSE {self.else_block}'
        return result

class WhileNode:
    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node
    def __repr__(self):
        return f'WHILE ({self.condition_node}) DO {self.body_node}'

class PrintNode:
    def __init__(self, expr_node):
        self.expr_node = expr_node
    def __repr__(self):
        return f'(PRINT {self.expr_node})'