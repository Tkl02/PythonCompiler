# Exemplos Práticos

Esta seção apresenta programas completos que demonstram o uso combinado de todas as funcionalidades da linguagem.

## 1. Calculadora de Média de Notas

**Objetivo:** Calcular a média de notas e determinar o status do aluno.

```
#{ ===================================
   Programa: Calculadora de Média
   Descrição: Calcula média de 4 notas
              e determina aprovação
   =================================== }#

print("=== CALCULADORA DE MÉDIA ===");

#{ Definição das notas }#
nota1 = 8.5;
nota2 = 7.0;
nota3 = 9.0;
nota4 = 6.5;

#{ Cálculo da média }#
soma = nota1 + nota2 + nota3 + nota4;
media = soma / 4;

print("Nota 1: " + nota1);
print("Nota 2: " + nota2);
print("Nota 3: " + nota3);
print("Nota 4: " + nota4);
print("Média: " + media);

#{ Determinação do status }#
if (media >= 7.0) {
    print("Status: APROVADO");
} else if (media >= 5.0) {
    print("Status: RECUPERAÇÃO");
} else {
    print("Status: REPROVADO");
};

print("=== FIM ===");
```

**Saída:**
```
=== CALCULADORA DE MÉDIA ===
Nota 1: 8.5
Nota 2: 7.0
Nota 3: 9.0
Nota 4: 6.5
Média: 7.75
Status: APROVADO
=== FIM ===
```

---

## 2. Cálculo de Fatorial

**Objetivo:** Calcular o fatorial de um número usando loop.

```
#{ ===================================
   Programa: Cálculo de Fatorial
   Descrição: Calcula n! usando while
   =================================== }#

numero = 5;
fatorial = 1;
contador = 1;

print("Calculando fatorial de " + numero);

while (contador <= numero) {
    fatorial = fatorial * contador;
    print(contador + "! = " + fatorial);
    contador = contador + 1;
};

print("Resultado final: " + numero + "! = " + fatorial);
```

**Saída:**
```
Calculando fatorial de 5
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
Resultado final: 5! = 120
```

---

## 3. Tabuada

**Objetivo:** Gerar a tabuada de um número.

```
#{ ===================================
   Programa: Tabuada
   Descrição: Gera tabuada de 1 a 10
   =================================== }#

numero = 7;
i = 1;

print("=== TABUADA DO " + numero + " ===");

while (i <= 10) {
    resultado = numero * i;
    print(numero + " x " + i + " = " + resultado);
    i = i + 1;
};

print("=== FIM DA TABUADA ===");
```

**Saída:**
```
=== TABUADA DO 7 ===
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
=== FIM DA TABUADA ===
```

---

## 4. Números Pares e Ímpares

**Objetivo:** Contar quantos números pares e ímpares existem em um intervalo.

```
#{ ===================================
   Programa: Contador de Pares/Ímpares
   Descrição: Conta pares e ímpares
              em um intervalo
   =================================== }#

inicio = 1;
fim = 20;
pares = 0;
impares = 0;

i = inicio;

print("Analisando números de " + inicio + " até " + fim);

while (i <= fim) {
    #{ Simula operação módulo: i % 2 }#
    resto = i - (i / 2) * 2;
    
    if (resto == 0) {
        pares = pares + 1;
    } else {
        impares = impares + 1;
    };
    
    i = i + 1;
};

print("Números pares: " + pares);
print("Números ímpares: " + impares);
print("Total: " + (pares + impares));
```

**Saída:**
```
Analisando números de 1 até 20
Números pares: 10
Números ímpares: 10
Total: 20
```

---

## 5. Sequência de Fibonacci

**Objetivo:** Gerar os primeiros N números da sequência de Fibonacci.

```
#{ ===================================
   Programa: Sequência de Fibonacci
   Descrição: Gera primeiros 10 números
              da sequência
   =================================== }#

n = 10;
a = 0;
b = 1;
contador = 1;

print("=== SEQUÊNCIA DE FIBONACCI ===");
print("Primeiros " + n + " números:");

while (contador <= n) {
    print("F" + contador + " = " + a);
    
    #{ Próximo número da sequência }#
    proximo = a + b;
    a = b;
    b = proximo;
    
    contador = contador + 1;
};

print("=== FIM ===");
```

**Saída:**
```
=== SEQUÊNCIA DE FIBONACCI ===
Primeiros 10 números:
F1 = 0
F2 = 1
F3 = 1
F4 = 2
F5 = 3
F6 = 5
F7 = 8
F8 = 13
F9 = 21
F10 = 34
=== FIM ===
```

---

## 6. Verificação de Número Primo

**Objetivo:** Verificar se um número é primo.

```
#{ ===================================
   Programa: Verificador de Primo
   Descrição: Verifica se número é primo
   =================================== }#

numero = 17;
divisor = 2;
primo = true;

print("Verificando se " + numero + " é primo...");

#{ Casos especiais }#
if (numero <= 1) {
    primo = false;
};

#{ Testa divisores de 2 até numero-1 }#
while (divisor < numero and primo) {
    #{ Simula módulo: numero % divisor }#
    resto = numero - (numero / divisor) * divisor;
    
    if (resto == 0) {
        print("Divisível por " + divisor);
        primo = false;
    };
    
    divisor = divisor + 1;
};

if (primo) {
    print(numero + " É PRIMO!");
} else {
    print(numero + " NÃO é primo");
};
```

**Saída (para 17):**
```
Verificando se 17 é primo...
17 É PRIMO!
```

**Saída (para 12):**
```
Verificando se 12 é primo...
Divisível por 2
12 NÃO é primo
```

---

## 7. Conversor de Temperatura

**Objetivo:** Converter temperaturas entre Celsius e Fahrenheit.

```
#{ ===================================
   Programa: Conversor de Temperatura
   Descrição: Celsius <-> Fahrenheit
   =================================== }#

print("=== CONVERSOR DE TEMPERATURA ===");

#{ Celsius para Fahrenheit }#
celsius = 25;
fahrenheit = celsius * 9 / 5 + 32;

print(celsius + "°C = " + fahrenheit + "°F");

#{ Fahrenheit para Celsius }#
fahrenheit2 = 77;
celsius2 = (fahrenheit2 - 32) * 5 / 9;

print(fahrenheit2 + "°F = " + celsius2 + "°C");

#{ Tabela de conversão }#
print("");
print("TABELA DE CONVERSÃO:");
print("Celsius | Fahrenheit");
print("--------|------------");

temp_c = 0;
while (temp_c <= 100) {
    temp_f = temp_c * 9 / 5 + 32;
    print(temp_c + "°C    | " + temp_f + "°F");
    temp_c = temp_c + 20;
};
```

**Saída:**
```
=== CONVERSOR DE TEMPERATURA ===
25°C = 77°F
77°F = 25°C

TABELA DE CONVERSÃO:
Celsius | Fahrenheit
--------|------------
0°C    | 32°F
20°C    | 68°F
40°C    | 104°F
60°C    | 140°F
80°C    | 176°F
100°C    | 212°F
```

---

## 8. Calculadora de IMC

**Objetivo:** Calcular o Índice de Massa Corporal e classificar.

```
#{ ===================================
   Programa: Calculadora de IMC
   Descrição: Calcula IMC e classifica
   =================================== }#

nome = "João Silva";
peso = 75.0;     #{ kg }#
altura = 1.75;   #{ metros }#

print("=== CALCULADORA DE IMC ===");
print("Nome: " + nome);
print("Peso: " + peso + " kg");
print("Altura: " + altura + " m");

#{ Cálculo: IMC = peso / (altura * altura) }#
imc = peso / (altura * altura);

print("IMC: " + imc);

#{ Classificação }#
if (imc < 18.5) {
    print("Classificação: ABAIXO DO PESO");
} else if (imc < 25) {
    print("Classificação: PESO NORMAL");
} else if (imc < 30) {
    print("Classificação: SOBREPESO");
} else if (imc < 35) {
    print("Classificação: OBESIDADE GRAU I");
} else if (imc < 40) {
    print("Classificação: OBESIDADE GRAU II");
} else {
    print("Classificação: OBESIDADE GRAU III");
};

print("=== FIM ===");
```

**Saída:**
```
=== CALCULADORA DE IMC ===
Nome: João Silva
Peso: 75.0 kg
Altura: 1.75 m
IMC: 24.489795918367346
Classificação: PESO NORMAL
=== FIM ===
```

---

## 9. Soma de Números em Intervalo

**Objetivo:** Somar todos os números em um intervalo com condições.

```
#{ ===================================
   Programa: Soma Condicional
   Descrição: Soma apenas números pares
              em um intervalo
   =================================== }#

inicio = 1;
fim = 50;
soma_pares = 0;
soma_impares = 0;
quantidade_pares = 0;

i = inicio;

print("Somando números de " + inicio + " até " + fim);

while (i <= fim) {
    #{ Verifica se é par }#
    resto = i - (i / 2) * 2;
    
    if (resto == 0) {
        soma_pares = soma_pares + i;
        quantidade_pares = quantidade_pares + 1;
    } else {
        soma_impares = soma_impares + i;
    };
    
    i = i + 1;
};

print("");
print("RESULTADOS:");
print("Soma dos pares: " + soma_pares);
print("Quantidade de pares: " + quantidade_pares);
print("Média dos pares: " + (soma_pares / quantidade_pares));
print("Soma dos ímpares: " + soma_impares);
print("Soma total: " + (soma_pares + soma_impares));
```

**Saída:**
```
Somando números de 1 até 50

RESULTADOS:
Soma dos pares: 650
Quantidade de pares: 25
Média dos pares: 26
Soma dos ímpares: 625
Soma total: 1275
```

---

## 10. Sistema de Login Simulado

**Objetivo:** Simular sistema de login com tentativas limitadas.

```
#{ ===================================
   Programa: Sistema de Login
   Descrição: Login com 3 tentativas
   =================================== }#

usuario_correto = "admin";
senha_correta = "1234";

max_tentativas = 3;
tentativa = 0;
autenticado = false;

print("=== SISTEMA DE LOGIN ===");

while (tentativa < max_tentativas and not autenticado) {
    tentativa = tentativa + 1;
    print("");
    print("Tentativa " + tentativa + " de " + max_tentativas);
    
    #{ Simulação de entrada (em aplicação real, seria input) }#
    if (tentativa == 1) {
        usuario = "admin";
        senha = "0000";  #{ Senha errada }#
    };
    
    if (tentativa == 2) {
        usuario = "user";  #{ Usuário errado }#
        senha = "1234";
    };
    
    if (tentativa == 3) {
        usuario = "admin";
        senha = "1234";  #{ Correto! }#
    };
    
    print("Usuário: " + usuario);
    
    #{ Verificação }#
    if (usuario == usuario_correto and senha == senha_correta) {
        autenticado = true;
        print("LOGIN REALIZADO COM SUCESSO!");
        break;
    } else {
        if (usuario != usuario_correto) {
            print("ERRO: Usuário incorreto");
        } else {
            print("ERRO: Senha incorreta");
        };
    };
};

print("");

if (not autenticado) {
    print("ACESSO BLOQUEADO - Máximo de tentativas excedido");
} else {
    print("Bem-vindo ao sistema!");
};

print("=== FIM ===");
```

**Saída:**
```
=== SISTEMA DE LOGIN ===

Tentativa 1 de 3
Usuário: admin
ERRO: Senha incorreta

Tentativa 2 de 3
Usuário: user
ERRO: Usuário incorreto

Tentativa 3 de 3
Usuário: admin
LOGIN REALIZADO COM SUCESSO!

Bem-vindo ao sistema!
=== FIM ===
```

---

## 11. Contador de Dígitos

**Objetivo:** Contar quantos dígitos tem um número.

```
#{ ===================================
   Programa: Contador de Dígitos
   Descrição: Conta dígitos de um número
   =================================== }#

numero = 123456;
numero_original = numero;
contador = 0;

print("Contando dígitos de: " + numero);

if (numero == 0) {
    contador = 1;
} else {
    while (numero > 0) {
        numero = numero / 10;
        contador = contador + 1;
    };
};

print("O número " + numero_original + " tem " + contador + " dígitos");
```

**Saída:**
```
Contando dígitos de: 123456
O número 123456 tem 6 dígitos
```

---

## 12. Jogo de Adivinhação (Simulado)

**Objetivo:** Simular um jogo onde o jogador tenta adivinhar um número.

```
#{ ===================================
   Programa: Jogo de Adivinhação
   Descrição: Adivinhe o número secreto
   =================================== }#

numero_secreto = 42;
max_tentativas = 5;
tentativa = 0;
acertou = false;

print("=== JOGO DE ADIVINHAÇÃO ===");
print("Tente adivinhar o número entre 1 e 100!");
print("Você tem " + max_tentativas + " tentativas");

while (tentativa < max_tentativas and not acertou) {
    tentativa = tentativa + 1;
    
    #{ Simulação de palpites }#
    if (tentativa == 1) { palpite = 50; };
    if (tentativa == 2) { palpite = 30; };
    if (tentativa == 3) { palpite = 40; };
    if (tentativa == 4) { palpite = 45; };
    if (tentativa == 5) { palpite = 42; };
    
    print("");
    print("Tentativa " + tentativa + ": " + palpite);
    
    if (palpite == numero_secreto) {
        acertou = true;
        print("PARABÉNS! Você acertou!");
        break;
    } else if (palpite < numero_secreto) {
        print("Muito baixo! Tente um número maior");
    } else {
        print("Muito alto! Tente um número menor");
    };
};

print("");

if (not acertou) {
    print("Que pena! Você não acertou.");
    print("O número secreto era: " + numero_secreto);
} else {
    print("Você acertou em " + tentativa + " tentativas!");
};

print("=== FIM DO JOGO ===");
```

**Saída:**
```
=== JOGO DE ADIVINHAÇÃO ===
Tente adivinhar o número entre 1 e 100!
Você tem 5 tentativas

Tentativa 1: 50
Muito alto! Tente um número menor

Tentativa 2: 30
Muito baixo! Tente um número maior

Tentativa 3: 40
Muito baixo! Tente um número maior

Tentativa 4: 45
Muito alto! Tente um número menor

Tentativa 5: 42
PARABÉNS! Você acertou!

Você acertou em 5 tentativas!
=== FIM DO JOGO ===
```

---

## 13. Programa Completo: Análise de Dados

**Objetivo:** Programa mais complexo combinando várias funcionalidades.

```
#{ ===================================
   Programa: Análise de Vendas
   Descrição: Analisa dados de vendas
              e gera relatório
   =================================== }#

print("=== SISTEMA DE ANÁLISE DE VENDAS ===");
print("");

#{ Dados de entrada }#
total_vendas = 10;
venda1 = 100.50;
venda2 = 250.00;
venda3 = 75.30;
venda4 = 180.00;
venda5 = 320.50;
venda6 = 95.00;
venda7 = 450.00;
venda8 = 120.75;
venda9 = 200.00;
venda10 = 310.00;

meta = 200.0;

#{ Processamento }#
soma = venda1 + venda2 + venda3 + venda4 + venda5;
soma = soma + venda6 + venda7 + venda8 + venda9 + venda10;

media = soma / total_vendas;

#{ Contadores }#
acima_meta = 0;
abaixo_meta = 0;

#{ Análise individual }#
print("ANÁLISE INDIVIDUAL:");
print("Meta por venda: R$ " + meta);
print("");

i = 1;
while (i <= total_vendas) {
    valor = 0;
    
    #{ Seleciona o valor correto }#
    if (i == 1) { valor = venda1; };
    if (i == 2) { valor = venda2; };
    if (i == 3) { valor = venda3; };
    if (i == 4) { valor = venda4; };
    if (i == 5) { valor = venda5; };
    if (i == 6) { valor = venda6; };
    if (i == 7) { valor = venda7; };
    if (i == 8) { valor = venda8; };
    if (i == 9) { valor = venda9; };
    if (i == 10) { valor = venda10; };
    
    if (valor >= meta) {
        status = "ATINGIU";
        acima_meta = acima_meta + 1;
    } else {
        status = "NÃO ATINGIU";
        abaixo_meta = abaixo_meta + 1;
    };
    
    print("Venda " + i + ": R$ " + valor + " - " + status);
    i = i + 1;
};

#{ Relatório final }#
print("");
print("=== RELATÓRIO GERAL ===");
print("Total de vendas: " + total_vendas);
print("Soma total: R$ " + soma);
print("Média: R$ " + media);
print("Vendas acima da meta: " + acima_meta);
print("Vendas abaixo da meta: " + abaixo_meta);

percentual_acima = (acima_meta * 100) / total_vendas;
print("Percentual acima da meta: " + percentual_acima + "%");

if (media >= meta) {
    print("RESULTADO: Meta média ATINGIDA!");
} else {
    print("RESULTADO: Meta média NÃO atingida");
};

print("=== FIM DO RELATÓRIO ===");
```

**Saída:**
```
=== SISTEMA DE ANÁLISE DE VENDAS ===

ANÁLISE INDIVIDUAL:
Meta por venda: R$ 200.0

Venda 1: R$ 100.5 - NÃO ATINGIU
Venda 2: R$ 250.0 - ATINGIU
Venda 3: R$ 75.3 - NÃO ATINGIU
Venda 4: R$ 180.0 - NÃO ATINGIU
Venda 5: R$ 320.5 - ATINGIU
Venda 6: R$ 95.0 - NÃO ATINGIU
Venda 7: R$ 450.0 - ATINGIU
Venda 8: R$ 120.75 - NÃO ATINGIU
Venda 9: R$ 200.0 - ATINGIU
Venda 10: R$ 310.0 - ATINGIU

=== RELATÓRIO GERAL ===
Total de vendas: 10
Soma total: R$ 2102.05
Média: R$ 210.205
Vendas acima da meta: 5
Vendas abaixo da meta: 5
Percentual acima da meta: 50%
RESULTADO: Meta média ATINGIDA!
=== FIM DO RELATÓRIO ===
```

---

## 12. Contador com Auto-Incremento

**Objetivo:** Demonstrar uso do operador `++` para incrementos.

```
#{===================================
  Programa: Contador Regressivo
  Descrição: Usa ++ para contagem
  ===================================}#

print("=== CONTADOR SIMPLES ===");

contador = 0;

print("Contando de 0 a 5:");

while (contador < 5) {
    print("Contador: " + contador);
    contador++;  #{ Incremento automático }#
};

print("Valor final: " + contador);
print("=== FIM ===");
```

**Saída:**
```
=== CONTADOR SIMPLES ===
Contando de 0 a 5:
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
Valor final: 5
=== FIM ===
```

---

## 13. Sistema de Pontuação com Operadores Compostos

**Objetivo:** Demonstrar uso de `+=` e `-=` em sistema de pontos.

```
#{===================================
  Programa: Sistema de Pontuação
  Descrição: Gerencia pontos com +=/-=
  ===================================}#

print("=== SISTEMA DE PONTUAÇÃO ===");

pontos = 0;
print("Pontos iniciais: " + pontos);

#{ Ganhar pontos }#
print("\n--- AÇÕES POSITIVAS ---");
print("Completou missão principal...");
pontos += 100;
print("Pontos: " + pontos);

print("Achou item secreto...");
pontos += 50;
print("Pontos: " + pontos);

print("Derrotou chefe...");
pontos += 200;
print("Pontos: " + pontos);

#{ Perder pontos }#
print("\n--- PENALIDADES ---");
print("Recebeu dano...");
pontos -= 30;
print("Pontos: " + pontos);

print("Usou item raro...");
pontos -= 20;
print("Pontos: " + pontos);

#{ Resultado final }#
print("\n=== PONTUAÇÃO FINAL ===");
print("Total: " + pontos + " pontos");

if (pontos >= 300) {
    print("Classificação: MESTRE");
} else if (pontos >= 200) {
    print("Classificação: EXPERT");
} else if (pontos >= 100) {
    print("Classificação: INTERMEDIÁRIO");
} else {
    print("Classificação: INICIANTE");
};
```

**Saída:**
```
=== SISTEMA DE PONTUAÇÃO ===
Pontos iniciais: 0

--- AÇÕES POSITIVAS ---
Completou missão principal...
Pontos: 100
Achou item secreto...
Pontos: 150
Derrotou chefe...
Pontos: 350

--- PENALIDADES ---
Recebeu dano...
Pontos: 320
Usou item raro...
Pontos: 300

=== PONTUAÇÃO FINAL ===
Total: 300 pontos
Classificação: MESTRE
```

---

## 14. Validação com Operadores Lógicos Simbólicos

**Objetivo:** Demonstrar uso de `&&` e `||` em validações.

```
#{===================================
  Programa: Sistema de Validação
  Descrição: Usa && e || para regras
  ===================================}#

print("=== SISTEMA DE VALIDAÇÃO DE ACESSO ===");

#{ Dados do usuário }#
idade = 25;
possui_id = true;
e_membro = true;
dia_semana = 5;  #{ 5 = sexta-feira }#

print("Idade: " + idade);
print("Possui ID: " + possui_id);
print("É membro: " + e_membro);
print("Dia da semana: " + dia_semana);

#{ Regra 1: Maior de 18 E possui ID }#
pode_entrar_basico = (idade >= 18) && possui_id;
print("\nPode entrar (básico): " + pode_entrar_basico);

#{ Regra 2: É membro OU (maior de 21 E fim de semana) }#
fim_semana = (dia_semana == 5) || (dia_semana == 6);
pode_area_vip = e_membro || ((idade >= 21) && fim_semana);
print("Acesso VIP: " + pode_area_vip);

#{ Regra 3: Validação completa }#
acesso_completo = pode_entrar_basico && pode_area_vip;

print("\n=== RESULTADO ===");
if (acesso_completo) {
    print("ACESSO LIBERADO - VIP");
} else if (pode_entrar_basico) {
    print("ACESSO LIBERADO - Área comum");
} else {
    print("ACESSO NEGADO");
};
```

**Saída:**
```
=== SISTEMA DE VALIDAÇÃO DE ACESSO ===
Idade: 25
Possui ID: true
É membro: true
Dia da semana: 5

Pode entrar (básico): true
Acesso VIP: true

=== RESULTADO ===
ACESSO LIBERADO - VIP
```

---

## 15. Simulador de Jogo com Todas as Funcionalidades

**Objetivo:** Combinar `++`, `+=`, `-=`, `&&` e `||` em um programa completo.

```
#{===================================
  Programa: Simulador de Batalha RPG
  Descrição: Demonstra todas as novas
             funcionalidades combinadas
  ===================================}#

print("=== SIMULADOR DE BATALHA RPG ===\n");

#{ Status do jogador }#
vida = 100;
mana = 50;
nivel = 1;
experiencia = 0;

#{ Status do inimigo }#
vida_inimigo = 80;

print("--- STATUS INICIAL ---");
print("Jogador - Vida: " + vida + " | Mana: " + mana + " | Nível: " + nivel);
print("Inimigo - Vida: " + vida_inimigo);

turno = 0;

#{ Loop de batalha }#
while ((vida > 0) && (vida_inimigo > 0)) {
    turno++;
    print("\n--- TURNO " + turno + " ---");
    
    #{ Jogador ataca }#
    tem_mana = mana >= 10;
    pode_especial = tem_mana && (nivel >= 1);
    
    if (pode_especial) {
        print("Ataque especial!");
        vida_inimigo -= 25;
        mana -= 10;
    } else {
        print("Ataque normal!");
        vida_inimigo -= 10;
    };
    
    print("Vida inimigo: " + vida_inimigo);
    
    #{ Verifica se inimigo morreu }#
    if (vida_inimigo <= 0) {
        print("\n=== VITÓRIA! ===");
        experiencia += 100;
        print("XP ganho: 100");
        break;
    };
    
    #{ Inimigo ataca }#
    print("Inimigo contra-ataca!");
    vida -= 15;
    print("Sua vida: " + vida);
    
    #{ Regeneração de mana }#
    mana += 5;
    if (mana > 50) {
        mana = 50;
    };
};

#{ Resultado final }#
print("\n--- STATUS FINAL ---");
print("Vida: " + vida);
print("Mana: " + mana);
print("XP: " + experiencia);

sobreviveu = vida > 0;
venceu = (vida > 0) && (vida_inimigo <= 0);

if (venceu) {
    print("\nRESULTADO: VENCEU A BATALHA!");
} else if (sobreviveu) {
    print("\nRESULTADO: Batalha em andamento...");
} else {
    print("\nRESULTADO: DERROTADO!");
};
```

**Saída (exemplo):**
```
=== SIMULADOR DE BATALHA RPG ===

--- STATUS INICIAL ---
Jogador - Vida: 100 | Mana: 50 | Nível: 1
Inimigo - Vida: 80

--- TURNO 1 ---
Ataque especial!
Vida inimigo: 55
Inimigo contra-ataca!
Sua vida: 85

--- TURNO 2 ---
Ataque especial!
Vida inimigo: 30
Inimigo contra-ataca!
Sua vida: 70

--- TURNO 3 ---
Ataque especial!
Vida inimigo: 5
Inimigo contra-ataca!
Sua vida: 55

--- TURNO 4 ---
Ataque especial!
Vida inimigo: -20

=== VITÓRIA! ===
XP ganho: 100

--- STATUS FINAL ---
Vida: 55
Mana: 20
XP: 100

RESULTADO: VENCEU A BATALHA!
```

