from .token import TokenType
from .ast_nodes import *
from .lexer import Lexer

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self, message: str = "Sintaxe inválida"):
        line = self.current_token.lineno
        raise Exception(f'Erro Sintático na linha {line}: {message} (token: {self.current_token})')
    
    def eat(self, token_type: TokenType):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Esperado {token_type.name}, mas encontrado {self.current_token.type.name}")

    def factor(self):
        token = self.current_token
        if token.type in (TokenType.PLUS, TokenType.MINUS):
            self.eat(token.type)
            return UnaryOpNode(op_token=token, expr_node=self.factor())
        elif token.type in (TokenType.INTEGER, TokenType.FLOAT):
            self.eat(token.type)
            return NumberNode(token)
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return StringNode(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return VarAccessNode(token)
        elif token.type == TokenType.PRINT:
            self.eat(TokenType.PRINT)
            self.eat(TokenType.LPAREN)
            expr_node = self.expr()
            self.eat(TokenType.RPAREN)
            return PrintNode(expr_node)
        self.error("Fator inválido, esperado INT, FLOAT, STRING, IDENTIFIER, PRINT, '+', '-' ou '('")

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op_token = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.factor())
        return node
    
    def arith_expr(self):
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op_token = self.current_token
            self.eat(self.current_token.type)
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.term())
        return node
        
    def expr(self):
        node = self.arith_expr()
        while self.current_token.type in (TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op_token = self.current_token
            self.eat(op_token.type)
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.arith_expr())
        return node
    
    def statement(self):
        if self.current_token.type == TokenType.WHILE:
            return self.while_statement()
        if self.current_token.type == TokenType.IF:
            return self.if_statement()
        elif self.current_token.type == TokenType.IDENTIFIER and self.lexer.peek() == '=':
            return self.assignment_statement()
        else:
            return self.expr()

    def while_statement(self):
        self.eat(TokenType.WHILE)
        self.eat(TokenType.LPAREN)
        condition = self.expr()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.LBRACE)
        body = self.compound_statement()
        self.eat(TokenType.RBRACE)
        return WhileNode(condition, body)

    def if_statement(self):
        self.eat(TokenType.IF)
        self.eat(TokenType.LPAREN)
        condition = self.expr()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.LBRACE)
        then_block = self.compound_statement()
        self.eat(TokenType.RBRACE)
        else_block = None
        if self.current_token.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            self.eat(TokenType.LBRACE)
            else_block = self.compound_statement()
            self.eat(TokenType.RBRACE)
        return IfNode(condition, then_block, else_block)

    def assignment_statement(self):
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGN)
        expr_node = self.expr()
        return VarAssignNode(var_token, expr_node)
            
    def compound_statement(self):
        nodes = []
        while self.current_token.type != TokenType.RBRACE and self.current_token.type != TokenType.EOF:
            nodes.append(self.statement())
            if self.current_token.type == TokenType.SEMICOLON:
                self.eat(TokenType.SEMICOLON)
            else:
                break
        if not nodes: return None
        if len(nodes) == 1: return nodes[0]
        root = CompoundNode()
        for node in nodes: root.children.append(node)
        return root
    
    def parse(self):
        if self.current_token.type == TokenType.EOF: return None
        nodes = []
        while self.current_token.type != TokenType.EOF:
            nodes.append(self.statement())
            self.eat(TokenType.SEMICOLON)
        if not nodes: return None
        if len(nodes) == 1: return nodes[0]
        root = CompoundNode()
        for node in nodes: root.children.append(node)
        return root