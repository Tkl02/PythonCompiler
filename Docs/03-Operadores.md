# Operadores

Os operadores são símbolos que realizam operações sobre valores e variáveis. A linguagem suporta operadores aritméticos, de comparação e lógicos.

## 1. Operadores Aritméticos

Realizam cálculos matemáticos básicos.

### Adição (`+`)

Soma dois números ou concatena strings.

**Sintaxe:**
```
expressão1 + expressão2
```

**Exemplos:**

```
#{ Adição de inteiros }#
a = 10 + 5;
print(a);  #{ Saída: 15 }#

#{ Adição de floats }#
b = 3.14 + 2.86;
print(b);  #{ Saída: 6.0 → convertido para 6 (Integer) }#

#{ Adição mista (Integer + Float) }#
c = 10 + 2.5;
print(c);  #{ Saída: 12.5 }#

#{ Concatenação de strings }#
nome = "João";
sobrenome = "Silva";
completo = nome + " " + sobrenome;
print(completo);  #{ Saída: João Silva }#

#{ String com número }#
mensagem = "Total: " + 100;
print(mensagem);  #{ Saída: Total: 100 }#
```

---

### Subtração (`-`)

Subtrai um número de outro.

**Sintaxe:**
```
expressão1 - expressão2
```

**Exemplos:**

```
#{ Subtração de inteiros }#
a = 20 - 8;
print(a);  #{ Saída: 12 }#

#{ Subtração de floats }#
b = 10.5 - 2.3;
print(b);  #{ Saída: 8.2 }#

#{ Subtração mista }#
c = 15 - 2.5;
print(c);  #{ Saída: 12.5 }#

#{ Resultado negativo }#
d = 5 - 10;
print(d);  #{ Saída: -5 }#
```

**Nota:** Não funciona com strings ou booleanos.

---

### Multiplicação (`*`)

Multiplica dois números ou repete uma string.

**Sintaxe:**
```
expressão1 * expressão2
```

**Exemplos:**

```
#{ Multiplicação de inteiros }#
a = 5 * 4;
print(a);  #{ Saída: 20 }#

#{ Multiplicação de floats }#
b = 2.5 * 4.0;
print(b);  #{ Saída: 10 }#

#{ Multiplicação mista }#
c = 3 * 2.5;
print(c);  #{ Saída: 7.5 }#

#{ Repetição de string }#
linha = "=" * 20;
print(linha);  #{ Saída: ==================== }#

#{ String * Integer }#
palavra = "Oi" * 3;
print(palavra);  #{ Saída: OiOiOi }#
```

---

### Divisão (`/`)

Divide um número por outro.

**Sintaxe:**
```
expressão1 / expressão2
```

**Exemplos:**

```
#{ Divisão exata }#
a = 10 / 2;
print(a);  #{ Saída: 5 }#

#{ Divisão não exata }#
b = 10 / 3;
print(b);  #{ Saída: 3.333333... }#

#{ Divisão de floats }#
c = 7.5 / 2.5;
print(c);  #{ Saída: 3 }#

#{ Divisão por zero (ERRO) }#
d = 10 / 0;  #{ ERRO: ZeroDivisionError: Divisão por zero }#
```

**Comportamento especial:** 
- Se o resultado for um número inteiro exato, retorna Integer
- Caso contrário, retorna Float
- Divisão por zero gera erro

---

### Precedência dos Operadores Aritméticos

A linguagem segue a precedência matemática padrão:

1. **Parênteses** `( )` - maior precedência
2. **Multiplicação e Divisão** `*`, `/`
3. **Adição e Subtração** `+`, `-` - menor precedência

**Exemplos:**

```
#{ Sem parênteses }#
resultado = 10 + 5 * 2;
print(resultado);  #{ Saída: 20 (5*2 = 10, depois 10+10 = 20) }#

#{ Com parênteses }#
resultado2 = (10 + 5) * 2;
print(resultado2);  #{ Saída: 30 (10+5 = 15, depois 15*2 = 30) }#

#{ Expressão complexa }#
resultado3 = 100 / (5 + 5) - 2 * 3;
print(resultado3);  #{ Saída: 4 }#
#{
  Passo a passo:
  1. (5 + 5) = 10
  2. 100 / 10 = 10
  3. 2 * 3 = 6
  4. 10 - 6 = 4
}#
```

---

## 2. Operadores de Comparação

Comparam dois valores e retornam um Boolean (`true` ou `false`).

### Igual (`==`)

Verifica se dois valores são iguais.

**Exemplos:**

```
a = 10 == 10;
print(a);  #{ Saída: true }#

b = 5 == 3;
print(b);  #{ Saída: false }#

c = "texto" == "texto";
print(c);  #{ Saída: true }#

d = true == true;
print(d);  #{ Saída: true }#

#{ Comparação entre tipos diferentes }#
e = 10 == 10.0;
print(e);  #{ Saída: true (valores são iguais) }#
```

---

### Diferente (`!=`)

Verifica se dois valores são diferentes.

**Exemplos:**

```
a = 10 != 5;
print(a);  #{ Saída: true }#

b = "abc" != "abc";
print(b);  #{ Saída: false }#

c = true != false;
print(c);  #{ Saída: true }#
```

---

### Menor que (`<`)

Verifica se o primeiro valor é menor que o segundo.

**Exemplos:**

```
a = 5 < 10;
print(a);  #{ Saída: true }#

b = 10 < 5;
print(b);  #{ Saída: false }#

#{ Comparação de strings (ordem lexicográfica) }#
c = "abc" < "xyz";
print(c);  #{ Saída: true }#

#{ Comparação de floats }#
d = 3.14 < 3.15;
print(d);  #{ Saída: true }#
```

---

### Maior que (`>`)

Verifica se o primeiro valor é maior que o segundo.

**Exemplos:**

```
a = 10 > 5;
print(a);  #{ Saída: true }#

b = 3 > 8;
print(b);  #{ Saída: false }#

c = "zebra" > "apple";
print(c);  #{ Saída: true }#
```

---

### Menor ou igual (`<=`)

Verifica se o primeiro valor é menor ou igual ao segundo.

**Exemplos:**

```
a = 5 <= 10;
print(a);  #{ Saída: true }#

b = 10 <= 10;
print(b);  #{ Saída: true }#

c = 15 <= 10;
print(c);  #{ Saída: false }#
```

---

### Maior ou igual (`>=`)

Verifica se o primeiro valor é maior ou igual ao segundo.

**Exemplos:**

```
a = 10 >= 5;
print(a);  #{ Saída: true }#

b = 10 >= 10;
print(b);  #{ Saída: true }#

c = 5 >= 10;
print(c);  #{ Saída: false }#
```

---

### Regras de Comparação

**Tipos compatíveis:**
- Integer com Integer ✓
- Float com Float ✓
- Integer com Float ✓
- String com String ✓
- Boolean com Boolean ✓

**Comparação entre tipos incompatíveis:**

```
#{ ERRO: Não é possível comparar tipos diferentes (exceto Int/Float) }#
resultado = "texto" < 10;  #{ ERRO }#
resultado2 = true > 5;     #{ ERRO }#
```

---

## 3. Operadores Lógicos

Operam sobre valores booleanos e retornam Boolean.

### AND (`and`)

Retorna `true` apenas se ambos os operandos forem `true`.

**Tabela verdade:**
| A     | B     | A and B |
|-------|-------|---------|
| true  | true  | true    |
| true  | false | false   |
| false | true  | false   |
| false | false | false   |

**Exemplos:**

```
#{ Ambos verdadeiros }#
a = true and true;
print(a);  #{ Saída: true }#

#{ Um falso }#
b = true and false;
print(b);  #{ Saída: false }#

#{ Ambos falsos }#
c = false and false;
print(c);  #{ Saída: false }#

#{ Com expressões }#
idade = 25;
tem_carteira = true;

pode_dirigir = (idade >= 18) and tem_carteira;
print(pode_dirigir);  #{ Saída: true }#
```

---

### OR (`or`)

Retorna `true` se pelo menos um dos operandos for `true`.

**Tabela verdade:**
| A     | B     | A or B |
|-------|-------|--------|
| true  | true  | true   |
| true  | false | true   |
| false | true  | true   |
| false | false | false  |

**Exemplos:**

```
#{ Ambos verdadeiros }#
a = true or true;
print(a);  #{ Saída: true }#

#{ Um verdadeiro }#
b = true or false;
print(b);  #{ Saída: true }#

#{ Ambos falsos }#
c = false or false;
print(c);  #{ Saída: false }#

#{ Com expressões }#
fim_de_semana = false;
feriado = true;

folga = fim_de_semana or feriado;
print(folga);  #{ Saída: true }#
```

---

### NOT (`not`)

Inverte o valor booleano.

**Tabela verdade:**
| A     | not A |
|-------|-------|
| true  | false |
| false | true  |

**Exemplos:**

```
a = not true;
print(a);  #{ Saída: false }#

b = not false;
print(b);  #{ Saída: true }#

#{ Dupla negação }#
c = not not true;
print(c);  #{ Saída: true }#

#{ Com expressões }#
chovendo = false;
sair = not chovendo;
print(sair);  #{ Saída: true }#
```

---

### Combinação de Operadores Lógicos

**Precedência:**
1. `not` (maior precedência)
2. `and`
3. `or` (menor precedência)

**Exemplos:**

```
#{ Sem parênteses }#
resultado = true or false and false;
print(resultado);  #{ Saída: true }#
#{
  Passo a passo:
  1. false and false = false
  2. true or false = true
}#

#{ Com parênteses }#
resultado2 = (true or false) and false;
print(resultado2);  #{ Saída: false }#
#{
  Passo a passo:
  1. (true or false) = true
  2. true and false = false
}#

#{ Negação com precedência }#
resultado3 = not true and false;
print(resultado3);  #{ Saída: false }#
#{
  Passo a passo:
  1. not true = false
  2. false and false = false
}#
```

---

## 4. Operadores Unários

Operam sobre um único operando.

### Negação Numérica (`-`)

Inverte o sinal de um número.

**Exemplos:**

```
a = -10;
print(a);  #{ Saída: -10 }#

b = -(-5);
print(b);  #{ Saída: 5 }#

c = -(3 + 2);
print(c);  #{ Saída: -5 }#

x = 15;
y = -x;
print(y);  #{ Saída: -15 }#
```

### Positivo (`+`)

Mantém o sinal do número (operação identidade).

**Exemplos:**

```
a = +10;
print(a);  #{ Saída: 10 }#

b = +(5);
print(b);  #{ Saída: 5 }#
```

---

## 5. Precedência Geral de Operadores

Da **maior** para a **menor** precedência:

1. **Parênteses** `( )`
2. **Operadores Unários** `-`, `+`, `not`
3. **Multiplicação e Divisão** `*`, `/`
4. **Adição e Subtração** `+`, `-`
5. **Comparação** `<`, `>`, `<=`, `>=`
6. **Igualdade** `==`, `!=`
7. **AND lógico** `and`
8. **OR lógico** `or`

**Exemplo complexo:**

```
resultado = 5 + 3 * 2 > 10 and not false or 1 == 1;
print(resultado);  #{ Saída: true }#

#{
  Passo a passo:
  1. 3 * 2 = 6
  2. 5 + 6 = 11
  3. 11 > 10 = true
  4. not false = true
  5. true and true = true
  6. 1 == 1 = true
  7. true or true = true
}#
```

---

## 6. Exemplos Práticos Combinados

### Cálculo de Média com Validação

```
nota1 = 8.5;
nota2 = 7.0;
nota3 = 9.5;

media = (nota1 + nota2 + nota3) / 3;
print("Média: " + media);  #{ Saída: Média: 8.333333... }#

aprovado = media >= 7.0;
print("Aprovado: " + aprovado);  #{ Saída: Aprovado: true }#
```

### Verificação de Condições Múltiplas

```
idade = 20;
tem_ingresso = true;
acompanhado = false;

pode_entrar = tem_ingresso and (idade >= 18 or acompanhado);
print(pode_entrar);  #{ Saída: true }#

#{
  Lógica:
  - Precisa de ingresso E
  - (Ser maior de 18 OU estar acompanhado)
}#
```

### Calculadora de Desconto

```
preco = 100.0;
tem_cupom = true;
cliente_vip = false;

desconto_cupom = 10.0;
desconto_vip = 15.0;

desconto_final = 0.0;

if (tem_cupom and not cliente_vip) {
    desconto_final = desconto_cupom;
};

if (cliente_vip) {
    desconto_final = desconto_vip;
};

preco_final = preco - desconto_final;
print("Preço final: " + preco_final);  #{ Saída: Preço final: 90.0 }#
```

### Expressões Complexas

```
#{ Verificação de intervalo }#
numero = 50;
no_intervalo = (numero >= 10) and (numero <= 100);
print(no_intervalo);  #{ Saída: true }#

#{ Validação de senha (lógica simplificada) }#
tamanho = 8;
tem_letra = true;
tem_numero = true;

senha_valida = (tamanho >= 8) and tem_letra and tem_numero;
print("Senha válida: " + senha_valida);  #{ Saída: Senha válida: true }#

#{ Cálculo com múltiplos operadores }#
base = 10;
altura = 5;
area_triangulo = (base * altura) / 2;
print("Área: " + area_triangulo);  #{ Saída: Área: 25 }#
```

---

## 7. Erros Comuns

### Erro 1: Tipo incompatível em operação
```
texto = "abc";
resultado = texto - 5;  #{ ERRO: Operador '-' inválido para String }#
```

### Erro 2: Operador lógico em não-booleano
```
a = 10;
b = 5;
resultado = a and b;  #{ ERRO: 'and' só funciona com Boolean }#
```

### Erro 3: Divisão por zero
```
x = 10 / 0;  #{ ERRO: ZeroDivisionError: Divisão por zero }#
```

### Erro 4: Comparação de tipos incompatíveis
```
resultado = "texto" < 10;  #{ ERRO: Não é possível comparar String com Integer }#
```
