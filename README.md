# Sistema de Gerenciamento de Estoque de Supermercado

## Objetivo

Este projeto visa a criação de um sistema de gerenciamento de estoque para uma cadeia de supermercados com múltiplas filiais, utilizando um banco de dados distribuído para garantir escalabilidade e desempenho.

## Tecnologias Utilizadas

- Docker
- MongoDB
- Python

## Estrutura do Projeto

- `docker-compose.yml`: Arquivo de configuração do Docker Compose para montar o ambiente distribuído do MongoDB.
- `setup_sharding.js`: Script para configurar a fragmentação no MongoDB.
- `test_performance.py`: Script em Python para gerar dados simulados, inserir dados e realizar consultas para testes de desempenho.

## Passo a Passo para Configuração e Execução

### 1. Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.7+ instalado

### 2. Configuração do Ambiente

Clone o repositório:

```bash
git clone https://github.com/emanuelpedrozo/mongo-shared-supermarket.git
cd seu_repositorio

### 3. Levantando os Contêineres Docker

```bash
docker-compose up -d

### 4. Configuração de Sharding no MongoDB

```bash
docker exec -it mongo-router bash

Dentro do contêiner, abra o shell do Mongo:

```bash

mongo

Execute o script de configuração de sharding no shell do Mongo:

```javascript

sh.addShard("mongo1:27017")
sh.addShard("mongo2:27017")
sh.addShard("mongo3:27017")

sh.enableSharding("supermercado")

sh.shardCollection("supermercado.produtos", { "filial_id": 1 })







