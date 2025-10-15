# app/disassembler.py
from .bytecode import Chunk
from .opcodes import OpCode

def disassemble_chunk(chunk: Chunk, name: str):
    """Exibe o conteúdo de um Chunk de forma legível."""
    print(f"--- {name} ---")
    offset = 0
    while offset < len(chunk.code):
        offset = disassemble_instruction(chunk, offset)
    print("-" * (len(name) + 8))

def simple_instruction(name: str, offset: int) -> int:
    """Formata uma instrução simples sem argumentos."""
    print(f"{name}")
    return offset + 1

def constant_instruction(name: str, chunk: Chunk, arg: int) -> int:
    """Formata uma instrução que referencia uma constante."""
    constant_value = chunk.constants[arg]
    print(f"{name:<16} {arg:4d} '{constant_value}'")
    return 1 # Retorna o tamanho da instrução (1 byte para opcode + 1 para arg, mas o loop cuida do offset)

def jump_instruction(name: str, sign: int, arg: int, offset: int) -> int:
    """Formata uma instrução de pulo."""
    jump = arg * sign
    target = offset + 1 + jump
    print(f"{name:<16} {offset:4d} -> {target}")
    return 2 # Retorna o tamanho da instrução

def disassemble_instruction(chunk: Chunk, offset: int) -> int:
    """Desmonta e exibe uma única instrução de bytecode."""
    print(f"{offset:04d} ", end='')
    line = chunk.lines[offset]
    if offset > 0 and line == chunk.lines[offset - 1]:
        print("   | ", end='')
    else:
        print(f"{line:4d} ", end='')

    opcode, arg = chunk.code[offset]

    # Mapeamento de opcodes para suas funções de formatação
    if opcode in [
        OpCode.OP_RETURN, OpCode.OP_POP, OpCode.OP_LOAD_TRUE, OpCode.OP_LOAD_FALSE,
        OpCode.OP_LOAD_NIL, OpCode.OP_ADD, OpCode.OP_SUBTRACT, OpCode.OP_MULTIPLY,
        OpCode.OP_DIVIDE, OpCode.OP_EQUAL, OpCode.OP_NOT_EQUAL, OpCode.OP_GREATER,
        OpCode.OP_LESS, OpCode.OP_NEGATE, OpCode.OP_NOT, OpCode.OP_CALL_PRINT,
        OpCode.OP_GREATER_EQUAL ,OpCode.OP_LESS_EQUAL
    ]:
        simple_instruction(opcode.name, offset)
        return offset + 1

    elif opcode in [
        OpCode.OP_LOAD_CONST, OpCode.OP_DEFINE_GLOBAL, OpCode.OP_LOAD_GLOBAL, OpCode.OP_STORE_GLOBAL
    ]:
        constant_instruction(opcode.name, chunk, arg)
        return offset + 1
    
    elif opcode in [
        OpCode.OP_JUMP_IF_FALSE, OpCode.OP_JUMP_FORWARD
    ]:
        jump_instruction(opcode.name, 1, arg, offset)
        return offset + 1
        
    elif opcode == OpCode.OP_JUMP_BACKWARD:
        jump_instruction(opcode.name, -1, arg, offset)
        return offset + 1
    
    else:
        print(f"Opcode desconhecido {opcode.name}")
        return offset + 1