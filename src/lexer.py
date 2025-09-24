from .token import Token, TokenType

KEYWORDS = {
    'if': Token(TokenType.IF, 'if'),
    'else': Token(TokenType.ELSE, 'else'),
}

class Lexer():
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self, message: str = "Caracter invalido"):
        """Gera uma exceção em casos de erro lexico"""
        raise Exception(f'Erro lexico: {message} -> "{self.current_char}" ')
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self) -> int:
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def _id(self) -> Token:
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        return KEYWORDS.get(result, Token(TokenType.IDENTIFIER, result))

    def get_next_token(self) -> Token:
                
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_':return self._id()

            if self.current_char.isdigit():return Token(TokenType.INTEGER, self.integer())

            if self.current_char == '=': self.advance(); return Token(TokenType.ASSIGN, '=')
            
            if self.current_char == ';': self.advance(); return Token(TokenType.SEMICOLON, ';')

            # Pular espaços
            if self.current_char.isspace(): self.skip_whitespace(); continue

            # Reconhece numeros inteiros
            if self.current_char.isdigit(): return Token(TokenType.INTEGER, self.integer())
            
            #reconhece operadores
            if self.current_char == '+': self.advance(); return Token(TokenType.PLUS, "+")
            
            if self.current_char == '-': self.advance(); return Token(TokenType.MINUS, "-")
            
            if self.current_char == '*': self.advance(); return Token(TokenType.MULTIPLY, "*")
            
            if self.current_char == '/': self.advance(); return Token(TokenType.DIVIDE, "/")
            
            # reconhece parenteses
            
            if self.current_char == '(': self.advance(); return Token(TokenType.LPAREN, "(")
            
            if self.current_char == ')': self.advance(); return Token(TokenType.RPAREN, ")")

            # reconhece comparacoes
            
            if self.current_char == '=' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.EQ, '==')
            if self.current_char == '!' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.NEQ, '!=')
            if self.current_char == '<' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.LTE, '<=')
            if self.current_char == '>' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.GTE, '>=')
            
            if self.current_char == '<': self.advance(); return Token(TokenType.LT, '<')
            if self.current_char == '>': self.advance(); return Token(TokenType.GT, '>')

            if self.current_char == '{': self.advance(); return Token(TokenType.LBRACE, '{')
            if self.current_char == '}': self.advance(); return Token(TokenType.RBRACE, '}')

            self.error()
        
        return Token(TokenType.EOF)
    
    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        return None