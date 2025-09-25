from enum import Enum

class TokenType(Enum):
    """Enumeração para todos os tipos de tokens da linguagem."""
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

    # Fim de arquivo
    EOF = 'EOF'

class Token:
    """
    Classe que representa um token.
    Contém um tipo, um valor opcional e o número da linha.
    """
    def __init__(self, type: TokenType, value: any = None, lineno: int = 0):
        self.type = type
        self.value = value
        self.lineno = lineno
    
    def __str__(self):
        return f'Token({self.type.name}, {repr(self.value)}, linha {self.lineno})'
    
    def __repr__(self):
        return self.__str__()