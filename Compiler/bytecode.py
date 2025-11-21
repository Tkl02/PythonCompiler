from dataclasses import dataclass, field
from typing import List, Tuple
from .opcodes import OpCode

# Um Bytecode é uma tupla de (OpCode, argumento), onde o argumento é um inteiro.
ByteCode = Tuple[OpCode, int]

@dataclass
class Chunk:
    code: List[ByteCode] = field(default_factory=list) 
    constants: List[any] = field(default_factory=list)
    lines: List[int] = field(default_factory=list)

    def write(self, opcode: OpCode, argument: int, line: int):
        """Adiciona uma instrução ao chunk."""
        self.code.append((opcode, argument))
        self.lines.append(line)

    def add_constant(self, value: any) -> int:
        """Adiciona uma constante à piscina e retorna seu índice."""
        try:
            return self.constants.index(value)
        except ValueError:
            self.constants.append(value)
            return len(self.constants) - 1