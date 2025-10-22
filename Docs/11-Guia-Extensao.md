# Guia de Extensão e Melhorias

Este documento sugere possíveis melhorias e extensões para a linguagem, com orientações para implementação.

---

## 🚀 Melhorias Propostas

### Nível 1: Facilidades Básicas

#### 1.1 Operador Módulo (`%`)

**Objetivo:** Adicionar operador para resto da divisão.

**Sintaxe proposta:**
```
resto = 10 % 3;  #{ resto = 1 }#
```

**Implementação:**

1. **Lexer** (`lexer.py`): Adicionar reconhecimento de `%`
```python
if self.current_char == '%': 
    self.advance()
    return Token(TokenType.MODULO, '%', self.lineno)
```

2. **Token** (`token.py`): Adicionar novo tipo
```python
MODULO = 'MODULO'  # %
```

3. **Parser** (`parser.py`): Adicionar em `term()`
```python
while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
    # ...
```

4. **Interpreter/Compiler**: Implementar operação

---

#### 1.2 Comentários de Linha Única

**Objetivo:** Adicionar comentários mais simples.

**Sintaxe proposta:**
```
x = 10;  ## Este é um comentário de linha
```

**Implementação:**

1. **Lexer** (`lexer.py`):
```python
def skip_line_comment(self):
    self.advance()  # Pula ##
    while self.current_char is not None and self.current_char != '\n':
        self.advance()

# Em get_next_token():
if self.current_char == '#' and self.peek() == '#':
    self.skip_line_comment()
    continue
```

---

#### 1.3 Operadores Compostos

**Objetivo:** Adicionar `+=`, `-=`, `*=`, `/=`.

**Sintaxe proposta:**
```
x += 5;   #{ Equivalente a: x = x + 5; }#
y *= 2;   #{ Equivalente a: y = y * 2; }#
```

**Implementação:**

1. **Lexer**: Reconhecer tokens compostos
2. **Parser**: Expandir para atribuição normal
3. **AST**: Transformar em `VarAssignNode` com `BinOpNode`

---

### Nível 2: Estruturas de Dados

#### 2.1 Arrays (Listas)

**Objetivo:** Suportar coleções indexadas.

**Sintaxe proposta:**
```
numeros = [1, 2, 3, 4, 5];
primeiro = numeros[0];
numeros[2] = 10;
tamanho = len(numeros);
```

**Implementação:**

1. Novo tipo de dados: `Array`
2. Novos nós AST: `ArrayLiteralNode`, `ArrayAccessNode`, `ArrayAssignNode`
3. Operações: acesso, atribuição, comprimento
4. Bytecode: `OP_BUILD_ARRAY`, `OP_LOAD_INDEX`, `OP_STORE_INDEX`

---

#### 2.2 Dicionários

**Objetivo:** Pares chave-valor.

**Sintaxe proposta:**
```
pessoa = {"nome": "João", "idade": 25};
nome = pessoa["nome"];
pessoa["cidade"] = "São Paulo";
```

**Implementação:**

1. Novo tipo: `Dictionary`
2. Novos nós AST
3. Operações de acesso e modificação

---

### Nível 3: Funções

#### 3.1 Definição de Funções

**Objetivo:** Permitir reutilização de código.

**Sintaxe proposta:**
```
func soma(a, b) {
    return a + b;
};

resultado = soma(10, 5);
print(resultado);  #{ 15 }#
```

**Implementação:**

1. **Token**: `FUNC`, `RETURN`, `LPAREN`, `RPAREN`, `COMMA`
2. **AST**: `FuncDefNode`, `FuncCallNode`, `ReturnNode`
3. **Interpreter**: Tabela de funções, pilha de chamadas
4. **Compiler**: `OP_CALL`, `OP_RETURN`, gestão de frames

**Escopo:**
- Variáveis locais vs globais
- Passagem de parâmetros
- Valor de retorno

---

#### 3.2 Funções Nativas Adicionais

**Objetivo:** Expandir biblioteca padrão.

**Funções propostas:**
```
input(mensagem)     #{ Ler entrada do usuário }#
len(array)          #{ Comprimento de array/string }#
int(valor)          #{ Converter para inteiro }#
float(valor)        #{ Converter para float }#
str(valor)          #{ Converter para string }#
abs(numero)         #{ Valor absoluto }#
min(a, b)           #{ Mínimo entre dois valores }#
max(a, b)           #{ Máximo entre dois valores }#
```

---

### Nível 4: Controle de Fluxo Avançado

#### 4.1 Laço For

**Objetivo:** Iteração mais conveniente.

**Sintaxe proposta:**
```
for (i = 0; i < 10; i = i + 1) {
    print(i);
};

#{ Ou com ranges }#
for (i in range(10)) {
    print(i);
};
```

**Implementação:**

1. **Parser**: Novo método `for_statement()`
2. **AST**: `ForNode`
3. Tradução para while internamente ou implementação dedicada

---

#### 4.2 Switch/Case

**Objetivo:** Múltiplas condições de forma elegante.

**Sintaxe proposta:**
```
switch (opcao) {
    case 1: {
        print("Opção 1");
    };
    case 2: {
        print("Opção 2");
    };
    default: {
        print("Opção inválida");
    };
};
```

---

#### 4.3 Continue

**Objetivo:** Pular para próxima iteração.

**Sintaxe proposta:**
```
i = 0;
while (i < 10) {
    i = i + 1;
    if (i % 2 == 0) {
        continue;  #{ Pula pares }#
    };
    print(i);  #{ Só imprime ímpares }#
};
```

**Implementação:**

Similar ao `break`, mas pula para início do loop.

---

### Nível 5: Programação Orientada a Objetos

#### 5.1 Classes e Objetos

**Sintaxe proposta:**
```
class Pessoa {
    func init(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    };
    
    func apresentar() {
        print("Meu nome é " + this.nome);
    };
};

p = Pessoa("João", 25);
p.apresentar();
```

**Implementação:**

Grande projeto! Requer:
- Instâncias e atributos
- Métodos
- Herança
- Encapsulamento

---

### Nível 6: Máquina Virtual

#### 6.1 Implementar VM para Executar Bytecode

**Objetivo:** Criar VM baseada em pilha.

**Componentes:**

```python
class VM:
    def __init__(self):
        self.stack = []
        self.globals = {}
        self.ip = 0  # Instruction Pointer
    
    def run(self, chunk):
        while self.ip < len(chunk.code):
            opcode, arg = chunk.code[self.ip]
            self.execute(opcode, arg)
            self.ip += 1
    
    def execute(self, opcode, arg):
        if opcode == OpCode.OP_LOAD_CONST:
            self.stack.append(chunk.constants[arg])
        elif opcode == OpCode.OP_ADD:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)
        # ... outros opcodes
```

**Benefícios:**
- Execução mais rápida
- Menor uso de memória
- Portabilidade

---

### Nível 7: Otimizações

#### 7.1 Constant Folding

**Objetivo:** Calcular constantes em tempo de compilação.

**Exemplo:**
```
x = 10 + 5 * 2;
#{ Compilador calcula: 10 + 10 = 20 }#
#{ Gera apenas: OP_LOAD_CONST 20 }#
```

---

#### 7.2 Dead Code Elimination

**Objetivo:** Remover código nunca executado.

**Exemplo:**
```
if (false) {
    print("Nunca executa");  #{ Remove este bloco }#
};
```

---

#### 7.3 Peephole Optimization

**Objetivo:** Otimizar sequências de bytecode.

**Exemplo:**
```
OP_LOAD_CONST 0
OP_POP
#{ Remove ambas - não fazem nada útil }#
```

---

### Nível 8: Ferramentas

#### 8.1 REPL (Read-Eval-Print Loop)

**Objetivo:** Terminal interativo.

```python
def repl():
    print(">>> Linguagem v1.0")
    while True:
        try:
            line = input(">>> ")
            if line == "exit": break
            
            lexer = Lexer(line)
            parser = Parser(lexer)
            ast = parser.parse()
            
            interpreter = Interpreter()
            result = interpreter.interpret(ast)
            
            if result: print(result)
        except Exception as e:
            print(f"Erro: {e}")
```

---

#### 8.2 Depurador Integrado

**Objetivo:** Step-by-step execution.

**Funcionalidades:**
- Breakpoints
- Step into/over/out
- Inspeção de variáveis
- Stack trace

---

#### 8.3 Formatter/Linter

**Objetivo:** Formatar código automaticamente.

**Funcionalidades:**
- Indentação consistente
- Espaçamento adequado
- Detecção de más práticas

---

## 🛠️ Guia de Implementação

### Passo 1: Planejamento

1. Escolha uma feature
2. Defina sintaxe claramente
3. Escreva exemplos de uso
4. Identifique componentes afetados

### Passo 2: Lexer e Parser

1. Adicione novos tokens
2. Atualize gramática
3. Crie novos nós AST
4. Escreva testes

### Passo 3: Interpretador

1. Adicione método `visit_` para novos nós
2. Implemente lógica de execução
3. Teste casos extremos

### Passo 4: Compilador

1. Adicione novos opcodes se necessário
2. Implemente `visit_` no compilador
3. Atualize disassembler
4. Teste bytecode gerado

### Passo 5: Documentação

1. Atualize documentação
2. Adicione exemplos
3. Documente comportamento
4. Crie testes automatizados

---

## 🧪 Estrutura de Testes

### Testes Unitários

```python
# test_lexer.py
def test_modulo_operator():
    lexer = Lexer("10 % 3")
    tokens = []
    while True:
        token = lexer.get_next_token()
        tokens.append(token)
        if token.type == TokenType.EOF:
            break
    
    assert tokens[0].type == TokenType.INTEGER
    assert tokens[1].type == TokenType.MODULO
    assert tokens[2].type == TokenType.INTEGER
```

### Testes de Integração

```python
# test_interpreter.py
def test_for_loop():
    code = """
    soma = 0;
    for (i = 1; i <= 5; i = i + 1) {
        soma = soma + i;
    };
    """
    
    lexer = Lexer(code)
    parser = Parser(lexer)
    ast = parser.parse()
    
    interpreter = Interpreter()
    interpreter.interpret(ast)
    
    assert interpreter.symbol_table['soma'] == 15
```

---

## 📋 Checklist de Nova Feature

- [ ] Sintaxe definida com exemplos
- [ ] Tokens adicionados (se necessário)
- [ ] Gramática atualizada
- [ ] Nós AST criados
- [ ] Parser implementado
- [ ] Interpretador implementado
- [ ] Compilador implementado (se aplicável)
- [ ] Opcodes adicionados (se necessário)
- [ ] Tratamento de erros
- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Documentação atualizada
- [ ] Exemplos práticos adicionados
- [ ] README atualizado

---

## 🎯 Roadmap Sugerido

### Fase 1: Fundamentos (1-2 semanas)
- [ ] Operador módulo
- [ ] Comentários de linha
- [ ] Operadores compostos

### Fase 2: Funções (2-3 semanas)
- [ ] Definição e chamada de funções
- [ ] Variáveis locais
- [ ] Valor de retorno
- [ ] Funções nativas adicionais

### Fase 3: Arrays (2 semanas)
- [ ] Arrays básicos
- [ ] Acesso e modificação
- [ ] Operações (len, append, etc.)

### Fase 4: VM (3-4 semanas)
- [ ] Implementar VM básica
- [ ] Suporte a todos opcodes existentes
- [ ] Otimizações de execução

### Fase 5: Laços Avançados (1 semana)
- [ ] Laço for
- [ ] Continue statement

### Fase 6: Ferramentas (2 semanas)
- [ ] REPL interativo
- [ ] Formatter básico

---

## 💡 Dicas de Desenvolvimento

### 1. Comece Pequeno
Implemente features simples primeiro para entender o fluxo.

### 2. Teste Incrementalmente
Teste cada componente isoladamente antes de integrar.

### 3. Mantenha Compatibilidade
Garanta que código existente continue funcionando.

### 4. Documente Bem
Boa documentação facilita manutenção futura.

### 5. Use Controle de Versão
Commits frequentes com mensagens descritivas.

---

## 📚 Recursos de Aprendizado

### Livros Recomendados
- **Crafting Interpreters** - Robert Nystrom
- **Writing An Interpreter In Go** - Thorsten Ball
- **Compilers: Principles, Techniques, and Tools** - Aho et al.

### Tutoriais Online
- Let's Build A Simple Interpreter
- Writing a Simple Operating System
- Make Your Own Lisp

### Projetos Similares
- Python
- Lua
- Wren
- Lox (de Crafting Interpreters)

---

**Boa sorte com as melhorias! 🚀**
