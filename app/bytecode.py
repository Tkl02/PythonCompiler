from dataclasses import dataclass, field
from typing import List, Union, Tuple
from .opcodes import OpCode

Bytecode = Tuple[OpCode, int]

@dataclass
class Chunk:
    code: List[Bytecode] = field(default_factory=list)
    constants: List[any] = field(default_factory=list)
    lines: List[int] = field(default_factory=list)
    
    def write(self, opcode: OpCode, arguments: int=0, line: int = -1 ):
        self.code.append((opcode,arguments))
        self.lines.append(line)
    
    def add_constant (self, value: any) -> int:
        self.constants.append(value)
        return len(self.constants) -1