from enum import IntEnum, auto

class OpCode(IntEnum):
    # definição dos codigos de operação para a VM
    
    # PILHA CONSTANTE
    OP_LOAD_CONST = auto()
    OP_POP = auto()
    
    # LITERAIS
    OP_LOAD_TRUE = auto()
    OP_LOAD_FALSE = auto()
    OP_LOAD_NULL = auto()
    
    # VARIAVEIS GLOBAIS
    OP_DEFINE_GLOBAL = auto()
    OP_LOAD_GLOBAL = auto()
    OP_STORE_GLOBAL = auto()
    
    # OPERAÇÃO BINIARIA
    OP_ADD = auto()
    OP_SUB = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    
    # OPERAÇÃO DE COMPARAÇÃO
    
    OP_EQUAL = auto()
    OP_NOT_EQUAL = auto()
    OP_GREATER = auto()
    OP_LESS = auto()
        
    # LOGICO UNARIOS
    OP_NEGATE = auto()
    OP_NOT = auto()
    
    # FLUXOS
    OP_JUMP_IF_FALSE = auto()
    OP_JUMP_FORWARD = auto()
    OP_JUMP_BACKWARD = auto()
    
    # RETORNOS
    OP_CALL_PRINT = auto()
    OP_RETURN = auto()