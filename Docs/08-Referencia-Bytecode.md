# Referência de Bytecode

Este documento fornece uma referência completa de todos os opcodes (códigos de operação) usados pelo compilador de bytecode.

## Introdução ao Bytecode

O **bytecode** é uma representação intermediária do código fonte, mais próxima da máquina que o código fonte original, mas ainda independente de plataforma. Cada instrução de bytecode consiste em:

- **OpCode**: Código da operação (ex: OP_ADD)
- **Argumento**: Valor opcional usado pela instrução (ex: índice de constante)
- **Linha**: Número da linha no código fonte (para debugging)

### Formato do Bytecode

```python
ByteCode = Tuple[OpCode, int]

Chunk = {
    'code': [(OpCode, arg), (OpCode, arg), ...],
    'constants': [valor1, valor2, ...],
    'lines': [linha1, linha2, ...]
}
```

---

## Modelo de Execução: Pilha

O bytecode opera usando uma **máquina de pilha**:

- Operandos são empilhados (push)
- Operadores consomem operandos do topo e empilham resultado
- Variáveis são acessadas através de índices no pool de constantes

### Exemplo Visual

**Código:** `10 + 5`

**Bytecode:**
```
OP_LOAD_CONST 0    # Empilha 10
OP_LOAD_CONST 1    # Empilha 5
OP_ADD             # Desempilha 5 e 10, empilha 15
```

**Pilha durante execução:**
```
Passo 1:  [10]
Passo 2:  [10, 5]
Passo 3:  [15]
```

---

## Categorias de OpCodes

### 1. Pilha e Constantes

#### `OP_LOAD_CONST`

**Descrição:** Carrega uma constante do pool e empilha.

**Argumento:** Índice da constante no array `constants`

**Comportamento da Pilha:** `[] → [valor]`

**Exemplo:**
```python
# Bytecode
OP_LOAD_CONST 0   # constants[0] = 42

# Pilha
[] → [42]
```

**Gerado por:**
```
x = 42;
#    ^^ gera OP_LOAD_CONST
```

---

#### `OP_POP`

**Descrição:** Remove e descarta o valor no topo da pilha.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[valor] → []`

**Exemplo:**
```python
# Pilha antes: [42, 10]
OP_POP
# Pilha depois: [42]
```

**Gerado por:**
```
10 + 5;  # Expressão-statement (resultado descartado)
```

---

### 2. Literais Booleanos

#### `OP_LOAD_TRUE`

**Descrição:** Empilha o valor booleano `true`.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[] → [true]`

**Exemplo:**
```python
OP_LOAD_TRUE
# Pilha: [true]
```

**Gerado por:**
```
ativo = true;
#       ^^^^ gera OP_LOAD_TRUE
```

---

#### `OP_LOAD_FALSE`

**Descrição:** Empilha o valor booleano `false`.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[] → [false]`

**Exemplo:**
```python
OP_LOAD_FALSE
# Pilha: [false]
```

**Gerado por:**
```
ativo = false;
#       ^^^^^ gera OP_LOAD_FALSE
```

---

#### `OP_LOAD_NIL`

**Descrição:** Empilha um valor nulo/vazio (reservado para uso futuro).

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[] → [nil]`

**Status:** Definido mas não usado atualmente.

---

### 3. Variáveis Globais

#### `OP_LOAD_GLOBAL`

**Descrição:** Carrega o valor de uma variável global e empilha.

**Argumento:** Índice do nome da variável no pool de constantes

**Comportamento da Pilha:** `[] → [valor_variável]`

**Exemplo:**
```python
# constants[0] = "x"
# globals["x"] = 42

OP_LOAD_GLOBAL 0
# Pilha: [42]
```

**Gerado por:**
```
print(x);  # Acesso à variável x
#     ^ gera OP_LOAD_GLOBAL
```

**Erro:** Se a variável não existir, erro em tempo de execução.

---

#### `OP_STORE_GLOBAL`

**Descrição:** Armazena o topo da pilha em uma variável global.

**Argumento:** Índice do nome da variável no pool de constantes

**Comportamento da Pilha:** `[valor] → []`

**Exemplo:**
```python
# Pilha antes: [42]
# constants[0] = "x"

OP_STORE_GLOBAL 0
# globals["x"] = 42
# Pilha depois: []
```

**Gerado por:**
```
x = 42;
# ^ gera OP_STORE_GLOBAL
```

---

### 4. Operadores Aritméticos

Todos os operadores aritméticos seguem o padrão:
- Desempilham dois valores (direita primeiro, depois esquerda)
- Executam a operação
- Empilham o resultado

#### `OP_ADD`

**Descrição:** Soma dois valores ou concatena strings.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [resultado]`

**Exemplo:**
```python
# Pilha antes: [10, 5]
OP_ADD
# Pilha depois: [15]
```

**Gerado por:**
```
x = 10 + 5;
#      ^ gera OP_ADD
```

**Tipos suportados:**
- Integer + Integer → Integer
- Float + Float → Float/Integer
- Integer + Float → Float/Integer
- String + qualquer → String (concatenação)

---

#### `OP_SUBTRACT`

**Descrição:** Subtrai o segundo valor do primeiro.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [resultado]`

**Exemplo:**
```python
# Pilha antes: [10, 3]
OP_SUBTRACT
# Pilha depois: [7]
```

**Gerado por:**
```
x = 10 - 3;
#      ^ gera OP_SUBTRACT
```

---

#### `OP_MULTIPLY`

**Descrição:** Multiplica dois valores ou repete string.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [resultado]`

**Exemplo:**
```python
# Pilha antes: [5, 3]
OP_MULTIPLY
# Pilha depois: [15]
```

**Gerado por:**
```
x = 5 * 3;
#     ^ gera OP_MULTIPLY
```

**Casos especiais:**
- String * Integer → String repetida
- Integer * String → String repetida

---

#### `OP_DIVIDE`

**Descrição:** Divide o primeiro valor pelo segundo.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [resultado]`

**Exemplo:**
```python
# Pilha antes: [10, 2]
OP_DIVIDE
# Pilha depois: [5]
```

**Gerado por:**
```
x = 10 / 2;
#      ^ gera OP_DIVIDE
```

**Erro:** Divisão por zero gera erro em tempo de execução.

---

### 5. Operadores de Comparação

#### `OP_EQUAL`

**Descrição:** Verifica igualdade entre dois valores.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Exemplo:**
```python
# Pilha antes: [10, 10]
OP_EQUAL
# Pilha depois: [true]
```

**Gerado por:**
```
x == y
#  ^^ gera OP_EQUAL
```

---

#### `OP_NOT_EQUAL`

**Descrição:** Verifica desigualdade entre dois valores.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Exemplo:**
```python
# Pilha antes: [10, 5]
OP_NOT_EQUAL
# Pilha depois: [true]
```

**Gerado por:**
```
x != y
#  ^^ gera OP_NOT_EQUAL
```

---

#### `OP_GREATER`

**Descrição:** Verifica se primeiro valor é maior que segundo.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Exemplo:**
```python
# Pilha antes: [10, 5]
OP_GREATER
# Pilha depois: [true]
```

**Gerado por:**
```
x > y
#   ^ gera OP_GREATER
```

---

#### `OP_LESS`

**Descrição:** Verifica se primeiro valor é menor que segundo.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Exemplo:**
```python
# Pilha antes: [5, 10]
OP_LESS
# Pilha depois: [true]
```

**Gerado por:**
```
x < y
#   ^ gera OP_LESS
```

---

#### `OP_GREATER_EQUAL`

**Descrição:** Verifica se primeiro valor é maior ou igual ao segundo.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Gerado por:**
```
x >= y
#  ^^ gera OP_GREATER_EQUAL
```

---

#### `OP_LESS_EQUAL`

**Descrição:** Verifica se primeiro valor é menor ou igual ao segundo.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[esq, dir] → [boolean]`

**Gerado por:**
```
x <= y
#  ^^ gera OP_LESS_EQUAL
```

---

### 6. Operadores Unários

#### `OP_NEGATE`

**Descrição:** Inverte o sinal de um número.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[valor] → [-valor]`

**Exemplo:**
```python
# Pilha antes: [10]
OP_NEGATE
# Pilha depois: [-10]
```

**Gerado por:**
```
x = -10;
#   ^ gera OP_NEGATE
```

---

#### `OP_NOT`

**Descrição:** Inverte um valor booleano.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[boolean] → [!boolean]`

**Exemplo:**
```python
# Pilha antes: [true]
OP_NOT
# Pilha depois: [false]
```

**Gerado por:**
```
x = not true;
#   ^^^ gera OP_NOT
```

---

### 7. Controle de Fluxo

#### `OP_JUMP_IF_FALSE`

**Descrição:** Pula para frente se o topo da pilha for falso. Desempilha o valor.

**Argumento:** Offset de salto (quantas instruções pular)

**Comportamento da Pilha:** `[boolean] → []`

**Exemplo:**
```python
# Pilha antes: [false]
# IP (Instruction Pointer) = 5

OP_JUMP_IF_FALSE 10
# Como valor é false, pula 10 instruções
# IP = 5 + 1 + 10 = 16
# Pilha depois: []
```

**Gerado por:**
```
if (condicao) { ... }
#   ^^^^^^^^ testa condição e pula se falsa
```

---

#### `OP_JUMP_FORWARD`

**Descrição:** Pula incondicionalmente para frente.

**Argumento:** Offset de salto (quantas instruções pular)

**Comportamento da Pilha:** Nenhuma alteração

**Exemplo:**
```python
# IP = 10

OP_JUMP_FORWARD 5
# IP = 10 + 1 + 5 = 16
```

**Gerado por:**
```
if (x) { 
    # bloco then
} else {  # ← OP_JUMP_FORWARD para pular o else
    # bloco else
}
```

---

#### `OP_JUMP_BACKWARD`

**Descrição:** Pula incondicionalmente para trás (usado em loops).

**Argumento:** Offset de salto (quantas instruções voltar)

**Comportamento da Pilha:** Nenhuma alteração

**Exemplo:**
```python
# IP = 20

OP_JUMP_BACKWARD 15
# IP = 20 + 1 - 15 = 6  (volta para instrução 6)
```

**Gerado por:**
```
while (condicao) {
    # corpo do loop
}  # ← OP_JUMP_BACKWARD para voltar à condição
```

---

### 8. Funções e Saída

#### `OP_CALL_PRINT`

**Descrição:** Chama a função nativa `print()`, imprimindo o topo da pilha.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** `[valor] → []`

**Exemplo:**
```python
# Pilha antes: [42]
OP_CALL_PRINT
# Saída no console: 42
# Pilha depois: []
```

**Gerado por:**
```
print(x);
# ^^^^ gera OP_CALL_PRINT
```

---

#### `OP_RETURN`

**Descrição:** Finaliza a execução do programa.

**Argumento:** Nenhum (sempre 0)

**Comportamento da Pilha:** Nenhuma alteração

**Exemplo:**
```python
OP_RETURN
# Execução termina
```

**Gerado por:** Automaticamente inserido no final de todo programa.

---

## Exemplos Completos de Compilação

### Exemplo 1: Atribuição Simples

**Código:**
```
x = 42;
```

**Bytecode:**
```
0000  1  OP_LOAD_CONST    0  '42'
0001  1  OP_STORE_GLOBAL  1  'x'
0002 -1  OP_RETURN
```

**Execução:**
```
Step 1: Pilha=[] → Pilha=[42]              (OP_LOAD_CONST)
Step 2: Pilha=[42], globals[x]=42 → Pilha=[] (OP_STORE_GLOBAL)
Step 3: Fim                                 (OP_RETURN)
```

---

### Exemplo 2: Expressão Aritmética

**Código:**
```
resultado = (10 + 5) * 2;
```

**Bytecode:**
```
0000  1  OP_LOAD_CONST    0  '10'
0001  1  OP_LOAD_CONST    1  '5'
0002  1  OP_ADD
0003  1  OP_LOAD_CONST    2  '2'
0004  1  OP_MULTIPLY
0005  1  OP_STORE_GLOBAL  3  'resultado'
0006 -1  OP_RETURN
```

**Execução:**
```
[10]           ← OP_LOAD_CONST 10
[10, 5]        ← OP_LOAD_CONST 5
[15]           ← OP_ADD (10+5)
[15, 2]        ← OP_LOAD_CONST 2
[30]           ← OP_MULTIPLY (15*2)
[]             ← OP_STORE_GLOBAL resultado=30
```

---

### Exemplo 3: Condicional If-Else

**Código:**
```
if (x > 5) {
    print("Maior");
} else {
    print("Menor");
};
```

**Bytecode:**
```
0000  1  OP_LOAD_GLOBAL    0  'x'
0001  1  OP_LOAD_CONST     1  '5'
0002  1  OP_GREATER
0003  1  OP_JUMP_IF_FALSE  2   → pula para 0006 se falso
0004  2  OP_LOAD_CONST     2  'Maior'
0005  2  OP_CALL_PRINT
0006  2  OP_JUMP_FORWARD   2   → pula para 0009 (pula o else)
0007  4  OP_LOAD_CONST     3  'Menor'
0008  4  OP_CALL_PRINT
0009 -1  OP_RETURN
```

**Execução (assumindo x=10):**
```
[10]          ← OP_LOAD_GLOBAL x
[10, 5]       ← OP_LOAD_CONST 5
[true]        ← OP_GREATER (10>5)
[]            ← OP_JUMP_IF_FALSE (não pula, continua)
["Maior"]     ← OP_LOAD_CONST "Maior"
[]            ← OP_CALL_PRINT → imprime "Maior"
              ← OP_JUMP_FORWARD → pula para 0009
              ← OP_RETURN
```

---

### Exemplo 4: Loop While

**Código:**
```
i = 0;
while (i < 3) {
    print(i);
    i = i + 1;
};
```

**Bytecode:**
```
0000  1  OP_LOAD_CONST     0  '0'
0001  1  OP_STORE_GLOBAL   1  'i'
0002  2  OP_LOAD_GLOBAL    1  'i'         ← loop_start
0003  2  OP_LOAD_CONST     2  '3'
0004  2  OP_LESS
0005  2  OP_JUMP_IF_FALSE  7   → sai para 0013
0006  3  OP_LOAD_GLOBAL    1  'i'
0007  3  OP_CALL_PRINT
0008  4  OP_LOAD_GLOBAL    1  'i'
0009  4  OP_LOAD_CONST     0  '1'
0010  4  OP_ADD
0011  4  OP_STORE_GLOBAL   1  'i'
0012  4  OP_JUMP_BACKWARD  11  → volta para 0002
0013 -1  OP_RETURN
```

**Execução (resumida):**
```
Iteração 1: i=0 → print(0) → i=1 → volta para 0002
Iteração 2: i=1 → print(1) → i=2 → volta para 0002
Iteração 3: i=2 → print(2) → i=3 → volta para 0002
Iteração 4: i=3 → (i<3 = false) → sai do loop
```

---

### Exemplo 5: Loop com Break

**Código:**
```
i = 0;
while (i < 10) {
    if (i == 5) {
        break;
    };
    i = i + 1;
};
```

**Bytecode:**
```
0000  1  OP_LOAD_CONST     0  '0'
0001  1  OP_STORE_GLOBAL   1  'i'
0002  2  OP_LOAD_GLOBAL    1  'i'         ← loop_start
0003  2  OP_LOAD_CONST     2  '10'
0004  2  OP_LESS
0005  2  OP_JUMP_IF_FALSE  11  → sai para 0017
0006  3  OP_LOAD_GLOBAL    1  'i'
0007  3  OP_LOAD_CONST     3  '5'
0008  3  OP_EQUAL
0009  3  OP_JUMP_IF_FALSE  2   → pula para 0012 se não for 5
0010  4  OP_JUMP_FORWARD   6   → BREAK: pula para 0017
0011  4  OP_POP
0012  6  OP_LOAD_GLOBAL    1  'i'
0013  6  OP_LOAD_CONST     0  '1'
0014  6  OP_ADD
0015  6  OP_STORE_GLOBAL   1  'i'
0016  6  OP_JUMP_BACKWARD  15  → volta para 0002
0017 -1  OP_RETURN
```

---

## Tabela Resumo de OpCodes

| OpCode | Argumento | Pilha | Descrição |
|--------|-----------|-------|-----------|
| `OP_LOAD_CONST` | índice | `[] → [val]` | Carrega constante |
| `OP_POP` | - | `[val] → []` | Remove topo |
| `OP_LOAD_TRUE` | - | `[] → [true]` | Carrega true |
| `OP_LOAD_FALSE` | - | `[] → [false]` | Carrega false |
| `OP_LOAD_GLOBAL` | índice | `[] → [val]` | Carrega variável |
| `OP_STORE_GLOBAL` | índice | `[val] → []` | Armazena variável |
| `OP_ADD` | - | `[a,b] → [a+b]` | Soma |
| `OP_SUBTRACT` | - | `[a,b] → [a-b]` | Subtração |
| `OP_MULTIPLY` | - | `[a,b] → [a*b]` | Multiplicação |
| `OP_DIVIDE` | - | `[a,b] → [a/b]` | Divisão |
| `OP_EQUAL` | - | `[a,b] → [a==b]` | Igualdade |
| `OP_NOT_EQUAL` | - | `[a,b] → [a!=b]` | Desigualdade |
| `OP_GREATER` | - | `[a,b] → [a>b]` | Maior que |
| `OP_LESS` | - | `[a,b] → [a<b]` | Menor que |
| `OP_GREATER_EQUAL` | - | `[a,b] → [a>=b]` | Maior ou igual |
| `OP_LESS_EQUAL` | - | `[a,b] → [a<=b]` | Menor ou igual |
| `OP_NEGATE` | - | `[a] → [-a]` | Negação numérica |
| `OP_NOT` | - | `[a] → [!a]` | Negação lógica |
| `OP_JUMP_IF_FALSE` | offset | `[b] → []` | Pula se falso |
| `OP_JUMP_FORWARD` | offset | - | Pula para frente |
| `OP_JUMP_BACKWARD` | offset | - | Pula para trás |
| `OP_CALL_PRINT` | - | `[val] → []` | Imprime valor |
| `OP_RETURN` | - | - | Finaliza execução |

---

## Notas Técnicas

### Pool de Constantes

Todas as constantes literais e nomes de variáveis são armazenados em um array único:

```python
constants = [42, "texto", 3.14, "x", "y"]
#            0    1       2     3    4
```

### Otimização: Reutilização

O compilador reutiliza constantes idênticas:

```
x = 10;
y = 10;  # Reutiliza a mesma constante 10
```

### Mapeamento de Linhas

Cada bytecode mantém referência à linha do código fonte para mensagens de erro precisas.

### Limitações Atuais

- Não há VM implementada (bytecode só é visualizado)
- Não há suporte a funções definidas pelo usuário
- Variáveis são sempre globais
- Sem garbage collection (irrelevante sem VM)
