# Tipos de Dados

A linguagem suporta quatro tipos de dados primitivos. O sistema de tipos é dinâmico, ou seja, o tipo de uma variável é determinado em tempo de execução baseado no valor atribuído.

## 1. Integer (Inteiro)

Representa números inteiros sem parte decimal.

### Sintaxe
```
42
-10
0
1000
```

### Exemplos Práticos

```
idade = 25;
quantidade = 100;
temperatura = -5;

print(idade);        #{ Saída: 25 }#
print(quantidade);   #{ Saída: 100 }#
print(temperatura);  #{ Saída: -5 }#
```

### Operações Suportadas

- **Aritméticas**: `+`, `-`, `*`, `/`
- **Comparação**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Conversão**: Operações com Float retornam Float quando necessário

### Comportamento Especial

```
a = 10;
b = 5;

c = a / b;        #{ c = 2 (Integer, pois divisão exata) }#

d = 10;
e = 3;

f = d / e;        #{ f = 3.333... (Float, pois divisão não exata) }#
```

---

## 2. Float (Ponto Flutuante)

Representa números com parte decimal.

### Sintaxe
```
3.14
-0.5
2.0
100.999
```

### Exemplos Práticos

```
pi = 3.14159;
preco = 19.99;
negativo = -2.5;

print(pi);      #{ Saída: 3.14159 }#
print(preco);   #{ Saída: 19.99 }#
```

### Operações Suportadas

- **Aritméticas**: `+`, `-`, `*`, `/`
- **Comparação**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Conversão automática**: Operações entre Integer e Float resultam em Float quando apropriado

### Comportamento com Inteiros

```
a = 10;      #{ Integer }#
b = 2.5;     #{ Float }#

c = a * b;   #{ c = 25.0 (convertido para Float) }#
d = a + b;   #{ d = 12.5 (Float) }#

e = 5.0;
f = 2.0;
g = e / f;   #{ g = 2 (Integer, pois resultado é inteiro) }#
```

**Regra de conversão**: O resultado é Float apenas se necessário. Se o resultado final for um número inteiro exato (sem parte decimal), retorna Integer.

---

## 3. String (Cadeia de Caracteres)

Representa texto. Strings são delimitadas por aspas duplas (`"`).

### Sintaxe
```
"Olá, Mundo!"
"Python"
"123"
""
"Linha com espaços     aqui"
```

### Exemplos Práticos

```
nome = "João";
sobrenome = "Silva";
mensagem = "Bem-vindo!";
vazio = "";

print(nome);      #{ Saída: João }#
print(mensagem);  #{ Saída: Bem-vindo! }#
```

### Operações Suportadas

#### Concatenação (`+`)
Combina strings ou adiciona outros tipos ao final:

```
primeiro = "Olá";
segundo = "Mundo";

resultado = primeiro + " " + segundo;
print(resultado);  #{ Saída: Olá Mundo }#

#{ Concatenação com números }#
idade = 30;
frase = "Eu tenho " + idade + " anos";
print(frase);  #{ Saída: Eu tenho 30 anos }#

#{ Concatenação com booleanos }#
ativo = true;
status = "Status: " + ativo;
print(status);  #{ Saída: Status: true }#
```

#### Multiplicação (`*`)
Repete a string N vezes (apenas com Integer):

```
linha = "-";
separador = linha * 20;
print(separador);  #{ Saída: -------------------- }#

palavra = "Ha";
risada = palavra * 3;
print(risada);  #{ Saída: HaHaHa }#

numero = 3;
texto = "Oi" * numero;
print(texto);  #{ Saída: OiOiOi }#
```

### Operações NÃO Suportadas

```
texto = "Olá";
resultado = texto - "l";   #{ ERRO: Operador '-' inválido para String }#
resultado2 = texto / 2;    #{ ERRO: Operador '/' inválido para String }#
```

### Comparação

```
a = "abc";
b = "abc";
c = "xyz";

print(a == b);  #{ Saída: true }#
print(a == c);  #{ Saída: false }#
print(a != c);  #{ Saída: true }#

#{ Comparação lexicográfica }#
print("abc" < "xyz");  #{ Saída: true }#
print("zebra" > "apple");  #{ Saída: true }#
```

---

## 4. Boolean (Booleano)

Representa valores lógicos de verdadeiro ou falso.

### Sintaxe
```
true
false
```

**Nota**: Os valores são escritos em minúsculas (`true` e `false`).

### Exemplos Práticos

```
esta_ativo = true;
tem_permissao = false;
maior_idade = true;

print(esta_ativo);     #{ Saída: true }#
print(tem_permissao);  #{ Saída: false }#
```

### Operações Lógicas

#### AND (E lógico)
```
a = true;
b = false;

resultado1 = a and a;  #{ true }#
resultado2 = a and b;  #{ false }#
resultado3 = b and b;  #{ false }#

print(resultado1);     #{ Saída: true }#
print(resultado2);     #{ Saída: false }#
```

#### OR (OU lógico)
```
a = true;
b = false;

resultado1 = a or b;   #{ true }#
resultado2 = b or b;   #{ false }#
resultado3 = a or a;   #{ true }#

print(resultado1);     #{ Saída: true }#
```

#### NOT (NÃO lógico)
```
a = true;
b = false;

resultado1 = not a;    #{ false }#
resultado2 = not b;    #{ true }#

print(resultado1);     #{ Saída: false }#
print(resultado2);     #{ Saída: true }#
```

### Comparações Produzem Booleanos

```
x = 10;
y = 20;

maior = x > y;         #{ false }#
menor = x < y;         #{ true }#
igual = x == 10;       #{ true }#

print(maior);          #{ Saída: false }#
print(menor);          #{ Saída: true }#
```

### Operações NÃO Suportadas

Booleanos não suportam operações aritméticas:

```
a = true;
b = false;

resultado = a + b;     #{ ERRO: Operador '+' inválido para Boolean }#
resultado2 = a * 5;    #{ ERRO: Operador '*' inválido para Boolean }#
resultado3 = a - b;    #{ ERRO: Operador '-' inválido para Boolean }#
```

---

## Conversão de Tipos

A linguagem realiza algumas conversões automáticas em contextos específicos:

### Em Operações Aritméticas

```
a = 10;       #{ Integer }#
b = 2.5;      #{ Float }#

c = a + b;    #{ 12.5 (Float) }#
d = a * b;    #{ 25.0 (Float - mas pode ser convertido para Integer se exato) }#
```

### Em Concatenação de Strings

Todos os tipos podem ser convertidos para string em operações de concatenação:

```
numero = 42;
decimal = 3.14;
verdade = true;

texto1 = "Número: " + numero;      #{ "Número: 42" }#
texto2 = "PI: " + decimal;         #{ "PI: 3.14" }#
texto3 = "Ativo: " + verdade;      #{ "Ativo: true" }#

print(texto1);
print(texto2);
print(texto3);
```

### Em Condições Booleanas

Em estruturas `if` e `while`, apenas valores Boolean são aceitos:

```
x = 10;

#{ Correto: comparação retorna Boolean }#
if (x > 5) {
    print("Maior que 5");
};

#{ ERRO: x não é um Boolean }#
if (x) {
    print("Isso causará erro");
};
```

---

## Resumo de Operações por Tipo

| Tipo    | `+`              | `-`     | `*`              | `/`     | Comparação | Lógicos     |
|---------|------------------|---------|------------------|---------|------------|-------------|
| Integer | ✓ (com Int/Float)| ✓ (com Int/Float) | ✓ (com Int/Float/String*) | ✓ (com Int/Float) | ✓          | ✗           |
| Float   | ✓ (com Int/Float)| ✓ (com Int/Float) | ✓ (com Int/Float) | ✓ (com Int/Float) | ✓          | ✗           |
| String  | ✓ (concatena)    | ✗       | ✓ (com Integer)  | ✗       | ✓          | ✗           |
| Boolean | ✗                | ✗       | ✗                | ✗       | ✓          | ✓ (and/or/not) |

**String***: Integer * String ou String * Integer resulta em repetição da string.

---

## Exemplo Completo: Todos os Tipos

```
#{ Demonstração de todos os tipos de dados }#

#{ Integers }#
idade = 25;
ano = 2024;

#{ Floats }#
altura = 1.75;
pi = 3.14159;

#{ Strings }#
nome = "Maria";
saudacao = "Olá, " + nome + "!";

#{ Booleans }#
ativo = true;
bloqueado = false;

#{ Operações mistas }#
info = nome + " tem " + idade + " anos";
area_circulo = pi * 5 * 5;
permitido = ativo and not bloqueado;

#{ Saída }#
print(info);              #{ Saída: Maria tem 25 anos }#
print(area_circulo);      #{ Saída: 78.53975 }#
print(permitido);         #{ Saída: true }#

#{ Comparações }#
maior_idade = idade >= 18;
print(maior_idade);       #{ Saída: true }#
```
