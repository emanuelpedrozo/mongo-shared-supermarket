# Sistema de Gerenciamento de Estoque de Supermercado

## Objetivo

Este projeto visa a criação de um sistema de gerenciamento de estoque para uma cadeia de supermercados com múltiplas filiais, utilizando um banco de dados distribuído para garantir escalabilidade e desempenho.

## Tecnologias Utilizadas

- Docker
- MongoDB
- Python

## Estrutura do Projeto

- `docker-compose.yml`: Arquivo de configuração do Docker Compose para montar o ambiente distribuído do MongoDB.
- `mongo-config-server-cnfg.js`: SScript para configurar o servidor do Mongo.
- `mongo-shard01-cnfg.js`: Script para configurar o shard1.
- `mongo-shard02-cnfg.js`: Script para configurar o shard2.
- `mongo-shard03-cnfg.js`: Script para configurar o shard3.
- `test_performance.py`: Script em Python para gerar dados simulados, inserir dados e realizar consultas para testes de desempenho.

## Passo a Passo para Configuração e Execução

### 1. Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.7+ instalado

### 2. Configuração do Ambiente

Criação de uma rede para a comunicação entre os containers 

```bash
docker network create mongo-shard
```

Clone o repositório:

```bash
git clone https://github.com/emanuelpedrozo/mongo-shared-supermarket.git
cd seu_repositorio
```

### 3. Levantando os Contêineres Docker

```bash
docker-compose up -d
```

### 4. Configuração do mongo de um dos containers dos ConfigServes

```bash
docker exec -it mongo-config01 mongosh
```

Execute o script de configuração de sharding no shell do Mongo:

```javascript

rs.initiate(
   {
      _id: "configserver",
      configsvr: true,
      version: 1,
      members: [
         { _id: 0, host : "mongo-config01:27017" },
         { _id: 1, host : "mongo-config02:27017" },
         { _id: 2, host : "mongo-config03:27017" }
      ]
   }
)
```

### 5. Configuração de todos os shards

Shard1

```bash
docker exec -it mongo-shard1a mongosh --port 27018
```

Execute o script de configuração de sharding no shell do Mongo:

```javascript

rs.initiate(
   {
      _id: "shard01",
      version: 1,
      members: [
         { _id: 0, host : "mongo-shard1a:27018" },
         { _id: 1, host : "mongo-shard1b:27018" },
      ]
   }
)
```

Shard2

```bash
docker exec -it mongo-shard2a mongosh --port 27019
```

Execute o script de configuração de sharding no shell do Mongo:

```javascript

rs.initiate(
   {
      _id: "shard02",
      version: 1,
      members: [
         { _id: 0, host : "mongo-shard2a:27019" },
         { _id: 1, host : "mongo-shard2b:27019" },
      ]
   }
)
```

Shard3

```bash
docker exec -it mongo-shard3a mongosh --port 27020
```

Execute o script de configuração de sharding no shell do Mongo:

```javascript

rs.initiate(
   {
      _id: "shard03",
      version: 1,
      members: [
         { _id: 0, host : "mongo-shard3a:27020" },
         { _id: 1, host : "mongo-shard3b:27020" },
      ]
   }
)
```

### 6. Iniciar o serviço do roteador e configurar o roteador para que conheça os shards disponíveis.

Iniciando o serviço do roteador

```bash
docker run -p 27017:27017 --name mongo-router --net mongo-shard -d mongo mongos --port 27017 --configdb configserver/mongo-config01:27017,mongo-config02:27017,mongo-config03:27017 --bind_ip_all
```

Configurando o roteador para que conheça os shards disponíveis.

```bash
docker exec -it mongo-router mongo
sh.addShard("shard01/mongo-shard1a:27018")
sh.addShard("shard01/mongo-shard1b:27018") 
sh.addShard("shard02/mongo-shard2a:27019")
sh.addShard("shard02/mongo-shard2b:27019") 
sh.addShard("shard03/mongo-shard3a:27020")
sh.addShard("shard03/mongo-shard3b:27020")
```

### 7. Gerar Dados Simulados e Executar Testes de Desempenho

Saia do contêiner do mongo-router e execute o script Python para gerar dados e realizar testes de desempenho:

```bash
python test_performance.py
```

### 6. Resultados

O script test_performance.py exibirá o tempo necessário para inserção e consultas de dados, avaliando a eficácia da estratégia de particionamento.


![Imagem do pyhton](https://github.com/emanuelpedrozo/mongo-shared-supermarket/blob/main/imagem_script_pyton.JPG?raw=true)











