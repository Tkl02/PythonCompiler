from .token import TokenType
from .ast_nodes import *
from .lexer import Lexer

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self, message: str = "Sintaxe inválida"):
        raise Exception(f'Erro Sintático: {message} (token: {self.current_token})')
    
    def eat(self, token_type: TokenType):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Esperado {token_type.name}, mas encontrado {self.current_token.type.name}")

    
    def factor(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return NumberNode(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return VarAccessNode(token)
        self.error("Fator inválido, esperado INTEGER, IDENTIFIER ou '('")

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            operation_token = self.current_token
            self.eat(self.current_token.type)
            node = BinaryOperationNode(left_node=node, operation_token=operation_token, right_node=self.factor())
        return node
    
    def expr(self):
        if self.current_token.type == TokenType.IDENTIFIER and self.lexer.text[self.lexer.pos:].lstrip().startswith('='):
             return self.assignment_statement()
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            operation_token = self.current_token
            self.eat(self.current_token.type)
            node = BinaryOperationNode(left_node=node, operation_token=operation_token, right_node=self.term())
        return node  
    
    def assignment_statement(self):
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGN)
        expr_node = self.expr()
        return VarAssignNode(var_token, expr_node)
    
    def statement(self):
        if self.current_token.type == TokenType.IDENTIFIER and self.lexer.text[self.lexer.pos:].lstrip().startswith('='):
            return self.assignment_statement()
        else:
            return self.expr()
        
    def compound_statement(self):
        nodes = [self.statement()]
        
        while self.current_token.type == TokenType.SEMICOLON:
            self.eat(TokenType.SEMICOLON)
            nodes.append(self.statement())
        
        if len(nodes) == 1:
            return nodes[0]
            
        root = CompoundNode()
        for node in nodes:
            root.children.append(node)
        return root
    
    
    def parse(self):
        return self.compound_statement()