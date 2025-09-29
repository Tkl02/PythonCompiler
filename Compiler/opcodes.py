# app/opcodes.py
from enum import IntEnum, auto

class OpCode(IntEnum):
    """
    Define todos os códigos de operação (opcodes) com nomes intuitivos 
    para a nossa Máquina Virtual baseada em pilha.
    """
    
    # --- Pilha e Constantes ---
    OP_LOAD_CONST = auto()      # Argumento: index da constante. Empurra constants[index] na pilha.
    OP_POP = auto()             # Descarta o valor no topo da pilha.

    # --- Literais ---
    OP_LOAD_TRUE = auto()       # Empurra o valor booleano 'true'.
    OP_LOAD_FALSE = auto()      # Empurra o valor booleano 'false'.
    OP_LOAD_NIL = auto()        # Empurra um valor nulo/vazio.

    # --- Variáveis Globais ---
    OP_DEFINE_GLOBAL = auto()   # Argumento: index do nome da var. Define uma nova variável.
    OP_LOAD_GLOBAL = auto()     # Argumento: index do nome da var. Empurra o valor da variável.
    OP_STORE_GLOBAL = auto()    # Argumento: index do nome da var. Atribui um valor a uma var existente.

    # --- Operadores Binários (retiram dois valores da pilha, empurram um) ---
    OP_ADD = auto()
    OP_SUBTRACT = auto()
    OP_MULTIPLY = auto()
    OP_DIVIDE = auto()
    
    # --- Operadores de Comparação ---
    OP_EQUAL = auto()           # ==
    OP_NOT_EQUAL = auto()       # !=
    OP_GREATER = auto()         # >
    OP_LESS = auto()            # <

    # --- Operadores Lógicos/Unários (retiram um valor da pilha, empurram um) ---
    OP_NEGATE = auto()          # - (negação numérica)
    OP_NOT = auto()             # not (negação lógica)

    # --- Controle de Fluxo ---
    OP_JUMP_IF_FALSE = auto()   # Argumento: offset. Pula se o topo da pilha for falso.
    OP_JUMP_FORWARD = auto()    # Argumento: offset. Pula incondicionalmente para a frente.
    OP_JUMP_BACKWARD = auto()   # Argumento: offset. Pula incondicionalmente para trás (loops).

    # --- Funções e Retorno ---
    OP_CALL_PRINT = auto()      # Chama a função nativa print.
    OP_RETURN = auto()          # Finaliza a execução.