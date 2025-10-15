from .token import Token, TokenType

KEYWORDS = {
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'print': TokenType.PRINT,
    'while': TokenType.WHILE,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'and': TokenType.AND,
    'or': TokenType.OR,
    'not': TokenType.NOT,
    'break': TokenType.BREAK,
}

class Lexer:
    def __init__(self, text: str):
        # Inicializa o analisador léxico com o texto de entrada
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        self.lineno = 1

    def error(self, message: str = "Caractere inválido"):
        # Lança uma exceção para erros léxicos
        raise Exception(f'Erro léxico na linha {self.lineno}: {message} -> "{self.current_char}" ')
    
    def advance(self):
        # Avança para o próximo caractere no texto
        if self.current_char == '\n':
            self.lineno += 1
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        # Ignora espaços em branco no texto
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def peek(self):
        # Olha o próximo caractere sem avançar a posição
        peek_pos = self.pos + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        return None

    def skip_comment(self):
        # Ignora comentários em bloco no código
        self.advance() # Pula o '#'
        self.advance() # Pula o '{'
        while self.current_char is not None and not (self.current_char == '}' and self.peek() == '#'):
            self.advance()
        if self.current_char is None:
            self.error("Comentário em bloco não terminado. Faltando '}#'.")
        self.advance() # Pula o '}'
        self.advance() # Pula o '#'

    def string(self) -> str:
        # Lê e retorna uma string entre aspas
        result = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        if self.current_char is None:
            self.error("String não terminada. Faltando '\"'.")
        self.advance()
        return result

    def number(self) -> Token:
        # Lê e retorna um número inteiro ou float
        result = ''
        lineno = self.lineno
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if self.current_char == '.':
            result += '.'
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token(TokenType.FLOAT, float(result), lineno)
        else:
            return Token(TokenType.INTEGER, int(result), lineno)

    def _id(self) -> Token:
        # Lê e retorna um identificador ou palavra-chave
        result = ''
        lineno = self.lineno
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        token_type = KEYWORDS.get(result, TokenType.IDENTIFIER)
        return Token(token_type, result, lineno)

    def get_next_token(self) -> Token:
        # Retorna o próximo token do texto de entrada
        while self.current_char is not None:
            if self.current_char.isspace(): self.skip_whitespace(); continue
            if self.current_char == '#' and self.peek() == '{': self.skip_comment(); continue
            if self.current_char.isalpha() or self.current_char == '_': return self._id()
            if self.current_char.isdigit(): return self.number()
            if self.current_char == '"': return Token(TokenType.STRING, self.string(), self.lineno)

            if self.current_char == '=' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.EQ, '==', self.lineno)
            if self.current_char == '!' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.NEQ, '!=', self.lineno)
            if self.current_char == '<' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.LTE, '<=', self.lineno)
            if self.current_char == '>' and self.peek() == '=': self.advance(); self.advance(); return Token(TokenType.GTE, '>=', self.lineno)

            if self.current_char == '=': self.advance(); return Token(TokenType.ASSIGN, '=', self.lineno)
            if self.current_char == ';': self.advance(); return Token(TokenType.SEMICOLON, ';', self.lineno)
            if self.current_char == '+': self.advance(); return Token(TokenType.PLUS, "+", self.lineno)
            if self.current_char == '-': self.advance(); return Token(TokenType.MINUS, "-", self.lineno)
            if self.current_char == '*': self.advance(); return Token(TokenType.MULTIPLY, "*", self.lineno)
            if self.current_char == '/': self.advance(); return Token(TokenType.DIVIDE, "/", self.lineno)
            if self.current_char == '<': self.advance(); return Token(TokenType.LT, '<', self.lineno)
            if self.current_char == '>': self.advance(); return Token(TokenType.GT, '>', self.lineno)
            if self.current_char == '(': self.advance(); return Token(TokenType.LPAREN, "(", self.lineno)
            if self.current_char == ')': self.advance(); return Token(TokenType.RPAREN, ")", self.lineno)
            if self.current_char == '{': self.advance(); return Token(TokenType.LBRACE, '{', self.lineno)
            if self.current_char == '}': self.advance(); return Token(TokenType.RBRACE, '}', self.lineno)

            self.error()
        
        return Token(TokenType.EOF, value=None, lineno=self.lineno)