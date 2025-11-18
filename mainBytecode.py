from Interpreter.lexer import Lexer
from Interpreter.parser import Parser
from Compiler.compiler import Compiler
from Compiler.disasembler import disassemble_chunk
from Compiler.mainVirtualMachine import VirtualMachine
import sys

debug_execution = True

def main():
    # Pega o arquivo passado via terminal ou usa 'code.txt' como padrão
    if len(sys.argv) > 1: 
        filename = sys.argv[1]
    else: 
        filename = 'code.txt'
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip(): return

        print(f"--- Executando {filename} ---\n")

        # 1. FASE FRONT-END (Lexer & Parser)
        lexer = Lexer(text)
        parser = Parser(lexer)
        ast = parser.parse()

        # Se a AST foi gerada com sucesso (sem erros de sintaxe)
        if ast and not parser.had_error:
            
            # 2. FASE BACK-END (Compilador)
            compiler = Compiler()
            bytecode_chunk = compiler.compile(ast)
            
            if bytecode_chunk:
                # Opcional: Mostra o bytecode legível
                if debug_execution:
                    disassemble_chunk(bytecode_chunk, "Bytecode Gerado")
                
                # 3. FASE DE EXECUÇÃO (Máquina Virtual)
                print("--- Saída do Programa ---")
                vm = VirtualMachine()
                vm.run(bytecode_chunk)
                print("\n-------------------------")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro crítico: {e}")
        # raise # Descomente essa linha se quiser ver o traceback completo do Python

if __name__ == "__main__":
    main()