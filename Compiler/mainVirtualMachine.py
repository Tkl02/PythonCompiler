from .opcodes import OpCode
from .bytecode import Chunk
from Interpreter.types import *

class VirtualMachine:
    def __init__(self):
        self.stack: list[Value] = []
        self.globals = {}
        self.ip = 0
        self.chunk: Chunk = None

    def run(self, chunk: Chunk):
        self.chunk = chunk
        self.ip = 0
        self.stack = []
        self.globals = {}
    
        while self.ip < len(self.chunk.code):
            opcode, arg = self.chunk.code[self.ip]
            self.ip +=1

            if opcode == OpCode.OP_LOAD_CONST:
                constant = self.chunk.constants[arg]

                if isinstance(constant, bool): self.stack.append(Boolean(constant))
                elif isinstance(constant, int): self.stack.append(Integer(constant))
                elif isinstance(constant, float): self.stack.append(Float(constant))
                elif isinstance(constant, str): self.stack.append(String(constant))
            
            elif opcode == OpCode.OP_POP:
                if self.stack: self.stack.pop()
            
            elif opcode == OpCode.OP_LOAD_TRUE: self.stack.append(Boolean(True))
            elif opcode == OpCode.OP_LOAD_FALSE: self.stack.append(Boolean(False))
            elif opcode == OpCode.OP_LOAD_NIL: self.stack.append(None)

            elif opcode == OpCode.OP_DEFINE_GLOBAL or opcode == OpCode.OP_STORE_GLOBAL:
                var_name = self.chunk.constants[arg]
                val = self.stack.pop()
                self.globals[var_name] = val

            elif opcode == OpCode.OP_LOAD_GLOBAL:
                var_name = self.chunk.constants[arg]
                val = self.globals.get(var_name)

                if val is None:
                    self.runtime_error(f"Variavel '{var_name}' não definida")
                    return

                self.stack.append(val)
            
            elif opcode in [OpCode.OP_ADD, OpCode.OP_SUBTRACT, OpCode.OP_MULTIPLY, OpCode.OP_DIVIDE]:
                right = self.stack.pop()
                left = self.stack.pop()
                result, error = None, None

                if opcode == OpCode.OP_ADD: result, error = left.__add__(right)
                elif opcode == OpCode.OP_SUBTRACT: result, error = left.__sub__(right)
                elif opcode == OpCode.OP_MULTIPLY: result, error = left.__mul__(right)
                elif opcode == OpCode.OP_DIVIDE: result, error = left.__truediv__(right)

                if error:
                    self.runtime_error(error)
                    return
                self.stack.append(result)

            elif opcode == OpCode.OP_NEGATE:
                val = self.stack.pop()
                if isinstance(val, (Integer, Float)):
                    val.value = -val.value
                    self.stack.append(val)
                else:
                    self.runtime_error(f"Operador '-' inválido para {type(val).__name__}")
                    return
            
            elif opcode == OpCode.OP_NOT:
                val = self.stack.pop()

                is_true = val.value if hasattr(val, 'value') else False
                self.stack.append(Boolean(not is_true))

            elif opcode in [OpCode.OP_EQUAL, OpCode.OP_NOT_EQUAL, OpCode.OP_GREATER, OpCode.OP_LESS, OpCode.OP_GREATER_EQUAL, OpCode.OP_LESS_EQUAL]:
                right = self.stack.pop()
                left = self.stack.pop()

                if opcode not in [OpCode.OP_EQUAL, OpCode.OP_NOT_EQUAL]:
                    if not isinstance(left, (Integer, Float)) or not isinstance(right, (Integer, Float)):
                        self.runtime_error("Comparação de ordem só permitida entre números")
                        return
                
                res = False
                if opcode == OpCode.OP_EQUAL: res = left.value == right.value
                elif opcode == OpCode.OP_NOT_EQUAL: res = left.value != right.value
                elif opcode == OpCode.OP_GREATER: res = left.value > right.value
                elif opcode == OpCode.OP_LESS: res = left.value < right.value
                elif opcode == OpCode.OP_GREATER_EQUAL: res = left.value >= right.value
                elif opcode == OpCode.OP_LESS_EQUAL: res = left.value <= right.value

                self.stack.append(Boolean(res))

            elif opcode == OpCode.OP_AND:
                right = self.stack.pop()
                left = self.stack.pop()
                left_true = left.value if hasattr(left, 'value') else False
                right_true = right.value if hasattr(right, 'value') else False
                self.stack.append(Boolean(left_true and right_true))

            elif opcode == OpCode.OP_OR:
                right = self.stack.pop()
                left = self.stack.pop()
                left_true = left.value if hasattr(left, 'value') else False
                right_true = right.value if hasattr(right, 'value') else False
                self.stack.append(Boolean(left_true or right_true))

            elif opcode == OpCode.OP_JUMP_FORWARD:
                self.ip += arg
            
            elif opcode == OpCode.OP_JUMP_BACKWARD:
                self.ip -= arg

            elif opcode == OpCode.OP_JUMP_IF_FALSE:
                val = self.stack.pop()
                is_true = val.value if hasattr(val, 'value') else False
                if not is_true:
                    self.ip += arg
            
            elif opcode == OpCode.OP_CALL_PRINT:
                val = self.stack.pop()
                print(repr(val))

            elif opcode == OpCode.OP_RETURN:
                return
    
    def runtime_error(self, message: str):
        line = -1
        if self.chunk and self.ip < len(self.chunk.lines):
            line = self.chunk.lines[self.ip - 1]

        print(f"[Erro de Execução na VM] Linha -> {line}: {message} ")