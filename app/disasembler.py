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

def constant_instruction(name: str, chunk: Chunk, offset: int, opcode: OpCode, arg: int) -> int:
    constant_value = chunk.constants[arg]
    print(f"{name:<16} {arg:4d} '{constant_value}'")
    return offset + 1

def simple_instruction(name: str, offset: int) -> int:
    print(f"{name}")
    return offset + 1

def disassemble_instruction(chunk: Chunk, offset: int) -> int:
    print(f"{offset:04d} ", end='')
    line = chunk.lines[offset]
    if offset > 0 and line == chunk.lines[offset - 1]:
        print("   | ", end='')
    else:
        print(f"{line:4d} ", end='')

    opcode, arg = chunk.code[offset]

    if opcode == OpCode.OP_RETURN: return simple_instruction("OP_RETURN", offset)
    if opcode == OpCode.OP_LOAD_CONST: return constant_instruction("OP_LOAD_CONST", chunk, offset, opcode, arg)
    if opcode == OpCode.OP_LOAD_TRUE: return simple_instruction("OP_LOAD_TRUE", offset)
    if opcode == OpCode.OP_LOAD_FALSE: return simple_instruction("OP_LOAD_FALSE", offset)
    if opcode == OpCode.OP_POP: return simple_instruction("OP_POP", offset)
    
    if opcode == OpCode.OP_ADD: return simple_instruction("OP_ADD", offset)
    if opcode == OpCode.OP_SUB: return simple_instruction("OP_SUBTRACT", offset)
    if opcode == OpCode.OP_MUL: return simple_instruction("OP_MULTIPLY", offset)
    if opcode == OpCode.OP_DIV: return simple_instruction("OP_DIVIDE", offset)
    if opcode == OpCode.OP_EQUAL: return simple_instruction("OP_EQUAL", offset)
    if opcode == OpCode.OP_NOT_EQUAL: return simple_instruction("OP_NOT_EQUAL", offset)
    if opcode == OpCode.OP_GREATER: return simple_instruction("OP_GREATER", offset)
    if opcode == OpCode.OP_LESS: return simple_instruction("OP_LESS", offset)
    if opcode == OpCode.OP_NEGATE: return simple_instruction("OP_NEGATE", offset)
    if opcode == OpCode.OP_NOT: return simple_instruction("OP_NOT", offset)
    
    print(f"Opcode desconhecido {opcode.name}")
    return offset + 1