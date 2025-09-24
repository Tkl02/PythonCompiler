from enum import Enum

class TokenType(Enum):
    """
    Enumeração para tipos de tokens da linguagem
    """

    # literais
    INTEGER = 'INTEGER'

    # operadores

    PLUS ='PLUS'
    MINUS ='MINUS'
    MULTIPLY ='MULTIPLY'
    DIVIDE ='DIVIDE'

    # Identificadores de palavras-chaves
    IDENTIFIER = 'IDENTIFIER'
    ASSIGN     = 'ASSIGN'

    # delimitadores
    SEMICOLON = 'SEMICOLON'
    LPAREN    = 'LPAREN'
    RPAREN    = 'RPAREN'
    #|--
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'


    # Palavras Chaves
    IF   = 'IF'
    ELSE = 'ELSE'
    EQ   = 'EQ'
    NEQ  = 'NEQ'
    LT   = 'LT'
    GT   = 'GT'
    LTE  = 'LTE'
    GTE  = 'GTE'

    # fim de arquivo
    EOF = 'EOF'
class Token:
    """
    Classe que representa um token.
    contem um tipo  e um valor opicional.
    """
    def __init__(self, type: TokenType, value: any = None):
        self.type = type
        self.value = value
    
    def __str__(self):
        """"
        representação do token em string
        """
        return f'\nToken -->| {self.type.name}, {repr(self.value)} |<--'
    
    def __repr__(self):
        """
        retorna os token em stringa para melhor visualização
        """
        return self.__str__()
    
