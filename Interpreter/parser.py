from .token import TokenType
from .ast_nodes import *
from .lexer import Lexer

class Parser:
    
    # Inicializa o parser com o lexer e prepara o lookahead de tokens
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.had_error = False

        # --- MUDANÇA ESTRUTURAL: AGORA TEMOS DOIS TOKENS DE LOOKAHEAD ---
        self.current_token = self.lexer.get_next_token()
        self.next_token = self.lexer.get_next_token() # <-- NOVO

    def parse(self):
        """
        Inicia o processo de parsing, construindo a árvore sintática abstrata (AST) a partir dos tokens.
        Retorna a raiz da AST (CompoundNode) ou None se não houver comandos.
        """
        if self.current_token.type == TokenType.EOF:
            return None
        nodes = []
        while self.current_token.type != TokenType.EOF:
            try:
                nodes.append(self.statement())
                self.eat(TokenType.SEMICOLON)
            except SyntaxError:
                self.synchronize()
        if self.had_error:
            return None
        if not nodes:
            return None
        root = CompoundNode()
        for node in nodes:
            root.children.append(node)
        return root
    
    # Metodos de analise de declaração
    
    def statement(self):
        """
        Analisa e retorna um comando (statement) do código-fonte, como atribuição, if, while ou expressão.
        """
        if self.current_token.type ==TokenType.BREAK:
            return self.break_statement()
        if self.current_token.type == TokenType.IDENTIFIER and self.next_token.type == TokenType.ASSIGN:
            return self.assignment_statement()
        elif self.current_token.type == TokenType.WHILE: return self.while_statement()
        elif self.current_token.type == TokenType.IF: return self.if_statement()
        else: return self.expr()
    
    def if_statement(self):
        """
        Analisa uma estrutura condicional if-else, incluindo blocos aninhados e else opcional.
        """
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
    
    def assignment_statement(self):
        """
        Analisa uma atribuição de variável (ex: x = 5).
        """
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGN)
        return VarAssignNode(var_token, self.expr())

    def while_statement(self):
        """
        Analisa um laço de repetição while, incluindo condição e corpo do laço.
        """
        self.eat(TokenType.WHILE); self.eat(TokenType.LPAREN)
        condition = self.expr()
        self.eat(TokenType.RPAREN); self.eat(TokenType.LBRACE)
        body = self.compound_statement()
        self.eat(TokenType.RBRACE)
        return WhileNode(condition, body)

    def break_statement(self):
        token = self.current_token
        self.eat(TokenType.BREAK)
        return BreakNode(token)
            
    def compound_statement(self):
        """
        Analisa um bloco de comandos (delimitado por chaves), retornando um CompoundNode.
        """
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
    
    # Metodos de analise de expressão
    
    def expr(self):
        """
        Analisa uma expressão lógica com operadores 'or'.
        """
        node = self.and_expr()
        while self.current_token.type == TokenType.OR:
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.and_expr())
        return node
    
    def and_expr(self):
        """
        Analisa uma expressão lógica com operadores 'and'.
        """
        node = self.comp_expr()
        while self.current_token.type == TokenType.AND:
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.comp_expr())
        return node
    
    def comp_expr(self):
        """
        Analisa expressões de comparação (==, !=, <, >, <=, >=).
        """
        node = self.arith_expr()
        while self.current_token.type in (TokenType.EQ, TokenType.NEQ, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.arith_expr())
        return node

    def arith_expr(self):
        """
        Analisa expressões aritméticas com soma e subtração.
        """
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.term())
        return node
    
    def term(self):
        """
        Analisa termos aritméticos com multiplicação e divisão.
        """
        node = self.factor()
        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op_token = self.current_token; self.advance()
            node = BinOpNode(left_node=node, op_token=op_token, right_node=self.factor())
        return node

    def factor(self):
        """
        Analisa fatores: literais, identificadores, expressões entre parênteses, operadores unários e comando print.
        """
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
    
    # Metodos auxiliares
    
    def error(self, message: str = "Sintaxe inválida"):
        """
        Exibe mensagem de erro sintático, marca erro e lança exceção SyntaxError.
        """
        line = self.current_token.lineno
        print(f'[ERRO SINTÁTICO] Linha {line}: {message} (token: {self.current_token})')
        self.had_error = True
        raise SyntaxError 

    def advance(self):
        """
        Avança os tokens: o próximo se torna o atual, e busca um novo lookahead.
        """
        self.current_token = self.next_token
        self.next_token = self.lexer.get_next_token()

    def eat(self, token_type: TokenType):
        """
        Consome o token atual se for do tipo esperado, senão lança erro sintático.
        """
        if self.current_token.type == token_type:
            self.advance() # <-- A LÓGICA DE AVANÇO AGORA ESTÁ CENTRALIZADA
        else:
            self.error(f"Esperado '{token_type.name}', mas encontrado '{self.current_token.type.name}'")

    def synchronize(self):
        """
        Recupera o parser após um erro, avançando até um ponto seguro (início de comando ou fim de arquivo).
        """
        self.advance()
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type in [TokenType.IF, TokenType.WHILE, TokenType.PRINT, TokenType.SEMICOLON]:
                return
            self.advance()
