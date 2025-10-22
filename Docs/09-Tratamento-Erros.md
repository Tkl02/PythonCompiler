# Tratamento de Erros e Depuração

Este documento explica como a linguagem lida com erros e fornece ferramentas para depuração.

## Tipos de Erros

A linguagem detecta erros em diferentes fases da compilação/interpretação:

### 1. Erros Léxicos

Ocorrem durante a tokenização, quando caracteres inválidos são encontrados.

#### Caractere Inválido

**Código com erro:**
```
x = 10 @ 5;
```

**Mensagem de erro:**
```
Erro léxico na linha 1: Caractere inválido -> "@"
```

**Causa:** O caractere `@` não é reconhecido pela linguagem.

---

#### String Não Terminada

**Código com erro:**
```
nome = "João Silva;
```

**Mensagem de erro:**
```
Erro léxico na linha 1: String não terminada. Faltando '"'.
```

**Causa:** Falta a aspa dupla de fechamento.

**Correção:**
```
nome = "João Silva";
```

---

#### Comentário Não Fechado

**Código com erro:**
```
#{
  Este comentário não foi fechado
  x = 10;
```

**Mensagem de erro:**
```
Erro léxico: Comentário em bloco não terminado. Faltando '}#'.
```

**Causa:** Falta o fechamento `}#`.

**Correção:**
```
#{
  Este comentário foi fechado corretamente
  x = 10;
}#
```

---

### 2. Erros Sintáticos

Ocorrem quando a estrutura do código não segue a gramática da linguagem.

#### Falta de Ponto e Vírgula

**Código com erro:**
```
x = 10
y = 20;
```

**Mensagem de erro:**
```
[ERRO SINTÁTICO] Linha 2: Esperado 'SEMICOLON', mas encontrado 'IDENTIFIER'
```

**Causa:** Falta `;` no final da primeira linha.

**Correção:**
```
x = 10;
y = 20;
```

---

#### Parênteses Não Balanceados

**Código com erro:**
```
if (x > 5 {
    print("Maior");
};
```

**Mensagem de erro:**
```
[ERRO SINTÁTICO] Linha 1: Esperado 'RPAREN', mas encontrado 'LBRACE'
```

**Causa:** Falta o `)` após a condição.

**Correção:**
```
if (x > 5) {
    print("Maior");
};
```

---

#### Falta de Chaves

**Código com erro:**
```
if (x > 5)
    print("Maior");
;
```

**Mensagem de erro:**
```
[ERRO SINTÁTICO] Linha 1: Esperado 'LBRACE', mas encontrado 'PRINT'
```

**Causa:** Blocos `if` devem usar chaves.

**Correção:**
```
if (x > 5) {
    print("Maior");
};
```

---

#### Expressão Incompleta

**Código com erro:**
```
x = 10 + ;
```

**Mensagem de erro:**
```
[ERRO SINTÁTICO] Linha 1: Fator inválido, esperado literal, identificador, print, 'not', '+', '-' ou '('
```

**Causa:** Operador `+` sem operando à direita.

**Correção:**
```
x = 10 + 5;
```

---

### 3. Erros Semânticos

Ocorrem quando o código é sintaticamente correto, mas semanticamente inválido.

#### Variável Não Definida

**Código com erro:**
```
x = 10;
y = x + z;  #{ z não foi definida }#
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 2: Variável 'z' não definida.
```

**Causa:** Tentativa de usar variável antes de atribuir valor.

**Correção:**
```
x = 10;
z = 5;
y = x + z;
```

---

#### Tipo Incompatível em Operação

**Código com erro:**
```
texto = "Olá";
resultado = texto - 5;
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 2: TypeError: Operador '-' inválido para o tipo String
```

**Causa:** String não suporta subtração.

**Correção:**
```
texto = "Olá";
resultado = texto + " Mundo";  #{ Use concatenação }#
```

---

#### Operação com Tipos Incompatíveis

**Código com erro:**
```
a = 10;
b = "texto";
c = a - b;
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 3: TypeError: Operador '-' inválido entre Inteiro e String
```

**Causa:** Não é possível subtrair String de Integer.

**Correção:**
```
a = 10;
b = 5;  #{ Use um número }#
c = a - b;
```

---

#### Operador Lógico com Não-Booleanos

**Código com erro:**
```
a = 10;
b = 5;
resultado = a and b;
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 3: TypeError: Operador 'and' só pode ser usado com booleanos.
```

**Causa:** `and` requer operandos Boolean.

**Correção:**
```
a = true;
b = false;
resultado = a and b;

#{ OU use comparações }#
a = 10;
b = 5;
resultado = (a > 0) and (b > 0);
```

---

#### Divisão por Zero

**Código com erro:**
```
x = 10 / 0;
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 1: ZeroDivisionError: Divisão por zero
```

**Causa:** Divisão por zero não é permitida.

**Correção:**
```
divisor = 5;  #{ Use valor diferente de zero }#
x = 10 / divisor;
```

---

#### Comparação de Tipos Incompatíveis

**Código com erro:**
```
a = "texto";
b = 10;
resultado = a < b;
```

**Mensagem de erro:**
```
erro na execução do codigo: Erro na linha 3: TypeError: Não é possível comparar String com Integer
```

**Causa:** Comparação `<`, `>`, `<=`, `>=` entre String e Integer não é permitida.

**Correção:**
```
#{ Compare tipos compatíveis }#
a = "abc";
b = "xyz";
resultado = a < b;  #{ Comparação lexicográfica }#

#{ OU }#
a = 10;
b = 20;
resultado = a < b;  #{ Comparação numérica }#
```

---

### 4. Erros de Controle de Fluxo

#### Break Fora de Loop

**Código com erro:**
```
x = 10;
if (x > 5) {
    break;  #{ break só pode estar em loop }#
};
```

**Mensagem de erro (modo compilador):**
```
Ocorreu um erro: Erro na linha 3: 'Break' so pode ser usado dentro de um laço
```

**Causa:** `break` só é válido dentro de `while`.

**Correção:**
```
i = 0;
while (i < 10) {
    if (i == 5) {
        break;  #{ Agora está correto }#
    };
    i = i + 1;
};
```

---

## Recuperação de Erros

O parser implementa recuperação de erros para continuar a análise após encontrar um erro.

### Sincronização

Quando um erro sintático é detectado, o parser:

1. Marca que houve erro (`had_error = True`)
2. Chama `synchronize()` para pular até um ponto seguro
3. Continua analisando o resto do código

**Pontos de sincronização:**
- Ponto e vírgula (`;`)
- Início de declaração (`if`, `while`, `print`)
- Fim de arquivo (`EOF`)

### Exemplo de Recuperação

**Código com múltiplos erros:**
```
a = 10 + ;          #{ ERRO 1: expressão incompleta }#

print("Após erro");  #{ Esta linha ainda é analisada }#

if (b > a {         #{ ERRO 2: falta parêntese }#
    c = 1;
};

print("Segunda linha válida");  #{ Esta também é analisada }#
```

**Comportamento:**
```
[ERRO SINTÁTICO] Linha 1: Fator inválido...
[ERRO SINTÁTICO] Linha 4: Esperado 'RPAREN'...
```

O parser detecta ambos os erros e permite que as linhas válidas sejam analisadas.

---

## Ferramentas de Depuração

### 1. Visualização de Tokens

**Ativar no `mainInterpret.py`:**
```python
print_tokens = True  #{ Mude para True }#
```

**Saída:**
```
[Tokens gerados pelo lexer]:

[Token(IDENTIFIER, 'x', linha 1),
 Token(ASSIGN, '=', linha 1),
 Token(INTEGER, 10, linha 1),
 Token(SEMICOLON, ';', linha 1),
 Token(EOF, None, linha 1)]
```

**Útil para:**
- Verificar se o lexer está tokenizando corretamente
- Identificar problemas com palavras-chave
- Ver exatamente o que o parser recebe

---

### 2. Visualização da AST

**Ativar no `mainInterpret.py`:**
```python
print_tree = True  #{ Mude para True }#
```

**Exemplo de saída:**
```
[Fluxo da árvore sintática abstrata]:

{
  (ASSIGN x = 10);
  (ASSIGN y = 5);
  (ASSIGN soma = (x PLUS y))
}
```

**Útil para:**
- Entender como o parser interpretou o código
- Verificar precedência de operadores
- Visualizar estrutura de controle de fluxo

---

### 3. Disassembler de Bytecode

**Executar:** `python mainBytecode.py`

**Saída:**
```
--- Bytecode Principal ---
0000    1 OP_LOAD_CONST     0 '10'
0001    1 OP_STORE_GLOBAL   1 'x'
0002   -1 OP_RETURN
--------------------------
```

**Formato:**
- **0000**: Offset da instrução
- **1**: Linha do código fonte
- **OP_LOAD_CONST**: Nome do opcode
- **0**: Argumento
- **'10'**: Valor da constante

**Útil para:**
- Ver como código é compilado
- Entender geração de bytecode
- Depurar problemas de compilação

---

### 4. Mensagens de Erro Detalhadas

Todas as mensagens de erro incluem:
- **Número da linha**: Para localizar rapidamente
- **Tipo de erro**: Léxico, Sintático, Semântico
- **Descrição clara**: Explica o problema
- **Contexto**: Mostra token/valor problemático

**Exemplo:**
```
[ERRO SINTÁTICO] Linha 3: Esperado 'SEMICOLON', mas encontrado 'IDENTIFIER' (token: Token (IDENTIFIER, 'y', linha 3))
```

---

## Boas Práticas para Evitar Erros

### ✓ Sempre termine com ponto e vírgula

```
#{ Correto }#
x = 10;
y = 20;

#{ Errado }#
x = 10
y = 20
```

---

### ✓ Use chaves em blocos

```
#{ Correto }#
if (x > 5) {
    print("Maior");
};

#{ Errado }#
if (x > 5)
    print("Maior");
```

---

### ✓ Inicialize variáveis antes de usar

```
#{ Correto }#
soma = 0;
i = 1;
while (i <= 10) {
    soma = soma + i;
    i = i + 1;
};

#{ Errado }#
while (i <= 10) {  #{ i não foi inicializada! }#
    soma = soma + i;
    i = i + 1;
};
```

---

### ✓ Feche strings e comentários

```
#{ Correto }#
texto = "Olá, Mundo!";
#{ comentário }#

#{ Errado }#
texto = "Olá, Mundo!
#{ comentário
```

---

### ✓ Verifique tipos em operações

```
#{ Correto }#
a = 10;
b = 5;
c = a - b;  #{ Ambos são números }#

#{ Errado }#
a = "texto";
b = 5;
c = a - b;  #{ String - Integer inválido }#
```

---

### ✓ Use break apenas em loops

```
#{ Correto }#
i = 0;
while (i < 10) {
    if (i == 5) {
        break;
    };
    i = i + 1;
};

#{ Errado }#
if (condicao) {
    break;  #{ Não está em loop! }#
};
```

---

### ✓ Balance parênteses e chaves

```
#{ Correto }#
if (x > 5 and y < 10) {
    print("Válido");
};

#{ Errado }#
if (x > 5 and y < 10 {  #{ Falta ) }#
    print("Inválido";   #{ Falta ) }#
;                        #{ Falta } }#
```

---

## Checklist de Depuração

Quando encontrar um erro, siga estes passos:

1. **Leia a mensagem de erro completa**
   - Identifique o tipo de erro
   - Note o número da linha

2. **Localize a linha problemática**
   - Vá até a linha indicada no erro
   - Verifique também linhas anteriores

3. **Verifique sintaxe básica**
   - Ponto e vírgula no final?
   - Parênteses balanceados?
   - Chaves balanceadas?
   - Strings fechadas?

4. **Verifique tipos**
   - Operadores compatíveis com tipos?
   - Variáveis foram inicializadas?

5. **Use ferramentas de depuração**
   - Ative `print_tokens` para ver tokens
   - Ative `print_tree` para ver AST
   - Use `mainBytecode.py` para ver compilação

6. **Isole o problema**
   - Comente partes do código
   - Teste incrementalmente

---

## Exemplos de Depuração

### Problema: Código não executa

**Código:**
```
x = 10
y = 20
print(x + y)
```

**Passos:**
1. Ativar `print_tokens = True`
2. Executar e verificar erro de sintaxe
3. Adicionar `;` faltantes:

```
x = 10;
y = 20;
print(x + y);
```

---

### Problema: Resultado inesperado

**Código:**
```
x = 10;
y = x + z;
print(y);
```

**Passos:**
1. Ler erro: `Variável 'z' não definida`
2. Verificar se `z` foi inicializada
3. Corrigir:

```
x = 10;
z = 5;
y = x + z;
print(y);
```

---

### Problema: Loop não funciona

**Código:**
```
i = 0;
while (i < 5) {
    print(i);
    #{ Esqueceu de incrementar! }#
};
```

**Passos:**
1. Identificar loop infinito
2. Adicionar incremento:

```
i = 0;
while (i < 5) {
    print(i);
    i = i + 1;  #{ Corrigido }#
};
```

---

## Resumo

- **Erros léxicos**: Caracteres ou estruturas inválidas
- **Erros sintáticos**: Gramática incorreta
- **Erros semânticos**: Lógica ou tipos incompatíveis
- **Recuperação**: Parser continua após erros para encontrar mais problemas
- **Ferramentas**: Tokens, AST e bytecode para depuração
- **Boas práticas**: Previnem a maioria dos erros comuns
