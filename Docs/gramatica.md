# Gramática Formal da Linguagem

Esta gramática descreve a sintaxe completa da linguagem de programação.

**Notação:** `[]` = opcional, `*` = zero ou mais, `+` = um ou mais, `|` = ou

---

## 1. Programa

```ebnf
programa         ::= declaração* EOF

declaração       ::= instrução_break
                   | instrução_atribuição
                   | instrução_while
                   | instrução_if
                   | instrução_expressão

instrução_expressão ::= expressão ';'
```

---

## 2. Declarações/Instruções

### Break
```ebnf
instrução_break  ::= 'break' ';'
```

### Atribuição
```ebnf
instrução_atribuição ::= IDENTIFICADOR '=' expressão ';'
```

### If-Else
```ebnf
instrução_if     ::= 'if' '(' expressão ')' '{' bloco_composto '}' 
                     ['else' (instrução_if | '{' bloco_composto '}')]
```

### While
```ebnf
instrução_while  ::= 'while' '(' expressão ')' '{' bloco_composto '}'
```

### Bloco Composto
```ebnf
bloco_composto   ::= (declaração ';'?)*
```

---

## 3. Expressões (em ordem de precedência)

### Nível 1: OR Lógico (menor precedência)
```ebnf
expressão        ::= and_expressão ('or' and_expressão)*
```

### Nível 2: AND Lógico
```ebnf
and_expressão    ::= comp_expressão ('and' comp_expressão)*
```

### Nível 3: Comparação
```ebnf
comp_expressão   ::= arit_expressão (operador_comp arit_expressão)*

operador_comp    ::= '==' | '!=' | '<' | '>' | '<=' | '>='
```

### Nível 4: Adição e Subtração
```ebnf
arit_expressão   ::= termo (operador_adit termo)*

operador_adit    ::= '+' | '-'
```

### Nível 5: Multiplicação e Divisão
```ebnf
termo            ::= fator (operador_mult fator)*

operador_mult    ::= '*' | '/'
```

### Nível 6: Operadores Unários e Literais (maior precedência)
```ebnf
fator            ::= operador_unário fator
                   | literal
                   | IDENTIFICADOR
                   | '(' expressão ')'
                   | instrução_print

operador_unário  ::= 'not' | '-' | '+'

literal          ::= INTEGER
                   | FLOAT
                   | STRING
                   | BOOLEAN

instrução_print  ::= 'print' '(' expressão ')'
```

---

## 4. Tokens (Elementos Léxicos)

### Literais

```ebnf
INTEGER          ::= ['-']? DÍGITO+
FLOAT            ::= ['-']? DÍGITO+ '.' DÍGITO+
STRING           ::= '"' CARACTERE* '"'
BOOLEAN          ::= 'true' | 'false'
```

### Identificadores

```ebnf
IDENTIFICADOR    ::= (LETRA | '_') (LETRA | DÍGITO | '_')*
```

### Palavras Reservadas

```ebnf
PALAVRA_RESERVADA ::= 'if' | 'else' | 'while' | 'print' | 'break'
                    | 'true' | 'false' | 'and' | 'or' | 'not'
```

### Operadores

```ebnf
# Operadores Aritméticos
OP_ARITMETICO    ::= '+' | '-' | '*' | '/'

# Operadores de Comparação
OP_COMPARAÇÃO    ::= '==' | '!=' | '<' | '>' | '<=' | '>='

# Operadores Lógicos
OP_LÓGICO        ::= 'and' | 'or' | 'not'
```

### Delimitadores e Outros

```ebnf
# Delimitadores
DELIMITADOR      ::= ';' | '(' | ')' | '{' | '}'

# Atribuição
ATRIBUIÇÃO       ::= '='

# Comentários
COMENTÁRIO       ::= '#{' QUALQUER_CARACTERE* '}#'
```

### Elementos Básicos

```ebnf
DÍGITO           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
LETRA            ::= 'a'..'z' | 'A'..'Z'
CARACTERE        ::= qualquer caractere exceto '"'
ESPAÇO           ::= ' ' | '\t' | '\n' | '\r'
```

---

## 5. Precedência de Operadores

| Nível | Operadores | Descrição | Precedência |
|-------|-----------|-----------|-------------|
| 1 | `( )` | Parênteses | Maior |
| 2 | `not`, `-` (unário), `+` (unário) | Operadores Unários | ↓ |
| 3 | `*`, `/` | Multiplicação, Divisão | ↓ |
| 4 | `+`, `-` | Adição, Subtração | ↓ |
| 5 | `<`, `>`, `<=`, `>=` | Comparação Relacional | ↓ |
| 6 | `==`, `!=` | Comparação de Igualdade | ↓ |
| 7 | `and` | AND Lógico | ↓ |
| 8 | `or` | OR Lógico | Menor |

---

## 6. Associatividade

| Tipo de Operador | Associatividade |
|------------------|-----------------|
| Operadores Binários | À Esquerda |
| Operadores Unários | À Direita |
| Atribuição | À Direita |

---

## 7. Regras Semânticas

### 7.1 Tipos de Dados

| Tipo | Descrição |
|------|-----------|
| `Integer` | Números inteiros (-2147483648 a 2147483647) |
| `Float` | Números de ponto flutuante |
| `String` | Cadeia de caracteres entre aspas duplas |
| `Boolean` | `true` ou `false` |

### 7.2 Conversões de Tipo

| Operação | Resultado |
|----------|-----------|
| `Integer + Float` | `Float` (ou `Integer` se resultado for inteiro exato) |
| `Float + Float` | `Float` (ou `Integer` se resultado for inteiro exato) |
| `Integer + Integer` | `Integer` |
| `String + qualquer` | `String` (concatenação) |
| `Integer * String` | `String` (repetição) |
| `String * Integer` | `String` (repetição) |

### 7.3 Operações Permitidas por Tipo

| Tipo | Operações Permitidas |
|------|---------------------|
| `Integer` | `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `Float` | `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `String` | `+` (concat), `*` (repetição), `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `Boolean` | `==`, `!=`, `and`, `or`, `not` |

### 7.4 Escopo

- Todas as variáveis são **globais**
- Variáveis devem ser **inicializadas antes do uso**
- Não há **declaração explícita** de variáveis

### 7.5 Controle de Fluxo

- `break` só pode aparecer dentro de `while`
- Condições em `if` e `while` devem resultar em `Boolean`
- Blocos sempre delimitados por `{` e `}`

---

## 8. Exemplos de Sintaxe Válida

### 8.1 Declaração de Variáveis

```javascript
x = 10;
nome = "João";
ativo = true;
resultado = 3.14;
```

### 8.2 Expressões Aritméticas

```javascript
soma = a + b;
media = (a + b + c) / 3;
area = base * altura / 2;
```

### 8.3 Expressões Lógicas

```javascript
valido = idade >= 18 and tem_permissao;
pode_sair = fim_semana or feriado;
negacao = not ativo;
```

### 8.4 Estrutura If-Else

```javascript
// If simples
if (x > 5) {
    print("Maior");
};

// If-Else
if (idade >= 18) {
    print("Maior de idade");
} else {
    print("Menor de idade");
};

// If-Else encadeado
if (nota >= 7) {
    print("Aprovado");
} else if (nota >= 5) {
    print("Recuperação");
} else {
    print("Reprovado");
};
```

### 8.5 Estrutura While

```javascript
i = 0;
while (i < 10) {
    print(i);
    i = i + 1;
};
```

### 8.6 Break

```javascript
i = 0;
while (i < 100) {
    if (i == 50) {
        break;
    };
    i = i + 1;
};
```

### 8.7 Comentários

```javascript
#{ Este é um comentário em bloco }#

#{
  Comentário
  de múltiplas
  linhas
}#

x = 10; #{ Comentário inline }#
```

---

## 9. Restrições Sintáticas

1. ✓ Toda instrução deve terminar com `;`
2. ✓ Blocos de código devem usar `{` e `}`
3. ✓ Condições devem estar entre `(` e `)`
4. ✓ Strings devem usar aspas duplas `"`
5. ✓ Comentários devem usar `#{` e `}#`
6. ✓ Identificadores não podem começar com dígito
7. ✓ Identificadores não podem ser palavras reservadas
8. ✓ Não pode haver espaços em branco dentro de tokens
9. ✓ `break` só é válido dentro de `while`
10. ✓ Expressões devem resultar em um valor

---

## 10. Notação BNF Estendida (EBNF) Formal

```ebnf
<programa>         ::= { <declaração> } <EOF>

<declaração>       ::= <instr_break>
                     | <instr_atribuição>
                     | <instr_while>
                     | <instr_if>
                     | <expressão> ";"

<instr_break>      ::= "break" ";"

<instr_atribuição> ::= <identificador> "=" <expressão> ";"

<instr_if>         ::= "if" "(" <expressão> ")" "{" <bloco> "}"
                       [ "else" ( <instr_if> | "{" <bloco> "}" ) ]

<instr_while>      ::= "while" "(" <expressão> ")" "{" <bloco> "}"

<bloco>            ::= { <declaração> [ ";" ] }

<expressão>        ::= <and_expr> { "or" <and_expr> }

<and_expr>         ::= <comp_expr> { "and" <comp_expr> }

<comp_expr>        ::= <arit_expr> { <op_comp> <arit_expr> }

<op_comp>          ::= "==" | "!=" | "<" | ">" | "<=" | ">="

<arit_expr>        ::= <termo> { ("+" | "-") <termo> }

<termo>            ::= <fator> { ("*" | "/") <fator> }

<fator>            ::= ("not" | "-" | "+") <fator>
                     | <literal>
                     | <identificador>
                     | "(" <expressão> ")"
                     | "print" "(" <expressão> ")"

<literal>          ::= <integer> | <float> | <string> | <boolean>

<integer>          ::= [ "-" ] <dígito> { <dígito> }

<float>            ::= [ "-" ] <dígito> { <dígito> } "." <dígito> { <dígito> }

<string>           ::= '"' { <caractere> } '"'

<boolean>          ::= "true" | "false"

<identificador>    ::= ( <letra> | "_" ) { <letra> | <dígito> | "_" }

<dígito>           ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<letra>            ::= "a" .. "z" | "A" .. "Z"

<caractere>        ::= qualquer caractere Unicode exceto '"'
```

---

## Diagrama de Fluxo de Compilação

```
Código Fonte
     ↓
  LEXER (Análise Léxica)
     ↓
  Tokens
     ↓
  PARSER (Análise Sintática)
     ↓
  AST (Árvore Sintática Abstrata)
     ↓
  ┌─────────────────┐
  │                 │
  ↓                 ↓
INTERPRETER     COMPILER
  ↓                 ↓
Execução        Bytecode
Direta            ↓
                  VM
                  ↓
                Execução
```

---

## Referências

- **Lexer:** `Interpreter/lexer.py`
- **Parser:** `Interpreter/parser.py`
- **AST Nodes:** `Interpreter/ast_nodes.py`
- **Interpreter:** `Interpreter/interpreter.py`
- **Compiler:** `Compiler/compiler.py`
- **OpCodes:** `Compiler/opcodes.py`
- **Bytecode:** `Compiler/bytecode.py`
- **Disassembler:** `Compiler/disasembler.py`

---

**Última Atualização:** 22 de outubro de 2025
