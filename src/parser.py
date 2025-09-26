from .token import TokenType
from .ast_nodes import *
from .lexer import Lexer

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.had_error = False

        # --- MUDANÇA ESTRUTURAL: AGORA TEMOS DOIS TOKENS DE LOOKAHEAD ---
        self.current_token = self.lexer.get_next_token()
        self.next_token = self.lexer.get_next_token() # <-- NOVO

    def error(self, message: str = "Sintaxe inválida"):
        line = self.current_token.lineno
        print(f'[ERRO SINTÁTICO] Linha {line}: {message} (token: {self.current_token})')
        self.had_error = True
        raise SyntaxError 

    def advance(self):
        """Avança os tokens: o próximo se torna o atual."""
        self.current_token = self.next_token
        self.next_token = self.lexer.get_next_token()

    def eat(self, token_type: TokenType):
        if self.current_token.type == token_type:
            self.advance() # <-- A LÓGICA DE AVANÇO AGORA ESTÁ CENTRALIZADA
        else:
            self.error(f"Esperado '{token_type.name}', mas encontrado '{self.current_token.type.name}'")

    def synchronize(self):
        # A lógica de sincronização não precisa de 'previous_token' agora
        self.advance()
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type in [TokenType.IF, TokenType.WHILE, TokenType.PRINT, TokenType.SEMICOLON]:
                return
            self.advance()

    # --- Hierarquia de Expressão (factor, term, etc. não mudam) ---
    def factor(self):
        token = self.current_token
        if token.type == TokenType.NOT: self.advance(); return UnaryOpNode(op_token=token, expr_node=self.factor())
        if token.type in (TokenType.PLUS, TokenType.MINUS): self.advance(); return UnaryOpNode(op_token=token, expr_node=self.factor())
        elif token.type in (TokenType.INTEGER, TokenType.FLOAT): self.advance(); return NumberNode(token)
        elif token.type == TokenType.STRING: self.advance(); return StringNode(token)
        elif token.type in (TokenType.TRUE, TokenType.FALSE): self.advance(); return BooleanNode(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.IDENTIFIER: self.advance(); return VarAccessNode(token)
        elif token.type == TokenType.PRINT:
            self.eat(TokenType.PRINT)
            self.eat(TokenType.LPAREN)
            expr_node = self.expr()
            self.eat(TokenType.RPAREN)
            return PrintNode(expr_node)
        self.error("Fator inválido, esperado literal, identificador, print, 'not', '+', '-' ou '('")

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.factor())
        return node
    
    def arith_expr(self):
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.term())
        return node
        
    def comp_expr(self):
        node = self.arith_expr()
        while self.current_token.type in (TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.arith_expr())
        return node

    def and_expr(self):
        node = self.comp_expr()
        while self.current_token.type == TokenType.AND:
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.comp_expr())
        return node

    def expr(self):
        node = self.and_expr()
        while self.current_token.type == TokenType.OR:
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.and_expr())
        return node
    
    # --- Fim da Hierarquia de Expressão ---

    def statement(self):
        """CORRIGIDO: Agora usa o lookahead de token, que é muito mais robusto."""
        if self.current_token.type == TokenType.IDENTIFIER and self.next_token.type == TokenType.ASSIGN:
            return self.assignment_statement()
        elif self.current_token.type == TokenType.WHILE: return self.while_statement()
        elif self.current_token.type == TokenType.IF: return self.if_statement()
        else: return self.expr()

    def assignment_statement(self):
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGN)
        return VarAssignNode(var_token, self.expr())

    def while_statement(self):
        self.eat(TokenType.WHILE); self.eat(TokenType.LPAREN)
        condition = self.expr()
        self.eat(TokenType.RPAREN); self.eat(TokenType.LBRACE)
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
            
            if self.current_token.type == TokenType.IF:
                else_block = self.if_statement()
            else:
                self.eat(TokenType.LBRACE)
                else_block = self.compound_statement()
                self.eat(TokenType.RBRACE)
        
        return IfNode(condition, then_block, else_block)
            
    def compound_statement(self):
        nodes = []
        while self.current_token.type != TokenType.RBRACE and self.current_token.type != TokenType.EOF:
            nodes.append(self.statement())
            if self.current_token.type == TokenType.SEMICOLON: self.eat(TokenType.SEMICOLON)
            else: break
        if not nodes: return None
        if len(nodes) == 1: return nodes[0]
        root = CompoundNode()
        for node in nodes: root.children.append(node)
        return root
    
    def parse(self):
        if self.current_token.type == TokenType.EOF: return None
        nodes = []
        while self.current_token.type != TokenType.EOF:
            try:
                nodes.append(self.statement())
                self.eat(TokenType.SEMICOLON)
            except SyntaxError:
                self.synchronize()
        if self.had_error: return None
        if not nodes: return None
        if len(nodes) == 1: return nodes[0]
        root = CompoundNode()
        for node in nodes: root.children.append(node)
        return root