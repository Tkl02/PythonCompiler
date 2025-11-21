from enum import IntEnum, auto

class OpCode(IntEnum):
    
    # --- Pilha e Constantes ---
    OP_LOAD_CONST = auto()      
    OP_POP = auto()             

    # --- Literais ---
    OP_LOAD_TRUE = auto()      
    OP_LOAD_FALSE = auto()      
    OP_LOAD_NIL = auto()       

    # --- Variáveis Globais ---
    OP_DEFINE_GLOBAL = auto()
    OP_LOAD_GLOBAL = auto()     
    OP_STORE_GLOBAL = auto()    

    # --- Operadores Binários (retiram dois valores da pilha, empurram um) ---
    OP_ADD = auto()
    OP_SUBTRACT = auto()
    OP_MULTIPLY = auto()
    OP_DIVIDE = auto()
    
    # --- Operadores de Comparação ---
    OP_EQUAL = auto()           
    OP_NOT_EQUAL = auto()       
    OP_GREATER = auto()         
    OP_LESS = auto()            
    OP_GREATER_EQUAL = auto()   
    OP_LESS_EQUAL = auto()     

    # --- Operadores Lógicos/Unários (retiram um valor da pilha, empurram um) ---
    OP_NEGATE = auto()        
    OP_NOT = auto()            
    OP_AND = auto()           
    OP_OR = auto()            

    # --- Controle de Fluxo ---
    OP_JUMP_IF_FALSE = auto()  
    OP_JUMP_FORWARD = auto()  
    OP_JUMP_BACKWARD = auto()  

    # --- Funções e Retorno ---
    OP_CALL_PRINT = auto()     
    OP_RETURN = auto()          