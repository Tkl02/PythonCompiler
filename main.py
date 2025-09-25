from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.token import TokenType

def get_all_tokens(text):
    lexer_debug = Lexer(text)
    tokens = []
    token = lexer_debug.get_next_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer_debug.get_next_token()
    tokens.append(token)
    return tokens

def main():
    interpreter = Interpreter()

    file = 'code.txt'
    print_tokens = False
    print_tree = False

    try:
        with open(file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print(f" Arquivo '{file}' esta vazio.")
            return
        
        try:
            lexer = Lexer(text)
            parser = Parser(lexer)
            ast = parser.parse()
            result = interpreter.interpret(ast)

            if print_tokens:
                print("\n[Tokens gerados pele lexer]: \n")
                all_tokens = get_all_tokens(text)
                print(all_tokens)
                print('\n'+('__'*40)+'\n')
            
            if print_tree:
                print("\n[Fluxo da arvore sintatica abstrata]: \n")
                print(ast)
                print('\n'+('__'*40)+'\n')

            if result is not None:
                print(f" resultado: \n {result}")
        except Exception as error:
            print("erro na execução do codigo:",error)
            #raise error
        
    except FileNotFoundError:
        print(f"Error -> arquivo {file} não encontrado")

if __name__ == "__main__":
    main()