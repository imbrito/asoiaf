# A Song of Ice and Fire

API A Song of Ice and Fire interactions.

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
├── app.py
├── docker-compose.yml
├── engine.py
├── exceptions.py
├── requirements.txt
├── tests
│   ├── test_app.py
│   ├── test_engine.py
│   └── test_version.py
└── version.py
```

## Desafio

Desenvolvimento de uma REST API, a qual deverá contar com dois endpoints, um para cadastrar novas interações entre personagens e outro para consultar amigos em comum.

**a**: ​Criar endpoint para adicionar novas interações entre personagens
Você deve criar um endpoint **​HTTP POST /interaction**​, o qual receberá como parâmetro um JSON​ com a interação entre 2 personagens, com o formato que segue:

POST -> /interaction

```json
{
    "source"​: ​"Nome do Personagem 1"​,
    "target"​: ​"Nome do Personagem 2"​,
    "weight"​: ​"Número de interações entre os dois personagens em 1 determinado livro"​,
    "book"​: ​"Número do livro da saga onde houve a interação" 
}
```

É necessário que a sua API filtre as chamadas e aceite ​somente​ interações do​ 4o​ livro da série. Se o registro for guardado com sucesso, o ​status code​ ​201​ deverá ser retornado.

**b**: ​Criar endpoint para consultar amigos em comum
O segundo endpoint a ser construído é o **​HTTP GET /common-friends**​, o qual receberá obrigatoriamente​ 2 parâmetros, com o formato:

GET -> /common-friends?source=NOME_DO_P1&target=NOME_DO_P2 onde:

- P1​ se refere ao personagem 1
- P2​ se refere ao personagem 2

Como resposta em caso de sucesso, a API deverá retornar o ​status code ​200 seguido da lista de amigos em comum entre os dois personagens, respeitando o seguinte formato:

```json
{
    "common_friends"​: [
        "Cersei-Lannister"​,​"Arya-Stark"
    ]
}
```

Se 2 personagens ​não possuem amigos em comum, uma lista ​vazia deve ser retornada, seguindo o formato da resposta apresentado acima.
Além disso, ​não​ deverá haver distinção de caixa alta/baixa para consulta dos amigos em comum.

## Como executar

```bash
make test
make start
make clean
```

Command List:

| command | description                              |
|---------|------------------------------------------|
|  build  | build a docker compose services          |
|  start  | start a docker compose services          |
|  stop   | stop a docker compose services           |
|  test   | run unit tests                           |
|  clean  | clean a docker compose services          |
