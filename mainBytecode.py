# mainBytecode.py
from src.lexer import Lexer
from src.parser import Parser
from app.compiler import Compiler
from app.disasembler import disassemble_chunk
import sys

def main():
    if len(sys.argv) > 1: filename = sys.argv[1]
    else: filename = 'code.txt'
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip(): return

        # FASE 1: Front-end
        lexer = Lexer(text)
        parser = Parser(lexer)
        ast = parser.parse()

        if ast:
            # FASE 2: Back-end (Compilação)
            compiler = Compiler()
            bytecode_chunk = compiler.compile(ast)
            
            # Depuração: Exibe o bytecode gerado
            if bytecode_chunk:
                disassemble_chunk(bytecode_chunk, "Bytecode Principal")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    except Exception as e:
        # Erros do compilador serão pegos aqui
        print(f"Ocorreu um erro: {e}")
        raise

if __name__ == "__main__":
    main()