# Referência Rápida (Cheat Sheet)

Guia de consulta rápida com a sintaxe e recursos da linguagem.

---

## 📋 Sintaxe Básica

### Declaração de Variável
```
identificador = valor;
```

### Regras de Nomenclatura
- Inicia com letra ou `_`
- Contém letras, números e `_`
- Case-sensitive
- Não use palavras reservadas

**Palavras reservadas:**
`if`, `else`, `while`, `print`, `true`, `false`, `and`, `or`, `not`, `break`

---

## 🔢 Tipos de Dados

| Tipo    | Exemplo           | Descrição                |
|---------|-------------------|--------------------------|
| Integer | `42`, `-10`, `0`  | Números inteiros         |
| Float   | `3.14`, `-0.5`    | Ponto flutuante          |
| String  | `"Olá"`, `""`     | Texto entre aspas duplas |
| Boolean | `true`, `false`   | Valores lógicos          |

---

## ➕ Operadores

### Aritméticos
```
+   # Adição / Concatenação
-   # Subtração
*   # Multiplicação / Repetição de string
/   # Divisão
```

### Atribuição Composta
```
++  # Auto-incremento (var = var + 1)
+=  # Adição com atribuição (var = var + valor)
-=  # Subtração com atribuição (var = var - valor)
```

### Comparação
```
==  # Igual
!=  # Diferente
<   # Menor que
>   # Maior que
<=  # Menor ou igual
>=  # Maior ou igual
```

### Lógicos
```
and  # E lógico (também pode usar &&)
or   # OU lógico (também pode usar ||)
not  # NÃO lógico
&&   # E lógico (alternativa a and)
||   # OU lógico (alternativa a or)
```

### Unários
```
-   # Negação numérica
+   # Identidade
not # Negação lógica
```

---

## 📊 Precedência (maior → menor)

1. `( )`
2. `-`, `+`, `not` (unários)
3. `*`, `/`
4. `+`, `-`
5. `<`, `>`, `<=`, `>=`
6. `==`, `!=`
7. `and`, `&&`
8. `or`, `||`

---

## 🔀 Estruturas de Controle

### If-Else
```
if (condição) {
    # código
};

if (condição) {
    # código
} else {
    # código
};

if (condição1) {
    # código
} else if (condição2) {
    # código
} else {
    # código
};
```

### While
```
while (condição) {
    # código
};
```

### Break
```
while (condição) {
    if (condição_saída) {
        break;
    };
};
```

---

## 🖨️ Saída

### Print
```
print(expressão);
```

**Exemplos:**
```
print("Texto");
print(42);
print(x + y);
print("Resultado: " + resultado);
```

---

## 💬 Comentários

### Bloco
```
#{
  Comentário
  em múltiplas linhas
}#
```

---

## 📝 Exemplos Comuns

### Atribuição
```
x = 10;
nome = "João";
ativo = true;
```

### Operações
```
soma = a + b;
produto = a * b;
divisao = a / b;
mensagem = "Valor: " + x;
```

### Comparações
```
maior = x > y;
igual = a == b;
diferente = c != d;
```

### Lógica
```
resultado = a and b;
ou_logico = a or b;
negacao = not a;
```

### Loop Simples
```
i = 0;
while (i < 10) {
    print(i);
    i = i + 1;
};
```

### Acumulador
```
soma = 0;
i = 1;
while (i <= 100) {
    soma = soma + i;
    i = i + 1;
};
```

### Contador
```
contador = 0;
while (contador < 5) {
    print("Iteração: " + contador);
    contador = contador + 1;
};
```

---

## ⚠️ Erros Comuns

### Falta de ponto e vírgula
```
❌ x = 10
✅ x = 10;
```

### Falta de chaves
```
❌ if (x > 5)
     print("Maior");

✅ if (x > 5) {
     print("Maior");
   };
```

### Variável não inicializada
```
❌ y = x + z;  # z não existe

✅ z = 5;
   y = x + z;
```

### Tipos incompatíveis
```
❌ resultado = "texto" - 5;

✅ resultado = "texto" + 5;  # Concatenação
```

### Break fora de loop
```
❌ if (x > 5) {
     break;
   };

✅ while (x > 0) {
     if (x == 5) {
       break;
     };
     x = x - 1;
   };
```

---

## 🎯 Padrões Úteis

### Incremento/Decremento
```
contador = contador + 1;  # Incremento
contador = contador - 1;  # Decremento
contador = contador + 5;  # Incremento por N
```

### Troca de Valores
```
temp = a;
a = b;
b = temp;
```

### Flag Booleana
```
encontrado = false;
while (i < max and not encontrado) {
    if (i == procurado) {
        encontrado = true;
    };
    i = i + 1;
};
```

### Contador Condicional
```
pares = 0;
i = 1;
while (i <= 100) {
    resto = i - (i / 2) * 2;
    if (resto == 0) {
        pares = pares + 1;
    };
    i = i + 1;
};
```

### Busca com Break
```
i = 0;
while (i < tamanho) {
    if (lista_i == procurado) {
        print("Encontrado na posição " + i);
        break;
    };
    i = i + 1;
};
```

---

## 🔧 Conversões de Tipo

### Automáticas em Aritmética
```
int + int   → int
int + float → float (ou int se resultado exato)
float + float → float (ou int se resultado exato)
```

### Automáticas em Concatenação
```
string + int     → string
string + float   → string
string + boolean → string
```

### Repetição de String
```
string * int → string
int * string → string
```

---

## 📐 Fórmulas Úteis

### Média
```
media = (a + b + c) / 3;
```

### Área do Círculo
```
PI = 3.14159;
area = PI * raio * raio;
```

### Celsius → Fahrenheit
```
fahrenheit = celsius * 9 / 5 + 32;
```

### Fahrenheit → Celsius
```
celsius = (fahrenheit - 32) * 5 / 9;
```

### Porcentagem
```
percentual = (parte * 100) / total;
```

### Desconto
```
preco_final = preco - (preco * desconto / 100);
```

---

## 🏃 Algoritmos Clássicos

### Fatorial
```
n = 5;
fat = 1;
i = 1;
while (i <= n) {
    fat = fat * i;
    i = i + 1;
};
```

### Fibonacci
```
n = 10;
a = 0;
b = 1;
i = 1;
while (i <= n) {
    print(a);
    temp = a + b;
    a = b;
    b = temp;
    i = i + 1;
};
```

### Número Primo
```
num = 17;
div = 2;
primo = true;
while (div < num and primo) {
    resto = num - (num / div) * div;
    if (resto == 0) {
        primo = false;
    };
    div = div + 1;
};
```

### Soma de Intervalo
```
inicio = 1;
fim = 100;
soma = 0;
i = inicio;
while (i <= fim) {
    soma = soma + i;
    i = i + 1;
};
```

---

## 🐛 Depuração

### Ativar Visualização de Tokens
```python
# Em mainInterpret.py
print_tokens = True
```

### Ativar Visualização da AST
```python
# Em mainInterpret.py
print_tree = True
```

### Ver Bytecode
```bash
python mainBytecode.py
```

---

## 📌 Atalhos Úteis

### Template Básico
```
#{ Descrição do programa }#

#{ Variáveis }#
x = 0;
y = 0;

#{ Processamento }#
# ... código ...

#{ Saída }#
print(resultado);
```

### Template com Loop
```
#{ Inicialização }#
i = 0;
max = 10;

#{ Loop }#
while (i < max) {
    #{ Processamento }#
    
    #{ Atualização }#
    i = i + 1;
};
```

### Template com Validação
```
#{ Entrada }#
valor = 10;

#{ Validação }#
if (valor >= 0 and valor <= 100) {
    #{ Processamento válido }#
    print("Válido");
} else {
    #{ Tratamento de erro }#
    print("Inválido");
};
```

---

## 📖 Documentação Completa

Para informações detalhadas, consulte:

- **[README.md](README.md)** - Índice completo
- **[01-Introducao.md](01-Introducao.md)** - Visão geral
- **[02-Tipos-de-Dados.md](02-Tipos-de-Dados.md)** - Tipos detalhados
- **[03-Operadores.md](03-Operadores.md)** - Operadores completos
- **[04-Estruturas-de-Controle.md](04-Estruturas-de-Controle.md)** - Controle de fluxo
- **[05-Variaveis.md](05-Variaveis.md)** - Variáveis em detalhe
- **[06-Exemplos-Praticos.md](06-Exemplos-Praticos.md)** - 13 programas completos
- **[07-Arquitetura-Compilador.md](07-Arquitetura-Compilador.md)** - Implementação
- **[08-Referencia-Bytecode.md](08-Referencia-Bytecode.md)** - Opcodes
- **[09-Tratamento-Erros.md](09-Tratamento-Erros.md)** - Erros e debug

---

## 🎓 Lembre-se

1. Todo comando termina com `;`
2. Blocos usam `{ }`
3. Condições em `( )`
4. Variáveis são globais
5. Tipos são dinâmicos
6. Strings usam `"`
7. Comentários usam `#{ }#`
8. `break` só em loops
9. Inicialize variáveis antes de usar
10. Use nomes descritivos

---

**Versão: 1.0 | Última atualização: 2025**
