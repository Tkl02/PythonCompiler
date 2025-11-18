from Interpreter.lexer import Lexer
from Interpreter.parser import Parser
from Interpreter.interpreter import Interpreter
from Interpreter.token import TokenType
from ast_visualizer import ASTVisualizer

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
    print_tree = True

    try:
        with open(file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print(f" Arquivo '{file.name}' esta vazio.")
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
            
            if ast and print_tree:
                visualizerTree = ASTVisualizer()
                visualizerTree.generate_html(ast, "ast_tree_visualizer.html")


            
        except Exception as error:
            print("erro na execução do codigo:",error)
            #raise error
        
    except FileNotFoundError:
        print(f"Error -> arquivo {file} não encontrado")

if __name__ == "__main__":
    main()