from .token import Token, TokenType

class Lexer():
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self, message: str = "Caracter invalido"):
        """Gera uma exceção em casos de erro lexico"""
        raise Exception(f'Error lexico: {message} -> {self.current_char} ')
    
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
        
        return Token(TokenType.IDENTIFIER, result)

    def get_next_token(self) -> Token:
                
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return self._id()

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=')
            
            if self.current_char == ';':
                self.advance()
                return Token(TokenType.SEMICOLON, ';')

            # Pular espaços
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Reconhece numeros inteiros
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())
            
            #reconhece operadores
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, "+")
            
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, "-")
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, "*")
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, "/")
            
            # reconhece parenteses
            
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, "(")
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ")")
            
            self.error()
        
        return Token(TokenType.EOF)    