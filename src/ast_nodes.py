class NumberNode():
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f'{self.value}'
    
class BinaryOperationNode():
    def __init__(self, left_node, operation_token, right_node):
        self.left_node = left_node
        self.operation_token = operation_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node} {self.operation_token.type.name} {self.right_node})'
    
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
        return f'COMPOUND {{\n' + ';\n'.join(map(repr, self.children)) + '\n}'
        