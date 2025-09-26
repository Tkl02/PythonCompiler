# Minha Linguagem de Programação Customizada

Bem-vindo à documentação oficial desta linguagem de programação customizada, construída do zero em Python. Este documento detalha a sintaxe, as funcionalidades e o uso da linguagem.

## 1. Funcionalidades

A linguagem suporta uma variedade de construções de programação fundamentais.

### 1.1. Tipos de Dados

A linguagem suporta quatro tipos de dados primitivos:

- **Integer**: Números inteiros (ex: `10`, `-5`).
- **Float**: Números de ponto flutuante (ex: `3.14`, `-0.5`).
- **String**: Uma sequência de caracteres entre aspas duplas (ex: `"Olá, Mundo!"`).
- **Boolean**: Representa valores de verdade, `true` ou `false`.

**Exemplo:**

```
#{
  x = 10;       # Integer
  y = 3.14;     # Float
  z = "teste";  # String
  a = true;     # Boolean
}#
```

### 1.2. Variáveis

Variáveis são usadas para armazenar dados. Elas são declaradas e atribuídas a um valor usando o operador `=`. Todas as declarações devem terminar com um ponto e vírgula `;`.

**Exemplo de implementação:**

```
minha_variavel = 100;
mensagem = "Esta é uma mensagem";
esta_ativo = false;
```

### 1.3. Operadores

#### Operadores Aritméticos

Usados para cálculos matemáticos.

- `+` (Adição)
- `-` (Subtração)
- `*` (Multiplicação)
- `/` (Divisão)

**Exemplo de implementação:**

```
x = 10 + 5;  # x será 15
y = 20 - 10; # y será 10
z = 5 * 2;   # z será 10
w = 10 / 2;  # w será 5.0
```

#### Operadores de Comparação e Lógicos

Usados para comparar valores e combinar expressões booleanas.

- `==` (Igual a)
- `!=` (Diferente de)
- `<` (Menor que)
- `>` (Maior que)
- `<=` (Menor ou igual a)
- `>=` (Maior ou igual a)
- `and` (E lógico)
- `or` (OU lógico)
- `not` (NÃO lógico)

**Exemplo de implementação:**

```
idade = 20;
habilitado = true;

if (idade >= 18 and habilitado == true) {
  print("Pode dirigir");
};
```

### 1.4. Estruturas de Controle

#### `if-else`

Executa um bloco de código se uma condição for verdadeira e, opcionalmente, outro bloco se for falsa. Os blocos de código são definidos por chaves `{}`.

**Exemplo de implementação:**

```
nota = 75;

if (nota >= 60) {
  print("Aprovado");
} else {
  print("Reprovado");
};
```

#### `while`

Executa um bloco de código repetidamente enquanto uma condição for verdadeira.

**Exemplo de implementação:**

```
contador = 0;
while (contador < 5) {
  print(contador);
  contador = contador + 1;
};
```

### 1.5. Funções Nativas

#### `print()`

Exibe o valor de uma expressão no console.

**Exemplo de implementação:**

```
nome = "Mundo";
print("Olá, " + nome + "!"); # Saída: Olá, Mundo!
```

### 1.6. Comentários

Comentários de bloco são usados para adicionar notas ao código que o interpretador irá ignorar. Eles começam com `#{` e terminam com `}#`.

**Exemplo de implementação:**

```
#{
  Este é um comentário de bloco.
  Qualquer texto aqui dentro será ignorado.
  x = 10; # Esta linha não será executada.
}#

print("Isso será executado");
```

## 2. Exemplo Completo

Aqui está um exemplo que combina várias funcionalidades da linguagem:

```
#{
  Este programa calcula a soma dos números de 1 a 10
  e verifica se o resultado é maior que 50.
}#

soma = 0;
contador = 1;

while (contador <= 10) {
  soma = soma + contador;
  contador = contador + 1;
};

print("A soma é: " + soma);

if (soma > 50) {
  print("A soma é maior que 50!");
} else {
  print("A soma não é maior que 50.");
};
```

## 3. Testes

Teste 1: Validação de tipos e operações básicas.

```
print("--- INICIANDO TESTE 1 ---");

a_int = 10;
b_float = 2.5;
c_string = "O valor é ";
d_bool = true;

resultado_float = a_int * b_float;
print(c_string + resultado_float);

resultado_string = c_string * 3;
print(resultado_string);

print("O booleano é " + d_bool);

print("--- FIM DO TESTE 1 ---");
```

Teste 2: Logica Booleana

```
print("--- INICIANDO TESTE 2 ---");

idade = 25;
tem_ingresso = true;
acompanhado_por_responsavel = false;

pode_entrar = tem_ingresso and (idade >= 18 or acompanhado_por_responsavel);

if (not pode_entrar) {
    print("Acesso negado.");
} else {
    print("Acesso permitido!");
};

print("--- FIM DO TESTE 2 ---");
```

Teste 3: Laçoes de repetição

```
print("--- INICIANDO TESTE 3 ---");

contador = 5;
while (contador > 0) {
    print("Contagem regressiva: " + contador);
    contador = contador - 1;
};

print("Lançar!");
print("--- FIM DO TESTE 3 ---");
```

Teste 4: recuperação de erros

```
a = 10 + ;

print("Esta linha não será executada")

if (b > a {
    c = 1;
};

print("Esta linha DEVE ser analisada e executada corretamente, pois vem depois de um ';' que permite a sincronização.");
```

Teste 5: Erro de tipagem

```
print("--- INICIANDO TESTE 5 ---");

a = 100;
b = "texto";

c = a - b;

print("Esta linha não será alcançada.");
```

Teste 2: Erro de operação com variavel vazia

```
print("--- INICIANDO TESTE 6 ---");

a = 10;
b = a + variavel_inexistente;

print("Esta linha não será alcançada.");
```
