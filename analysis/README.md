# A Song of Ice and Fire

PySpark analysis A Song of Ice and Fire tasks.

## Dependências

- docker
- python
- make
- pyenv (local development)

## Arquitetura de Código

```bash
.
├── Dockerfile
├── Makefile
├── README.md
├── __init__.py
├── asoiaf.py
├── data
│   ├── input
│   │   └── dataset.csv
│   └── output
│       ├── challenge1.csv
│       └── challenge2.csv
├── engine.py
├── main.py
├── requirements.txt
└── tests
    ├── test_asoiaf.py
    ├── test_engine.py
    └── test_main.py
```

## Desafio

O objetivo destes desafios é analisar redes de interação entre os personagens dos livros da saga As Crônicas de Gelo e Fogo (A Song of Ice and Fire), escritos por George R. R. Martin.

Todos os registros da lista de interações do arquivo de entrada tem o formato `{​Personagem​1​, P​ ersonagem​2​, P​eso​, ​Livro​}`.

- O campo ​Peso corresponde ao número de interações entre dois personagens em um dado livro.
- O campo ​Livro indica a qual livro da saga aquele registro se refere. No arquivo enviado para o seu e-mail, esse campo pode receber valores 1, 2 ou 3.
- Uma conexão entre dois personagens (​Personagem​1 e ​Personagem​2)​ é dada por um registro que começa com (​Personagem​1,​ ​Personagem​2)​ e tem um ​Peso maior que 0.

1. Você deverá criar um código que, para cada personagem, compute o número de interações em cada um dos três primeiros livros da série e a soma das interações. A saída será uma lista com linhas no formato: `p​<TAB>​i​1​,i​2​,i​​3​,s​`

   - p​ é o nome do personagem
   - i​1 ​é o número de interações no livro 1
   - i​2​ é o número de interações no livro 2
   - i​3 ​é o número de interações no livro 3
   - s​ é a soma das interações nos três livros

    Na saída, os personagens devem estar ordenados de forma decrescente pelo valor de ​s​. Não imprima espaços nem antes nem depois do caractere TAB.

2. Dados dois personagens ​p​1 e ​p​2,​ um personagem ​p​3 é dito ser um amigo em comum entre ​p​1 e ​p​2 caso ​p​3​ interaja com ​p​1​ e também com ​p​2.​ Para completar o desafio 2 você deverá computar o número de amigos em comum entre dois personagens. Caso um par de personagens não tenha amigos em comum, então não deverá ser colocado na lista. Observe que os dois personagens não precisam interagir entre si para terem amigos em comum.
A saída será uma lista em que cada linha está no formato: `p​1​​<TAB>p​2​​<TAB>a​1​,a​​2​,...,a​n`

   - p​1 ​é o primeiro personagem
   - p​2​ é o segundo personagem
   - p​1​ e​ ​p​2​ possuem ​n​ >​ ​ 0​ ​ a​migos em comum
   - a​i​ é​ o ​i​-ésimo amigo em comum entre ​p​1​ e​ ​p​ ​2,​ com 1 ≤ ​i ​≤ ​n​;

    A lista de saída como um todo não precisará estar em nenhuma ordem pré-definida. Não imprima espaços nem antes nem depois dos caracteres TAB.

## Como executar

```bash
make create 
make test
make run
make clean
```

Command List:

| command | description                              |
|---------|------------------------------------------|
|  build  | build a docker image                     |
|  create | build and create docker container        |
|  start  | start a docker container                 |
|  stop   | stop a docker container                  |
|  test   | run unit tests                           |
|  run    | run tasks: wordcount and blackfriday     |
|  clean  | clean a docker image and container       |
