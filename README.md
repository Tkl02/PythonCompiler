# Documentação da Linguagem

Bem-vindo à documentação completa desta linguagem de programação customizada, implementada em Python para fins educacionais.

## 📚 Índice da Documentação

### Para Iniciantes

1. **[Introdução](Docs/01-Introducao.md)**
   - Visão geral da linguagem
   - Arquitetura do projeto (Interpretador vs Compilador)
   - Como executar programas
   - Estrutura básica de um programa

2. **[Tipos de Dados](Docs/02-Tipos-de-Dados.md)**
   - Integer (Inteiros)
   - Float (Ponto Flutuante)
   - String (Cadeias de Caracteres)
   - Boolean (Booleanos)
   - Conversões automáticas
   - Operações por tipo

3. **[Operadores](Docs/03-Operadores.md)**
   - Aritméticos: `+`, `-`, `*`, `/`
   - Comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`
   - Lógicos: `and`, `or`, `not`
   - Unários: `-`, `+`
   - Precedência de operadores
   - Exemplos práticos

4. **[Estruturas de Controle](Docs/04-Estruturas-de-Controle.md)**
   - Condicionais: `if`, `else`, `else if`
   - Laços: `while`
   - Comando `break`
   - Exemplos completos
   - Boas práticas

5. **[Variáveis](Docs/05-Variaveis.md)**
   - Declaração e atribuição
   - Regras de nomenclatura
   - Escopo (global)
   - Operações com variáveis
   - Flags e variáveis temporárias

6. **[Exemplos Práticos](Docs/06-Exemplos-Praticos.md)**
   - 13 programas completos comentados
   - Calculadoras e conversores
   - Algoritmos clássicos (Fibonacci, Fatorial, Primo)
   - Sistemas de validação e análise

### Para Desenvolvedores

7. **[Arquitetura do Compilador](Docs/07-Arquitetura-Compilador.md)**
   - Análise Léxica (Lexer)
   - Análise Sintática (Parser)
   - AST (Árvore Sintática Abstrata)
   - Interpretador (Visitor Pattern)
   - Compilador de Bytecode
   - Sistema de tipos
   - Tratamento de erros

8. **[Referência de Bytecode](Docs/08-Referencia-Bytecode.md)**
   - Modelo de pilha
   - Todos os opcodes detalhados
   - Exemplos de compilação
   - Tabela de referência rápida
   - Notas técnicas

9. **[Tratamento de Erros e Depuração](Docs/09-Tratamento-Erros.md)**
   - Erros léxicos, sintáticos e semânticos
   - Mensagens de erro detalhadas
   - Recuperação de erros
   - Ferramentas de depuração
   - Boas práticas
   - Checklist de depuração

10. **[Referência Rápida (Cheat Sheet)](Docs/10-Referencia-Rapida.md)**
    - Sintaxe básica condensada
    - Tabelas de operadores e tipos
    - Padrões e algoritmos comuns
    - Guia de consulta rápida

11. **[Guia de Extensão e Melhorias](Docs/11-Guia-Extensao.md)**
    - Sugestões de novas features
    - Roadmap de implementação
    - Guia passo a passo
    - Checklist de desenvolvimento

---

## 🚀 Início Rápido

### 1. Primeiro Programa

Crie ou edite o arquivo `code.txt` na raiz do projeto:

```
print("Olá, Mundo!");
```

Execute:
```bash
python mainInterpret.py
```

Saída:
```
Olá, Mundo!
```

### 2. Programa com Variáveis

```
nome = "João";
idade = 25;
mensagem = "Olá, " + nome + "! Você tem " + idade + " anos.";
print(mensagem);
```

### 3. Programa com Estruturas de Controle

```
numero = 7;

if (numero > 10) {
    print("Maior que 10");
} else {
    print("Menor ou igual a 10");
};

contador = 1;
while (contador <= 5) {
    print("Contagem: " + contador);
    contador = contador + 1;
};
```

---

## 📖 Guia de Leitura Recomendado

### Para Aprender a Programar na Linguagem

1. Comece com [Introdução](Docs/01-Introducao.md)
2. Aprenda sobre [Tipos de Dados](Docs/02-Tipos-de-Dados.md)
3. Domine os [Operadores](Docs/03-Operadores.md)
4. Estude [Estruturas de Controle](Docs/04-Estruturas-de-Controle.md)
5. Pratique com [Variáveis](Docs/05-Variaveis.md)
6. Implemente os [Exemplos Práticos](Docs/06-Exemplos-Praticos.md)
7. Consulte [Tratamento de Erros](Docs/09-Tratamento-Erros.md) quando necessário

### Para Entender a Implementação

1. Comece com [Arquitetura do Compilador](Docs/7-Arquitetura-Compilador.md)
2. Estude a [Referência de Bytecode](Docs/08-Referencia-Bytecode.md)
3. Explore os códigos fonte comentados
4. Experimente modificar a linguagem

---

## 🎯 Funcionalidades da Linguagem

### ✅ Implementado

- ✓ Tipos primitivos (Integer, Float, String, Boolean)
- ✓ Operadores aritméticos, lógicos e de comparação
- ✓ Variáveis globais
- ✓ Estruturas condicionais (if-else)
- ✓ Laços de repetição (while)
- ✓ Comando break
- ✓ Função print()
- ✓ Comentários em bloco
- ✓ Interpretador direto
- ✓ Compilador para bytecode
- ✓ Tratamento de erros robusto
- ✓ Recuperação de erros sintáticos
- ✓ Sistema de tipos dinâmico

### 🔮 Possíveis Extensões Futuras

- ⭕ Máquina virtual para executar bytecode
- ⭕ Funções definidas pelo usuário
- ⭕ Arrays e estruturas de dados
- ⭕ Laço for
- ⭕ Operador módulo (%)
- ⭕ Variáveis locais e escopo
- ⭕ Input do usuário
- ⭕ Operadores compostos (+=, -=, etc.)
- ⭕ Strings multi-linha
- ⭕ Comentários de linha única

---

## 🔧 Arquivos do Projeto

### Executáveis Principais

- **`mainInterpret.py`**: Executa código usando interpretador direto
- **`mainBytecode.py`**: Compila código para bytecode e exibe

### Módulo Interpreter/

- **`lexer.py`**: Análise léxica - converte texto em tokens
- **`token.py`**: Definição de tipos de tokens
- **`parser.py`**: Análise sintática - constrói AST
- **`ast_nodes.py`**: Definição dos nós da AST
- **`interpreter.py`**: Executa AST usando Visitor Pattern
- **`types.py`**: Sistema de tipos (Integer, Float, String, Boolean)

### Módulo Compiler/

- **`compiler.py`**: Gera bytecode a partir da AST
- **`opcodes.py`**: Definição dos códigos de operação
- **`bytecode.py`**: Estrutura de dados para bytecode
- **`disasembler.py`**: Visualização de bytecode gerado

### Outros

- **`code.txt`**: Arquivo de entrada (código a ser executado)
- **`teste.py`**: Arquivo de testes
- **`README.md`**: Documentação principal do projeto

---

## 💡 Exemplos Rápidos

### Cálculo de Fatorial

```
numero = 5;
fatorial = 1;
i = 1;

while (i <= numero) {
    fatorial = fatorial * i;
    i = i + 1;
};

print("Fatorial de " + numero + " é " + fatorial);
#{ Saída: Fatorial de 5 é 120 }#
```

### Verificação de Número Primo

```
numero = 17;
divisor = 2;
primo = true;

while (divisor < numero and primo) {
    resto = numero - (numero / divisor) * divisor;
    if (resto == 0) {
        primo = false;
    };
    divisor = divisor + 1;
};

if (primo) {
    print(numero + " é primo!");
} else {
    print(numero + " não é primo");
};
```

### Sequência de Fibonacci

```
n = 10;
a = 0;
b = 1;
contador = 1;

while (contador <= n) {
    print("F" + contador + " = " + a);
    proximo = a + b;
    a = b;
    b = proximo;
    contador = contador + 1;
};
```

---

## 🐛 Depuração

### Visualizar Tokens

Edite `mainInterpret.py`:
```python
print_tokens = True  # Mude para True
```

### Visualizar AST

Edite `mainInterpret.py`:
```python
print_tree = True  # Mude para True
```

### Visualizar Bytecode

Execute:
```bash
python mainBytecode.py
```

---

## 📝 Sintaxe Rápida

### Declaração de Variável
```
nome = valor;
```

### Condicional
```
if (condição) {
    # código
} else {
    # código
};
```

### Loop
```
while (condição) {
    # código
};
```

### Comentários
```
#{ Este é um comentário }#
```

### Print
```
print(expressão);
```

---

## 🎓 Conceitos Importantes

### Tipagem Dinâmica

Variáveis não precisam de declaração de tipo:
```
x = 10;        #{ x é Integer }#
x = "texto";   #{ agora x é String }#
x = 3.14;      #{ agora x é Float }#
```

### Conversão Automática

Operações entre Integer e Float convertem automaticamente:
```
a = 10;      #{ Integer }#
b = 2.5;     #{ Float }#
c = a + b;   #{ c = 12.5 (Float) }#
```

### Concatenação Universal

Strings podem concatenar com qualquer tipo:
```
idade = 25;
texto = "Idade: " + idade;  #{ "Idade: 25" }#
```

---

## 🤝 Contribuindo

Este projeto é educacional. Sugestões de melhorias:

1. Implementar VM para executar bytecode
2. Adicionar mais tipos de dados
3. Implementar funções
4. Melhorar mensagens de erro
5. Adicionar mais exemplos

---

## 📞 Suporte

Ao encontrar problemas:

1. Verifique a [documentação de erros](Docs/09-Tratamento-Erros.md)
2. Use as ferramentas de depuração
3. Consulte os [exemplos práticos](Docs/06-Exemplos-Praticos.md)
4. Revise a [arquitetura](Docs/07-Arquitetura-Compilador.md)

---

## 📄 Licença

Projeto educacional de código aberto.

---

## ✨ Características Técnicas

- **Linguagem de implementação**: Python 3
- **Paradigma**: Imperativo, procedural
- **Análise**: LL(2) - Parser com 2 tokens de lookahead
- **Representação intermediária**: AST
- **Execução**: Interpretação direta ou compilação para bytecode
- **Sistema de tipos**: Dinâmico com verificação em runtime
- **Gerenciamento de memória**: Garbage collection do Python
- **Tratamento de erros**: Recuperação com sincronização

---
visitor
Composite -> nos da ast
strategy -> __add__ __sub__ ...

**Boa programação! 🚀**
