# Microsoft Learn Studies

> Repositório com exercícios e códigos desenvolvidos durante os estudos dos módulos de Python na plataforma Microsoft Learn.

## 📋 Sobre o Projeto

Este projeto contém uma coleção de programas em Python desenvolvidos como parte dos estudos na Microsoft Learn. Os códigos incluem exercícios práticos dos módulos oficiais (operações numéricas, listas, funções, biblioteca padrão), jogos e programas interativos (chute o número, roleta-russa, jogo de cartas), além de exemplos de programação orientada a objetos (classes, herança, encapsulamento, composição e associação).

## 📁 Estrutura do Projeto

### Módulos Microsoft Learn

#### `python-standart-library/`
- **exercise1.py** — Uso de módulos da biblioteca padrão (ex.: `random` com alias)

#### `python-numeric-operations/`
- **Exercise1.py** — Funções `type()` e `isinstance()` para verificação de tipos
- **Exercise2.py** — Exercício de operações numéricas
- **Exercise3.py** — Exercício de operações numéricas
- **challenge1.py** — Desafio do módulo de operações numéricas
- **challenge2.py** — Desafio do módulo de operações numéricas

#### `python-lists/`
- **exercise1.py** — Indexação, fatiamento (slices) e manipulação de listas
- **exercise2.py** — Exercício de listas
- **jogoDeCartas.py** — Jogo de cartas usando listas
- **SolutionChallenge1.py** — Solução do desafio de listas

#### `python-functions/`
- **exercise1.py** — Funções, parâmetros opcionais e retorno de valores
- **exercise2.py** — Exercício de funções
- **exercise3.py** — Exercício de funções
- **challenge.py** — Desafio de processamento de listas (usa `processor.py`)
- **processor.py** — Módulo com `process_numbers()` e `process_names()` para o desafio
- **deck.py** — Funções relacionadas a baralho de cartas

### Programas e scripts na raiz

- **chute-numero.py** / **chute-numero2.py** — Jogo “adivinhe o número” com laço e entrada do usuário
- **roleta-russa.py** — Jogo de roleta-russa
- **yasmin.py** — Script pessoal
- **test2.py** — Script de teste
- **exercise1.py** — Exercício de Python na raiz
- **Farenheint1.py** — Conversão ou uso de Fahrenheit
- **Calculadora.py** — Programa de calculadora

### Programação orientada a objetos (Aulas 35–44)

- **Classes - Aula 35/** — Introdução a classes (`Pessoa`, `main.py`)
- **Atributos da Classe - Aula 39/** — Atributos de classe e instância
- **Métodos de Classe - Aula 36/** — Métodos de classe
- **Métodos Estáticos - Aula 37/** — Métodos estáticos
- **Property - Getters e Setters - Aula 38/** — Propriedades e encapsulamento
- **Encapsulamento - Aula 40/** — Encapsulamento
- **Associação - Aula 41/** — Associação entre classes
- **Agregação - Aula 42/** — Agregação
- **Composição - Aula 43/** — Composição
- **Herança Simples - Aula 44/** — Herança simples

## 📂 Estrutura do repositório

```
LICENSE
README.md
python-standart-library/
  exercise1.py          # módulo random e alias
python-numeric-operations/
  Exercise1.py          # type() e isinstance()
  Exercise2.py
  Exercise3.py
  challenge1.py
  challenge2.py
python-lists/
  exercise1.py          # listas, índices e slices
  exercise2.py
  jogoDeCartas.py
  SolutionChallenge1.py
python-functions/
  exercise1.py          # funções e parâmetros
  exercise2.py
  exercise3.py
  challenge.py          # desafio (usa processor.py)
  processor.py          # process_numbers, process_names
  deck.py
Classes - Aula 35/      # POO: classes
Atributos da Classe - Aula 39/
Métodos de Classe - Aula 36/
Métodos Estáticos - Aula 37/
Property - Getters e Setters - Aula 38/
Encapsulamento - Aula 40/
Associação - Aula 41/
Agregação - Aula 42/
Composição - Aula 43/
Herança Simples - Aula 44/
chute-numero.py         # jogo adivinhe o número
chute-numero2.py
roleta-russa.py
yasmin.py
test2.py
exercise1.py
Farenheint1.py
Calculadora.py
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** — Linguagem de programação
- **Microsoft Learn** — Plataforma de estudos e módulos
- Módulos da biblioteca padrão: `random`, entre outros

## 📝 Funcionalidades Principais

### Módulos Microsoft Learn
- Verificação de tipos com `type()` e `isinstance()`
- Operações numéricas e expressões booleanas
- Listas: indexação, fatiamento, métodos e iteração
- Funções: definição, parâmetros opcionais, retorno de valores e listas
- Uso de módulos da biblioteca padrão (ex.: `random`)

### Jogos e programas interativos
- **Chute o número** — Laço com entrada do usuário até acertar
- **Roleta-russa** — Jogo de sorte
- **Jogo de cartas** — Manipulação de listas e lógica de jogo

### Orientação a objetos
- Classes, atributos e métodos (instância, classe e estáticos)
- Property, getters e setters
- Encapsulamento, associação, agregação, composição e herança simples

## 🚀 Como Executar

### Pré-requisitos
- Python 3 instalado ([python.org](https://www.python.org/downloads/))

### Via terminal (Linux / macOS / Windows)

```bash
# Na raiz do projeto, executar um script:
python chute-numero.py

# Módulos Microsoft Learn (exemplos):
python python-standart-library/exercise1.py
python python-numeric-operations/Exercise1.py
python python-lists/exercise1.py
python python-functions/exercise1.py
python python-functions/challenge.py

# POO (exemplo – Aula 35):
python "Classes - Aula 35/main.py"
```

### Executar dentro de uma pasta
```bash
cd "Classes - Aula 35"
python main.py
```

## 📚 Conteúdos Abordados

- ✅ Tipos de dados e verificação com `type()` e `isinstance()`
- ✅ Entrada e saída (input, print, f-strings)
- ✅ Estruturas condicionais (if/else)
- ✅ Laços (for, while)
- ✅ Listas: criação, índices, slices e métodos
- ✅ Funções: parâmetros, valores default e retorno
- ✅ Módulos e importação (incluindo alias)
- ✅ Classes e objetos
- ✅ Atributos e métodos (instância, classe, estáticos)
- ✅ Encapsulamento, properties, getters e setters
- ✅ Associação, agregação, composição e herança

## ⚙️ Como funciona

### Jogo “Chute o número”
1. O programa sorteia um número (ex.: entre 1 e 5).
2. O usuário digita palpites até acertar.
3. Ao final, é exibido em quantas tentativas acertou.

### Desafio `python-functions` (processor)
1. `challenge.py` importa o módulo `processor`.
2. Chama `process_numbers()` e `process_names()` com uma lista mista.
3. `process_numbers()` filtra valores numéricos (incluindo strings numéricas), converte, ordena e retorna; se a entrada não for lista, retorna lista vazia.
4. `process_names()` filtra strings não numéricas, ordena e retorna.

### Módulos de POO (Aulas 35–44)
- Cada pasta corresponde a um conceito (Classes, Herança, etc.).
- Em geral há `main.py` (ou similar) que importa classes de outro arquivo (ex.: `pessoa.py`, `classes.py`) e demonstra o uso.

## 📄 Licença

Este projeto está licenciado sob a MIT License — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📖 Referências

- [Microsoft Learn — Python](https://learn.microsoft.com/pt-br/training/paths/beginner-python/) — Trilhas e módulos de Python
- Código-fonte em `*.py` — exemplos práticos de programação em Python
- Estrutura e organização disponíveis neste repositório

---

### Hashtags
#Python #MicrosoftLearn #Programming #LearningToCode #OpenSource #GitHub #CodeExamples #BeginnerProgramming #OOP #ObjectOrientedProgramming #Lists #Functions #StandardLibrary

### Meta Keywords
```
Python, Microsoft Learn, programação, exercícios Python, listas, funções,
biblioteca padrão, POO, orientação a objetos, classes, herança, encapsulamento,
jogos em Python, código exemplo, aprender programação, código aberto
```
