from enum import Enum

class TokenType(Enum):
    # Literais
    INTEGER = 'INTEGER'
    FLOAT   = 'FLOAT'
    STRING  = 'STRING'

    # Operadores Aritméticos
    PLUS     = 'PLUS'
    MINUS    = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE   = 'DIVIDE'

    # Operadores de Comparação
    EQ   = 'EQ'   # ==
    NEQ  = 'NEQ'  # !=
    LT   = 'LT'   # <
    GT   = 'GT'   # >
    LTE  = 'LTE'  # <=
    GTE  = 'GTE'  # >=

    # Identificadores e Atribuição
    IDENTIFIER = 'IDENTIFIER'
    ASSIGN     = 'ASSIGN'     # =

    # Delimitadores
    SEMICOLON = 'SEMICOLON' # ;
    LPAREN    = 'LPAREN'    # (
    RPAREN    = 'RPAREN'    # )
    LBRACE    = 'LBRACE'    # {
    RBRACE    = 'RBRACE'    # }

    # Palavras-chave
    IF    = 'IF'
    ELSE  = 'ELSE'
    WHILE = 'WHILE'
    PRINT = 'PRINT'
    TRUE  = 'TRUE'
    FALSE = 'FALSE'
    AND   = 'AND'
    OR    = 'OR'
    NOT   = 'NOT'
    BREAK = 'BREAK'

    # Fim de arquivo
    EOF = 'EOF'

class Token:
    def __init__(self, type: TokenType, value: any = None, lineno: int = 0):
        self.type = type
        self.value = value
        self.lineno = lineno
    
    def __str__(self):
        return f'Token \n ({self.type.name}, {repr(self.value)}, linha {self.lineno})'
    
    def __repr__(self):
        return self.__str__()