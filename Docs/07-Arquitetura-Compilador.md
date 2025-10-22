# Arquitetura do Compilador

Este documento explica em detalhes a arquitetura técnica do compilador e interpretador da linguagem.

## Visão Geral

O projeto implementa duas abordagens para executar código:

1. **Interpretador**: Executa código diretamente percorrendo a AST
2. **Compilador**: Transforma código em bytecode para uma máquina virtual

```
┌─────────────┐
│ Código Fonte│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    LEXER    │ ← Análise Léxica
└──────┬──────┘
       │ (Tokens)
       ▼
┌─────────────┐
│   PARSER    │ ← Análise Sintática
└──────┬──────┘
       │ (AST)
       ▼
    ┌──┴───┐
    │      │
    ▼      ▼
┌────────┐ ┌────────┐
│INTERPR.│ │COMPILER│
└───┬────┘ └───┬────┘
    │          │
    ▼          ▼
 Execução   Bytecode
```

---

## 1. Front-End: Análise Léxica (Lexer)

**Arquivo:** `Interpreter/lexer.py`

O **Lexer** é responsável por transformar o texto fonte em uma sequência de tokens.

### Funcionamento

```python
class Lexer:
    def __init__(self, text: str):
        self.text = text          # Código fonte
        self.pos = 0              # Posição atual
        self.current_char = ...   # Caractere atual
        self.lineno = 1           # Linha atual
```

### Processo de Tokenização

1. **Ignora espaços em branco**: `skip_whitespace()`
2. **Identifica comentários**: `skip_comment()` para `#{ }#`
3. **Reconhece números**: `number()` retorna INTEGER ou FLOAT
4. **Reconhece strings**: `string()` entre aspas duplas
5. **Reconhece identificadores**: `_id()` e palavras-chave
6. **Reconhece operadores**: Caracteres especiais (`+`, `-`, `==`, etc.)

### Exemplo de Tokenização

**Entrada:**
```
x = 10 + 5;
```

**Saída (tokens):**
```
Token(IDENTIFIER, 'x', linha 1)
Token(ASSIGN, '=', linha 1)
Token(INTEGER, 10, linha 1)
Token(PLUS, '+', linha 1)
Token(INTEGER, 5, linha 1)
Token(SEMICOLON, ';', linha 1)
Token(EOF, None, linha 1)
```

### Palavras Reservadas

```python
KEYWORDS = {
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'print': TokenType.PRINT,
    'while': TokenType.WHILE,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'and': TokenType.AND,
    'or': TokenType.OR,
    'not': TokenType.NOT,
    'break': TokenType.BREAK,
}
```

### Operadores de Dois Caracteres

O lexer usa `peek()` para reconhecer operadores compostos:

```python
if self.current_char == '=' and self.peek() == '=':
    return Token(TokenType.EQ, '==', self.lineno)
```

Operadores compostos: `==`, `!=`, `<=`, `>=`

---

## 2. Front-End: Análise Sintática (Parser)

**Arquivo:** `Interpreter/parser.py`

O **Parser** constrói uma **Árvore Sintática Abstrata (AST)** a partir dos tokens.

### Gramática da Linguagem

A linguagem segue uma gramática hierárquica:

```
programa        → declaração* EOF
declaração      → if_stmt | while_stmt | assign_stmt | expr_stmt
if_stmt         → "if" "(" expr ")" "{" compound "}" ("else" (if_stmt | "{" compound "}"))?
while_stmt      → "while" "(" expr ")" "{" compound "}"
assign_stmt     → IDENTIFIER "=" expr
expr_stmt       → expr ";"

expr            → or_expr
or_expr         → and_expr ("or" and_expr)*
and_expr        → comp_expr ("and" comp_expr)*
comp_expr       → arith_expr (("==" | "!=" | "<" | ">" | "<=" | ">=") arith_expr)*
arith_expr      → term (("+" | "-") term)*
term            → factor (("*" | "/") factor)*
factor          → NUMBER | STRING | BOOLEAN | IDENTIFIER
                | "(" expr ")"
                | ("+" | "-" | "not") factor
                | "print" "(" expr ")"
```

### Precedência de Operadores

Da menor para a maior precedência (implementada de cima para baixo):

1. `expr()` - OR lógico
2. `and_expr()` - AND lógico
3. `comp_expr()` - Comparação
4. `arith_expr()` - Adição/Subtração
5. `term()` - Multiplicação/Divisão
6. `factor()` - Unários, literais, parênteses

### Lookahead de Dois Tokens

Para distinguir entre atribuição e expressão:

```python
def __init__(self, lexer: Lexer):
    self.current_token = self.lexer.get_next_token()
    self.next_token = self.lexer.get_next_token()  # Lookahead

def statement(self):
    if (self.current_token.type == TokenType.IDENTIFIER and 
        self.next_token.type == TokenType.ASSIGN):
        return self.assignment_statement()
    # ...
```

### Exemplo de Parsing

**Entrada:**
```
x = 10 + 5;
```

**AST gerada:**
```
VarAssignNode(
    var_name='x',
    value=BinOpNode(
        left=NumberNode(10),
        op=PLUS,
        right=NumberNode(5)
    )
)
```

### Tratamento de Erros

O parser implementa **recuperação de erros** com `synchronize()`:

```python
def synchronize(self):
    """Avança até encontrar um ponto seguro após erro."""
    self.advance()
    while self.current_token.type != TokenType.EOF:
        if self.current_token.type in [TokenType.SEMICOLON, TokenType.IF, ...]:
            return
        self.advance()
```

---

## 3. AST Nodes (Nós da Árvore Sintática)

**Arquivo:** `Interpreter/ast_nodes.py`

### Hierarquia de Nós

#### Literais
- `NumberNode`: Valores inteiros e float
- `StringNode`: Strings
- `BooleanNode`: true/false

#### Operações
- `BinOpNode`: Operações binárias (+, -, *, /, ==, <, and, or)
- `UnaryOpNode`: Operações unárias (-, +, not)

#### Variáveis
- `VarAssignNode`: Atribuição (x = valor)
- `VarAccessNode`: Acesso (usar x)

#### Controle de Fluxo
- `IfNode`: if-else
- `WhileNode`: while
- `BreakNode`: break

#### Outros
- `CompoundNode`: Bloco de comandos
- `PrintNode`: print()

### Exemplo de AST Completo

**Código:**
```
if (x > 5) {
    print("Maior");
} else {
    print("Menor");
};
```

**AST:**
```
IfNode(
    condition=BinOpNode(
        left=VarAccessNode('x'),
        op=GT,
        right=NumberNode(5)
    ),
    then_block=PrintNode(
        expr=StringNode("Maior")
    ),
    else_block=PrintNode(
        expr=StringNode("Menor")
    )
)
```

---

## 4. Back-End: Interpretador

**Arquivo:** `Interpreter/interpreter.py`

O interpretador percorre a AST usando o padrão **Visitor**.

### Padrão Visitor

```python
def visit(self, node):
    method_name = f'visit_{type(node).__name__}'
    visitor_method = getattr(self, method_name, self.generic_visit)
    return visitor_method(node)
```

Para cada tipo de nó, existe um método correspondente:

- `visit_NumberNode()`
- `visit_BinOpNode()`
- `visit_IfNode()`
- etc.

### Tabela de Símbolos

Armazena variáveis em um dicionário:

```python
class Interpreter:
    def __init__(self):
        self.symbol_table = {}  # nome → valor
    
    def visit_VarAssignNode(self, node):
        var_name = node.var_name_token.value
        value = self.visit(node.value_node)
        self.symbol_table[var_name] = value
```

### Sistema de Tipos

**Arquivo:** `Interpreter/types.py`

Cada valor é encapsulado em uma classe:

```python
class Integer(Value):
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value), None
        # ...
```

Operações retornam tupla `(resultado, erro)`:

```python
result, error = left.__add__(right)
if error:
    raise Exception(error)
```

### Execução de Controle de Fluxo

**If-Else:**
```python
def visit_IfNode(self, node):
    condition = self.visit(node.condition_node)
    if condition.value:
        return self.visit(node.then_block)
    elif node.else_block:
        return self.visit(node.else_block)
```

**While:**
```python
def visit_WhileNode(self, node):
    while True:
        condition = self.visit(node.condition_node)
        if condition.value:
            try:
                self.visit(node.body_node)
            except BreakException:
                break
        else:
            break
```

**Break:**
```python
class BreakException(Exception):
    pass

def visit_BreakNode(self, node):
    raise BreakException()
```

---

## 5. Back-End: Compilador

**Arquivo:** `Compiler/compiler.py`

O compilador transforma a AST em bytecode.

### Estrutura do Bytecode

**Arquivo:** `Compiler/bytecode.py`

```python
@dataclass
class Chunk:
    code: List[ByteCode]        # Lista de (OpCode, argumento)
    constants: List[any]        # Pool de constantes
    lines: List[int]            # Mapeamento linha fonte
```

### Emissão de Bytecode

```python
def emit_byte(self, opcode: OpCode, line: int):
    self.chunk.write(opcode, 0, line)

def emit_constant(self, value: any, line: int):
    const_index = self.chunk.add_constant(value)
    self.chunk.write(OpCode.OP_LOAD_CONST, const_index, line)
```

### Compilação de Expressões

**Exemplo: `10 + 5`**

```python
def visit_BinOpNode(self, node):
    self.visit(node.left_node)   # Compila 10
    self.visit(node.right_node)  # Compila 5
    
    if node.op_token.type == TokenType.PLUS:
        self.emit_byte(OpCode.OP_ADD, line)
```

**Bytecode gerado:**
```
OP_LOAD_CONST  0  (10)
OP_LOAD_CONST  1  (5)
OP_ADD
```

### Compilação de Controle de Fluxo

**If-Else:**
```python
def visit_IfNode(self, node):
    self.visit(node.condition_node)        # Compila condição
    
    then_jump = self.emit_jump(OP_JUMP_IF_FALSE, line)
    self.visit(node.then_block)            # Compila bloco then
    
    else_jump = self.emit_jump(OP_JUMP_FORWARD, line)
    self.patch_jump(then_jump)             # Corrige salto
    
    if node.else_block:
        self.visit(node.else_block)        # Compila bloco else
    
    self.patch_jump(else_jump)
```

### Patch de Saltos

Saltos são compilados em duas fases:

1. **Emissão**: Cria instrução com placeholder
```python
def emit_jump(self, opcode: OpCode, line: int) -> int:
    self.chunk.write(opcode, 0xFFFF, line)  # Placeholder
    return len(self.chunk.code) - 1          # Retorna índice
```

2. **Patch**: Calcula e corrige o offset
```python
def patch_jump(self, offset: int):
    jump = len(self.chunk.code) - offset - 1
    opcode, _ = self.chunk.code[offset]
    self.chunk.code[offset] = (opcode, jump)
```

### Loops com Break

O compilador mantém uma pilha de contextos de loop:

```python
def visit_WhileNode(self, node):
    self.loop_contexts.append([])  # Inicia contexto
    
    loop_start = len(self.chunk.code)
    # ... compila loop ...
    
    break_jumps = self.loop_contexts.pop()
    for jump in break_jumps:
        self.patch_jump(jump)  # Corrige todos os breaks
```

---

## 6. OpCodes (Códigos de Operação)

**Arquivo:** `Compiler/opcodes.py`

### Categorias de OpCodes

#### Pilha e Constantes
```python
OP_LOAD_CONST   # Empilha constante
OP_POP          # Remove topo da pilha
```

#### Literais
```python
OP_LOAD_TRUE    # Empilha true
OP_LOAD_FALSE   # Empilha false
OP_LOAD_NIL     # Empilha nil/null
```

#### Variáveis Globais
```python
OP_LOAD_GLOBAL  # Carrega valor de variável
OP_STORE_GLOBAL # Armazena em variável
```

#### Operadores Aritméticos
```python
OP_ADD          # +
OP_SUBTRACT     # -
OP_MULTIPLY     # *
OP_DIVIDE       # /
```

#### Operadores de Comparação
```python
OP_EQUAL        # ==
OP_NOT_EQUAL    # !=
OP_GREATER      # >
OP_LESS         # <
OP_GREATER_EQUAL # >=
OP_LESS_EQUAL    # <=
```

#### Operadores Unários
```python
OP_NEGATE       # - (negação numérica)
OP_NOT          # not (negação lógica)
```

#### Controle de Fluxo
```python
OP_JUMP_IF_FALSE   # Pula se falso
OP_JUMP_FORWARD    # Pula para frente
OP_JUMP_BACKWARD   # Pula para trás (loops)
```

#### Funções
```python
OP_CALL_PRINT   # Chama print()
OP_RETURN       # Finaliza execução
```

---

## 7. Disassembler (Depuração)

**Arquivo:** `Compiler/disasembler.py`

Ferramenta para visualizar bytecode gerado.

### Exemplo de Saída

**Código:**
```
x = 10 + 5;
print(x);
```

**Bytecode disassembled:**
```
--- Bytecode Principal ---
0000    1 OP_LOAD_CONST     0 '10'
0001    1 OP_LOAD_CONST     1 '5'
0002    1 OP_ADD
0003    1 OP_LOAD_CONST     2 'x'
0004    1 OP_STORE_GLOBAL   2 'x'
0005    2 OP_LOAD_CONST     2 'x'
0006    2 OP_LOAD_GLOBAL    2 'x'
0007    2 OP_CALL_PRINT
0008   -1 OP_RETURN
--------------------------
```

**Formato:**
```
[offset] [linha] [opcode] [arg] [valor]
```

---

## 8. Fluxo de Execução Completo

### Modo Interpretador

```
1. Ler arquivo code.txt
2. Lexer(text) → tokens
3. Parser(lexer) → AST
4. Interpreter().interpret(AST) → execução
5. Resultados impressos no console
```

### Modo Compilador

```
1. Ler arquivo code.txt
2. Lexer(text) → tokens
3. Parser(lexer) → AST
4. Compiler().compile(AST) → Chunk (bytecode)
5. Disassembler.disassemble(chunk) → visualização
```

---

## 9. Tratamento de Erros

### Erros Léxicos

```python
# lexer.py
def error(self, message: str):
    raise Exception(f'Erro léxico na linha {self.lineno}: {message}')
```

**Exemplos:**
- Caractere inválido: `@`
- String não terminada: `"texto`
- Comentário não fechado: `#{ comentário`

### Erros Sintáticos

```python
# parser.py
def error(self, message: str):
    line = self.current_token.lineno
    print(f'[ERRO SINTÁTICO] Linha {line}: {message}')
    self.had_error = True
    raise SyntaxError
```

Com recuperação:
```python
def synchronize(self):
    """Pula até próximo ponto seguro."""
    while self.current_token.type != TokenType.EOF:
        if self.current_token.type in [TokenType.SEMICOLON, ...]:
            return
        self.advance()
```

### Erros Semânticos

```python
# interpreter.py
# Variável não definida
if value is None:
    raise NameError(f"Variável '{var_name}' não definida")

# Tipo incompatível
if error_msg:
    raise Exception(f"Erro na linha {line}: {error_msg}")
```

### Erros de Compilação

```python
# compiler.py
# Break fora de loop
if not self.loop_contexts:
    raise Exception(f"'break' só pode ser usado dentro de um laço")
```

---

## 10. Otimizações Implementadas

### Reutilização de Constantes

```python
def add_constant(self, value: any) -> int:
    try:
        return self.constants.index(value)  # Reutiliza existente
    except ValueError:
        self.constants.append(value)
        return len(self.constants) - 1
```

### Conversão Automática de Tipos

```python
# Integer + Float → resultado apropriado
result = float(self.value) + other.value
if result % 1 == 0:
    return Integer(int(result)), None  # Mantém Integer se possível
return Float(result), None
```

### Eliminação de Código Morto (Expressões)

```python
# Em CompoundNode, expressões isoladas são removidas da pilha
is_expression_statement = isinstance(child, (...))
if is_expression_statement:
    self.emit_byte(OpCode.OP_POP, line)
```

---

## Conclusão

A arquitetura do projeto demonstra conceitos fundamentais de compiladores:

- **Front-end**: Análise léxica e sintática
- **Representação intermediária**: AST
- **Back-end**: Interpretação ou compilação para bytecode
- **Tratamento de erros**: Em cada fase
- **Otimizações**: Reutilização e conversões inteligentes

Esta estrutura modular permite fácil extensão e manutenção do compilador.
