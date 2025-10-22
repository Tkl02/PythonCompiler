# Introdução à Linguagem

## Visão Geral

Esta é uma linguagem de programação customizada, implementada do zero em Python, com o propósito educacional de demonstrar os conceitos fundamentais de compiladores e interpretadores. O projeto implementa tanto um **interpretador direto** quanto um **compilador para bytecode**, oferecendo duas formas distintas de executar programas.

## Características Principais

- **Tipagem Dinâmica**: Variáveis não precisam de declaração de tipo explícita
- **Tipos Primitivos**: Integer, Float, String e Boolean
- **Estruturas de Controle**: Condicionais (if-else) e laços (while)
- **Operadores**: Aritméticos, lógicos e de comparação
- **Sistema de Comentários**: Comentários em bloco `#{ }#`
- **Função Nativa**: `print()` para saída de dados
- **Comando de Controle**: `break` para interromper laços

## Arquitetura do Projeto

O projeto está organizado em duas componentes principais:

### 1. Interpretador (Interpreter/)

O interpretador executa o código diretamente, seguindo o padrão de **árvore sintática abstrata (AST)**:

```
Código Fonte → Lexer → Parser → AST → Interpreter → Execução
```

**Componentes:**
- **Lexer** (`lexer.py`): Análise léxica - transforma texto em tokens
- **Parser** (`parser.py`): Análise sintática - constrói a AST a partir dos tokens
- **AST Nodes** (`ast_nodes.py`): Definições dos nós da árvore sintática
- **Interpreter** (`interpreter.py`): Percorre a AST e executa as instruções
- **Token** (`token.py`): Define os tipos de tokens da linguagem
- **Types** (`types.py`): Sistema de tipos da linguagem (Integer, Float, String, Boolean)

### 2. Compilador (Compiler/)

O compilador transforma o código em bytecode, que pode ser executado por uma máquina virtual:

```
Código Fonte → Lexer → Parser → AST → Compiler → Bytecode → VM
```

**Componentes:**
- **Compiler** (`compiler.py`): Gera bytecode a partir da AST
- **OpCodes** (`opcodes.py`): Define os códigos de operação da máquina virtual
- **Bytecode** (`bytecode.py`): Estrutura de dados para armazenar bytecode
- **Disassembler** (`disasembler.py`): Ferramenta para visualizar bytecode gerado

## Executando Programas

### Modo Interpretador (Execução Direta)

```bash
python mainInterpret.py
```

Este modo lê o arquivo `code.txt` e executa o código diretamente através do interpretador.

**Vantagens:**
- Execução imediata
- Mais fácil de depurar
- Mensagens de erro diretas

### Modo Compilador (Bytecode)

```bash
python mainBytecode.py
```

Este modo compila o código em `code.txt` para bytecode e exibe o resultado da compilação.

**Vantagens:**
- Visualização do bytecode gerado
- Compreensão do processo de compilação
- Base para implementação de VM no futuro

## Estrutura de um Programa

Um programa básico nesta linguagem tem a seguinte estrutura:

```
#{ Este é um comentário explicativo }#

x = 10;                    #{ Declaração de variável }#
y = 20;

resultado = x + y;         #{ Operação aritmética }#

if (resultado > 25) {      #{ Estrutura condicional }#
    print("Maior que 25");
} else {
    print("Menor ou igual a 25");
};

contador = 0;
while (contador < 5) {     #{ Laço de repetição }#
    print(contador);
    contador = contador + 1;
};
```

**Regras importantes:**
1. Todas as instruções devem terminar com ponto e vírgula (`;`)
2. Blocos de código são delimitados por chaves (`{ }`)
3. Comentários usam a sintaxe `#{ comentário }#`
4. Strings são definidas com aspas duplas (`"texto"`)

## Fluxo de Execução

### 1. Análise Léxica (Lexer)
O texto fonte é dividido em tokens (palavras-chave, identificadores, operadores, etc.)

### 2. Análise Sintática (Parser)
Os tokens são organizados em uma estrutura hierárquica (AST) que representa a sintaxe do programa

### 3. Execução/Compilação
- **Interpretador**: Percorre a AST executando cada nó
- **Compilador**: Percorre a AST gerando bytecode correspondente

## Próximos Passos

Para aprender mais sobre a linguagem, consulte:

- [**Tipos de Dados**](02-Tipos-de-Dados.md): Aprenda sobre os tipos primitivos
- [**Operadores**](03-Operadores.md): Conheça todos os operadores disponíveis
- [**Estruturas de Controle**](04-Estruturas-de-Controle.md): If-else e while
- [**Variáveis**](05-Variaveis.md): Como declarar e usar variáveis
- [**Exemplos Práticos**](06-Exemplos-Praticos.md): Programas completos demonstrativos
- [**Arquitetura do Compilador**](07-Arquitetura-Compilador.md): Detalhes técnicos do compilador
- [**Referência de Bytecode**](08-Referencia-Bytecode.md): Documentação dos opcodes
