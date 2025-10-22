# Variáveis

Variáveis são espaços de memória nomeados que armazenam valores durante a execução do programa. A linguagem utiliza tipagem dinâmica, onde o tipo da variável é determinado pelo valor atribuído.

## 1. Declaração e Atribuição

### Sintaxe Básica

```
nome_variavel = valor;
```

**Elementos:**
- **nome_variavel**: identificador único da variável
- **`=`**: operador de atribuição
- **valor**: expressão que será armazenada
- **`;`**: ponto e vírgula obrigatório no final

### Exemplos Simples

```
idade = 25;
nome = "João";
altura = 1.75;
ativo = true;
```

**Importante:** Não há palavra-chave especial (como `var` ou `let`) para declarar variáveis. A simples atribuição cria a variável.

---

## 2. Regras para Nomes de Variáveis

### Caracteres Permitidos

- **Letras**: a-z, A-Z
- **Números**: 0-9 (não pode começar com número)
- **Underscore**: `_`

### Válidos ✓

```
usuario = "admin";
nome_completo = "Maria Silva";
idade1 = 30;
_privado = 100;
contador_de_tentativas = 0;
valorTotal = 150;
PI = 3.14159;
```

### Inválidos ✗

```
1usuario = "erro";        #{ Não pode começar com número }#
nome-completo = "erro";   #{ Hífen não é permitido }#
meu valor = 10;           #{ Espaços não são permitidos }#
@variavel = 5;            #{ Símbolos especiais não permitidos }#
```

### Palavras Reservadas

Estas palavras **não podem** ser usadas como nomes de variáveis:

```
if, else, while, print, true, false, and, or, not, break
```

**Erro:**
```
if = 10;       #{ ERRO: 'if' é palavra reservada }#
while = "x";   #{ ERRO: 'while' é palavra reservada }#
```

---

## 3. Convenções de Nomenclatura

### Snake Case (Recomendado)

Use underscores para separar palavras:

```
idade_usuario = 25;
nome_completo = "Ana Silva";
total_de_vendas = 1000;
preco_com_desconto = 89.90;
```

### Camel Case (Alternativa)

Capitalize a primeira letra de cada palavra (exceto a primeira):

```
idadeUsuario = 25;
nomeCompleto = "Ana Silva";
totalDeVendas = 1000;
precoComDesconto = 89.90;
```

### Nomes Descritivos

```
#{ Bom: nomes claros }#
quantidade_alunos = 30;
temperatura_media = 25.5;
usuario_autenticado = true;

#{ Evite: nomes genéricos }#
x = 30;
temp = 25.5;
flag = true;
```

---

## 4. Tipos Dinâmicos

O tipo da variável é determinado pelo valor atribuído e pode mudar durante a execução.

### Atribuição Inicial

```
x = 10;         #{ x é Integer }#
x = "texto";    #{ Agora x é String }#
x = 3.14;       #{ Agora x é Float }#
x = true;       #{ Agora x é Boolean }#
```

### Tipo Determinado pelo Valor

```
#{ Integer }#
contador = 0;
ano = 2024;

#{ Float }#
preco = 19.99;
temperatura = -5.5;

#{ String }#
nome = "Pedro";
mensagem = "Olá!";

#{ Boolean }#
ativo = true;
concluido = false;
```

---

## 5. Atribuição e Reatribuição

### Primeira Atribuição (Declaração)

```
x = 10;
print(x);  #{ Saída: 10 }#
```

### Reatribuição (Modificação)

```
x = 10;
print(x);  #{ Saída: 10 }#

x = 20;
print(x);  #{ Saída: 20 }#

x = x + 5;
print(x);  #{ Saída: 25 }#
```

### Atribuição com Expressões

```
a = 5;
b = 10;

#{ Expressão aritmética }#
soma = a + b;
print(soma);  #{ Saída: 15 }#

#{ Expressão com a própria variável }#
soma = soma * 2;
print(soma);  #{ Saída: 30 }#

#{ Expressão booleana }#
maior = a > b;
print(maior);  #{ Saída: false }#
```

---

## 6. Escopo de Variáveis

Todas as variáveis na linguagem são **globais**. Não há escopo local (como em funções ou blocos).

### Variáveis em Blocos

```
x = 10;

if (x > 5) {
    y = 20;      #{ y é criada dentro do if }#
    x = x + 1;   #{ x é modificada }#
};

print(x);  #{ Saída: 11 (x foi modificada) }#
print(y);  #{ Saída: 20 (y existe fora do bloco) }#
```

### Variáveis em Loops

```
i = 0;

while (i < 3) {
    valor = i * 2;
    i = i + 1;
};

print(i);      #{ Saída: 3 }#
print(valor);  #{ Saída: 4 (último valor atribuído) }#
```

---

## 7. Uso de Variáveis Não Declaradas

Acessar uma variável antes de atribuir um valor resulta em **erro**.

### Erro de Variável Não Definida

```
print(x);  #{ ERRO: Variável 'x' não definida }#

x = 10;
print(x);  #{ Agora funciona: Saída: 10 }#
```

### Exemplo de Erro

```
a = 10;
b = a + c;  #{ ERRO: Variável 'c' não definida }#
```

**Sempre inicialize variáveis antes de usá-las:**

```
a = 10;
c = 5;      #{ Inicializa c }#
b = a + c;  #{ Agora funciona }#
print(b);   #{ Saída: 15 }#
```

---

## 8. Operações com Variáveis

### Aritméticas

```
a = 10;
b = 5;

soma = a + b;          #{ 15 }#
subtracao = a - b;     #{ 5 }#
multiplicacao = a * b; #{ 50 }#
divisao = a / b;       #{ 2 }#

print(soma);           #{ Saída: 15 }#
```

### Incremento e Decremento

A linguagem não possui `++` ou `--`, use:

```
contador = 0;

#{ Incremento }#
contador = contador + 1;
print(contador);  #{ Saída: 1 }#

#{ Decremento }#
contador = contador - 1;
print(contador);  #{ Saída: 0 }#

#{ Incremento por valor }#
contador = contador + 5;
print(contador);  #{ Saída: 5 }#
```

### Acumulação

```
total = 0;

total = total + 10;
total = total + 20;
total = total + 30;

print(total);  #{ Saída: 60 }#
```

### Comparação

```
x = 10;
y = 20;

igual = x == y;        #{ false }#
diferente = x != y;    #{ true }#
menor = x < y;         #{ true }#
maior = x > y;         #{ false }#

print(menor);          #{ Saída: true }#
```

### Lógicas

```
a = true;
b = false;

resultado_and = a and b;  #{ false }#
resultado_or = a or b;    #{ true }#
resultado_not = not a;    #{ false }#

print(resultado_or);      #{ Saída: true }#
```

---

## 9. Strings em Variáveis

### Concatenação

```
primeiro_nome = "João";
sobrenome = "Silva";

nome_completo = primeiro_nome + " " + sobrenome;
print(nome_completo);  #{ Saída: João Silva }#
```

### Concatenação com Outros Tipos

```
nome = "Ana";
idade = 25;

mensagem = nome + " tem " + idade + " anos";
print(mensagem);  #{ Saída: Ana tem 25 anos }#
```

### Repetição

```
char = "-";
linha = char * 20;
print(linha);  #{ Saída: -------------------- }#
```

---

## 10. Variáveis em Estruturas de Controle

### Em Condições

```
idade = 17;
tem_permissao = false;

if (idade >= 18) {
    pode_entrar = true;
} else {
    pode_entrar = false;
};

if (pode_entrar or tem_permissao) {
    print("Entrada permitida");
} else {
    print("Entrada negada");
};

#{ Saída: Entrada negada }#
```

### Em Loops

```
soma = 0;
i = 1;

while (i <= 5) {
    soma = soma + i;
    i = i + 1;
};

print("Soma: " + soma);  #{ Saída: Soma: 15 }#
```

---

## 11. Variáveis de Controle (Flags)

Variáveis booleanas usadas para controlar o fluxo do programa.

### Flag Simples

```
encontrado = false;
i = 0;

while (i < 10) {
    if (i == 5) {
        encontrado = true;
        break;
    };
    i = i + 1;
};

if (encontrado) {
    print("Número encontrado!");
} else {
    print("Número não encontrado");
};

#{ Saída: Número encontrado! }#
```

### Múltiplas Flags

```
autenticado = false;
admin = false;

usuario = "root";
senha = "1234";

if (usuario == "root" and senha == "1234") {
    autenticado = true;
    admin = true;
};

if (autenticado and admin) {
    print("Acesso total concedido");
} else if (autenticado) {
    print("Acesso básico concedido");
} else {
    print("Acesso negado");
};

#{ Saída: Acesso total concedido }#
```

---

## 12. Variáveis Temporárias

Use variáveis temporárias para armazenar resultados intermediários.

### Cálculos Complexos

```
a = 10;
b = 5;
c = 3;

#{ Sem temporárias (difícil de ler) }#
resultado = ((a + b) * c) / 2;

#{ Com temporárias (mais claro) }#
soma = a + b;
produto = soma * c;
resultado = produto / 2;

print(resultado);  #{ Saída: 22.5 }#
```

### Troca de Valores

```
#{ Não há suporte direto para swap, use variável temporária }#
a = 10;
b = 20;

temp = a;
a = b;
b = temp;

print("a = " + a);  #{ Saída: a = 20 }#
print("b = " + b);  #{ Saída: b = 10 }#
```

---

## 13. Exemplos Práticos

### Calculadora Simples

```
numero1 = 15;
numero2 = 4;
operacao = "+";

resultado = 0;

if (operacao == "+") {
    resultado = numero1 + numero2;
} else if (operacao == "-") {
    resultado = numero1 - numero2;
} else if (operacao == "*") {
    resultado = numero1 * numero2;
} else if (operacao == "/") {
    resultado = numero1 / numero2;
};

print("Resultado: " + resultado);
#{ Saída: Resultado: 19 }#
```

### Contador de Pares e Ímpares

```
inicio = 1;
fim = 10;
pares = 0;
impares = 0;

i = inicio;

while (i <= fim) {
    resto = i - (i / 2) * 2;  #{ Simulação de módulo }#
    
    if (resto == 0) {
        pares = pares + 1;
    } else {
        impares = impares + 1;
    };
    
    i = i + 1;
};

print("Números pares: " + pares);      #{ Saída: Números pares: 5 }#
print("Números ímpares: " + impares);  #{ Saída: Números ímpares: 5 }#
```

### Sistema de Pontuação

```
pontos = 0;
nivel = 1;

#{ Ação 1: ganhou 100 pontos }#
pontos = pontos + 100;

#{ Ação 2: ganhou 50 pontos }#
pontos = pontos + 50;

#{ Verificação de nível }#
if (pontos >= 100 and pontos < 200) {
    nivel = 2;
} else if (pontos >= 200) {
    nivel = 3;
};

print("Pontos: " + pontos);  #{ Saída: Pontos: 150 }#
print("Nível: " + nivel);    #{ Saída: Nível: 2 }#
```

### Conversão de Temperatura

```
celsius = 25;
fahrenheit = 0;

#{ Fórmula: F = C * 9/5 + 32 }#
fahrenheit = celsius * 9 / 5 + 32;

print(celsius + "°C = " + fahrenheit + "°F");
#{ Saída: 25°C = 77°F }#
```

---

## 14. Boas Práticas

### ✓ Nomes Descritivos

```
#{ Bom }#
idade_usuario = 25;
preco_total = 150.50;
quantidade_itens = 10;

#{ Evite }#
x = 25;
p = 150.50;
q = 10;
```

### ✓ Inicialize Antes de Usar

```
#{ Correto }#
contador = 0;
soma = 0;

while (contador < 5) {
    soma = soma + contador;
    contador = contador + 1;
};

#{ Erro: 'soma' não inicializada }#
while (contador < 5) {
    soma = soma + contador;  #{ ERRO! }#
    contador = contador + 1;
};
```

### ✓ Use Constantes com Nomes em Maiúsculas

Embora a linguagem não tenha constantes reais, use convenção:

```
PI = 3.14159;
MAX_TENTATIVAS = 3;
TAXA_JUROS = 0.05;

area = PI * raio * raio;
```

### ✓ Agrupe Variáveis Relacionadas

```
#{ Dados do usuário }#
usuario_nome = "João";
usuario_idade = 30;
usuario_email = "joao@email.com";

#{ Configurações }#
max_tentativas = 3;
timeout = 30;
debug_mode = false;
```

### ✗ Evite Reutilizar Variáveis para Propósitos Diferentes

```
#{ Evite }#
temp = idade * 2;
print(temp);

temp = "Nome: " + nome;  #{ Reutilização confusa }#
print(temp);

#{ Melhor }#
idade_dobrada = idade * 2;
print(idade_dobrada);

mensagem_nome = "Nome: " + nome;
print(mensagem_nome);
```
