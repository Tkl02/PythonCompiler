# Estruturas de Controle

As estruturas de controle permitem que o programa tome decisões e execute código repetidamente. A linguagem suporta estruturas condicionais (`if-else`) e laços de repetição (`while`).

## 1. Estrutura Condicional: `if-else`

A estrutura `if` permite executar código condicionalmente, baseado em uma expressão booleana.

### Sintaxe Básica

```
if (condição) {
    #{ código executado se condição for verdadeira }#
};
```

**Elementos:**
- **`if`**: palavra-chave que inicia a condicional
- **`(condição)`**: expressão que resulta em Boolean (entre parênteses obrigatórios)
- **`{ }`**: bloco de código delimitado por chaves
- **`;`**: ponto e vírgula após o fechamento da chave

### Exemplo Simples

```
idade = 20;

if (idade >= 18) {
    print("Você é maior de idade");
};

#{ Saída: Você é maior de idade }#
```

---

### `if-else`: Duas Alternativas

Executa um bloco se a condição for verdadeira, outro bloco se for falsa.

**Sintaxe:**

```
if (condição) {
    #{ código se verdadeiro }#
} else {
    #{ código se falso }#
};
```

**Exemplo:**

```
nota = 6.5;

if (nota >= 7.0) {
    print("Aprovado");
} else {
    print("Reprovado");
};

#{ Saída: Reprovado }#
```

---

### `if-else if-else`: Múltiplas Condições

Permite verificar várias condições em sequência.

**Sintaxe:**

```
if (condição1) {
    #{ código se condição1 for verdadeira }#
} else if (condição2) {
    #{ código se condição2 for verdadeira }#
} else {
    #{ código se todas forem falsas }#
};
```

**Exemplo:**

```
nota = 5.5;

if (nota >= 7.0) {
    print("Aprovado");
} else if (nota >= 5.0) {
    print("Recuperação");
} else {
    print("Reprovado");
};

#{ Saída: Recuperação }#
```

---

### Condições Compostas

Você pode usar operadores lógicos (`and`, `or`, `not`) nas condições.

**Exemplo 1: AND**

```
idade = 20;
tem_carteira = true;

if (idade >= 18 and tem_carteira) {
    print("Pode dirigir");
} else {
    print("Não pode dirigir");
};

#{ Saída: Pode dirigir }#
```

**Exemplo 2: OR**

```
dia = "sábado";
feriado = false;

if (dia == "sábado" or dia == "domingo" or feriado) {
    print("É dia de descanso!");
} else {
    print("Dia de trabalho");
};

#{ Saída: É dia de descanso! }#
```

**Exemplo 3: NOT**

```
chovendo = false;

if (not chovendo) {
    print("Vamos ao parque!");
} else {
    print("Melhor ficar em casa");
};

#{ Saída: Vamos ao parque! }#
```

---

### Aninhamento de `if`

Estruturas `if` podem ser aninhadas dentro de outras.

**Exemplo:**

```
idade = 20;
tem_ingresso = true;

if (idade >= 18) {
    if (tem_ingresso) {
        print("Entrada permitida");
    } else {
        print("Precisa comprar ingresso");
    };
} else {
    print("Entrada proibida - menor de idade");
};

#{ Saída: Entrada permitida }#
```

---

### Casos Práticos

**Classificação de Temperatura:**

```
temperatura = 25;

if (temperatura < 0) {
    print("Congelante");
} else if (temperatura < 15) {
    print("Frio");
} else if (temperatura < 25) {
    print("Agradável");
} else if (temperatura < 35) {
    print("Quente");
} else {
    print("Muito quente");
};

#{ Saída: Quente }#
```

**Verificação de Intervalo:**

```
numero = 50;

if (numero >= 1 and numero <= 100) {
    print("Número está no intervalo [1, 100]");
} else {
    print("Número fora do intervalo");
};

#{ Saída: Número está no intervalo [1, 100] }#
```

**Sistema de Login Simplificado:**

```
usuario = "admin";
senha = "1234";

usuario_correto = "admin";
senha_correta = "1234";

if (usuario == usuario_correto and senha == senha_correta) {
    print("Login bem-sucedido!");
} else if (usuario != usuario_correto) {
    print("Usuário incorreto");
} else {
    print("Senha incorreta");
};

#{ Saída: Login bem-sucedido! }#
```

---

## 2. Laço de Repetição: `while`

O `while` executa um bloco de código repetidamente enquanto uma condição for verdadeira.

### Sintaxe Básica

```
while (condição) {
    #{ código executado enquanto condição for verdadeira }#
};
```

**Elementos:**
- **`while`**: palavra-chave que inicia o laço
- **`(condição)`**: expressão booleana verificada a cada iteração
- **`{ }`**: bloco de código a ser repetido
- **`;`**: ponto e vírgula após o fechamento da chave

### Exemplo Simples

```
contador = 0;

while (contador < 5) {
    print(contador);
    contador = contador + 1;
};

#{
  Saída:
  0
  1
  2
  3
  4
}#
```

---

### Estrutura de um Loop Típico

Um loop `while` geralmente segue este padrão:

1. **Inicialização**: Definir variável de controle antes do loop
2. **Condição**: Testar a variável de controle
3. **Atualização**: Modificar a variável dentro do loop

**Exemplo:**

```
#{ 1. Inicialização }#
i = 1;

#{ 2. Condição }#
while (i <= 10) {
    print("Número: " + i);
    
    #{ 3. Atualização }#
    i = i + 1;
};
```

---

### Contagem Regressiva

```
contador = 5;

while (contador > 0) {
    print("Contagem: " + contador);
    contador = contador - 1;
};

print("Fim!");

#{
  Saída:
  Contagem: 5
  Contagem: 4
  Contagem: 3
  Contagem: 2
  Contagem: 1
  Fim!
}#
```

---

### Acumulação de Valores

**Soma de números de 1 a 10:**

```
soma = 0;
i = 1;

while (i <= 10) {
    soma = soma + i;
    i = i + 1;
};

print("A soma é: " + soma);

#{ Saída: A soma é: 55 }#
```

**Cálculo de fatorial:**

```
numero = 5;
fatorial = 1;
i = 1;

while (i <= numero) {
    fatorial = fatorial * i;
    i = i + 1;
};

print("Fatorial de " + numero + " é: " + fatorial);

#{ Saída: Fatorial de 5 é: 120 }#
```

---

### Loops Aninhados

Loops podem ser colocados dentro de outros loops.

**Tabela de multiplicação:**

```
i = 1;

while (i <= 3) {
    j = 1;
    
    while (j <= 3) {
        resultado = i * j;
        print(i + " x " + j + " = " + resultado);
        j = j + 1;
    };
    
    print("---");
    i = i + 1;
};

#{
  Saída:
  1 x 1 = 1
  1 x 2 = 2
  1 x 3 = 3
  ---
  2 x 1 = 2
  2 x 2 = 4
  2 x 3 = 6
  ---
  3 x 1 = 3
  3 x 2 = 6
  3 x 3 = 9
  ---
}#
```

---

### Condições Compostas em `while`

**Exemplo com múltiplas condições:**

```
tentativas = 0;
max_tentativas = 3;
senha_correta = false;

while (tentativas < max_tentativas and not senha_correta) {
    print("Tentativa " + (tentativas + 1));
    
    #{ Simulação: só acerta na 2ª tentativa }#
    if (tentativas == 1) {
        senha_correta = true;
        print("Senha correta!");
    } else {
        print("Senha incorreta");
    };
    
    tentativas = tentativas + 1;
};

if (not senha_correta) {
    print("Acesso bloqueado");
};

#{
  Saída:
  Tentativa 1
  Senha incorreta
  Tentativa 2
  Senha correta!
}#
```

---

## 3. Comando `break`

O comando `break` interrompe a execução de um loop `while` imediatamente.

### Sintaxe

```
while (condição) {
    if (condição_de_saída) {
        break;
    };
    #{ mais código }#
};
```

### Exemplo Básico

```
i = 0;

while (i < 10) {
    if (i == 5) {
        print("Encontrei o 5, saindo...");
        break;
    };
    
    print("i = " + i);
    i = i + 1;
};

print("Loop terminado");

#{
  Saída:
  i = 0
  i = 1
  i = 2
  i = 3
  i = 4
  Encontrei o 5, saindo...
  Loop terminado
}#
```

---

### Busca em Sequência

```
numero_procurado = 7;
i = 1;
encontrado = false;

while (i <= 10) {
    if (i == numero_procurado) {
        print("Número " + numero_procurado + " encontrado!");
        encontrado = true;
        break;
    };
    
    i = i + 1;
};

if (not encontrado) {
    print("Número não encontrado");
};

#{
  Saída:
  Número 7 encontrado!
}#
```

---

### Validação de Entrada (Simulação)

```
tentativa = 0;
senha_correta = "1234";

while (true) {
    tentativa = tentativa + 1;
    
    #{ Simulação: usuário acerta na 3ª tentativa }#
    if (tentativa == 3) {
        print("Senha correta!");
        break;
    };
    
    print("Tentativa " + tentativa + " - Senha incorreta");
    
    if (tentativa >= 5) {
        print("Muitas tentativas - bloqueado");
        break;
    };
};

#{
  Saída:
  Tentativa 1 - Senha incorreta
  Tentativa 2 - Senha incorreta
  Senha correta!
}#
```

---

### `break` em Loops Aninhados

**Importante:** O `break` só sai do loop mais interno.

```
i = 0;

while (i < 3) {
    j = 0;
    
    while (j < 5) {
        if (j == 2) {
            print("Break no loop interno (i=" + i + ", j=" + j + ")");
            break;  #{ Sai apenas do loop de j }#
        };
        
        print("i=" + i + ", j=" + j);
        j = j + 1;
    };
    
    i = i + 1;
};

#{
  Saída:
  i=0, j=0
  i=0, j=1
  Break no loop interno (i=0, j=2)
  i=1, j=0
  i=1, j=1
  Break no loop interno (i=1, j=2)
  i=2, j=0
  i=2, j=1
  Break no loop interno (i=2, j=2)
}#
```

---

## 4. Exemplos Práticos Completos

### Programa 1: Calculadora de Média

```
print("=== Calculadora de Média ===");

quantidade = 5;
soma = 0;
i = 1;

while (i <= quantidade) {
    #{ Simulando entrada de notas }#
    nota = i * 2;  #{ 2, 4, 6, 8, 10 }#
    
    print("Nota " + i + ": " + nota);
    soma = soma + nota;
    i = i + 1;
};

media = soma / quantidade;
print("Média: " + media);

if (media >= 7) {
    print("Aprovado!");
} else if (media >= 5) {
    print("Recuperação");
} else {
    print("Reprovado");
};

#{
  Saída:
  === Calculadora de Média ===
  Nota 1: 2
  Nota 2: 4
  Nota 3: 6
  Nota 4: 8
  Nota 5: 10
  Média: 6
  Recuperação
}#
```

---

### Programa 2: Verificação de Número Primo

```
numero = 17;
divisor = 2;
primo = true;

if (numero <= 1) {
    primo = false;
};

while (divisor < numero) {
    resto = numero - (numero / divisor) * divisor;  #{ Simulação de módulo }#
    
    if (resto == 0) {
        primo = false;
        break;
    };
    
    divisor = divisor + 1;
};

if (primo) {
    print(numero + " é primo");
} else {
    print(numero + " não é primo");
};

#{ Saída: 17 é primo }#
```

---

### Programa 3: Contagem de Dígitos

```
numero = 12345;
contador_digitos = 0;
temp = numero;

while (temp > 0) {
    temp = temp / 10;  #{ Remove último dígito }#
    contador_digitos = contador_digitos + 1;
};

print("O número " + numero + " tem " + contador_digitos + " dígitos");

#{ Saída: O número 12345 tem 5 dígitos }#
```

---

### Programa 4: Menu Interativo (Simulação)

```
opcao = 0;
executando = true;

while (executando) {
    print("=== MENU ===");
    print("1 - Opção A");
    print("2 - Opção B");
    print("3 - Sair");
    
    #{ Simulação de entrada do usuário }#
    opcao = opcao + 1;  #{ Simula: 1, 2, 3 }#
    
    if (opcao == 1) {
        print("Você escolheu: Opção A");
    } else if (opcao == 2) {
        print("Você escolheu: Opção B");
    } else if (opcao == 3) {
        print("Saindo...");
        executando = false;
        break;
    } else {
        print("Opção inválida");
    };
};

#{
  Saída:
  === MENU ===
  1 - Opção A
  2 - Opção B
  3 - Sair
  Você escolheu: Opção A
  === MENU ===
  1 - Opção A
  2 - Opção B
  3 - Sair
  Você escolheu: Opção B
  === MENU ===
  1 - Opção A
  2 - Opção B
  3 - Sair
  Saindo...
}#
```

---

## 5. Boas Práticas

### ✓ Use condições claras

```
#{ Bom }#
if (idade >= 18 and tem_permissao) {
    print("Acesso permitido");
};

#{ Evite }#
if (not (idade < 18 or not tem_permissao)) {
    print("Acesso permitido");
};
```

### ✓ Evite loops infinitos

```
#{ Cuidado: loop infinito! }#
i = 0;
while (i < 10) {
    print(i);
    #{ Esqueceu de incrementar i! }#
};

#{ Correto }#
i = 0;
while (i < 10) {
    print(i);
    i = i + 1;  #{ Incremento garante que o loop termine }#
};
```

### ✓ Inicialize variáveis antes de usar

```
#{ Correto }#
soma = 0;
i = 1;

while (i <= 5) {
    soma = soma + i;
    i = i + 1;
};
```

### ✓ Use `break` para saídas antecipadas

```
#{ Em vez de condições complexas }#
i = 0;
encontrado = false;

while (i < 100 and not encontrado) {
    if (i == 50) {
        encontrado = true;
    };
    i = i + 1;
};

#{ Melhor: use break }#
i = 0;

while (i < 100) {
    if (i == 50) {
        break;
    };
    i = i + 1;
};
```
