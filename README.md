# Sistema de Gerenciamento de Estoque Distribuído

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
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
