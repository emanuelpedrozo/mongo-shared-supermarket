import pymongo
import time
from pymongo import MongoClient
from random import randint, choice

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017")

# Selecionar o banco de dados e a coleção
db = client["estoque"]
collection = db["produtos"]

# Inserir dados simulados
def inserir_dados(num_filiais, num_produtos_por_filial):
    produtos = ["produto_" + str(i) for i in range(1000)]
    filiais = ["filial_" + str(i) for i in range(num_filiais)]

    for filial in filiais:
        for _ in range(num_produtos_por_filial):
            produto = {
                "filial": filial,
                "produto": choice(produtos),
                "quantidade": randint(1, 1000),
                "preco": round(randint(100, 10000) / 100, 2)
            }
            collection.insert_one(produto)

# Testar consultas
def testar_consultas():
    filiais = collection.distinct("filial")
    tempos = []

    for filial in filiais:
        inicio = time.time()
        produtos = list(collection.find({"filial": filial}))
        fim = time.time()
        tempos.append(fim - inicio)
        print(f"Consulta para {filial} retornou {len(produtos)} produtos em {fim - inicio:.4f} segundos")

    return tempos

# Testar atualizações
def testar_atualizacoes():
    filiais = collection.distinct("filial")
    tempos = []

    for filial in filiais:
        inicio = time.time()
        collection.update_many({"filial": filial}, {"$inc": {"quantidade": 10}})
        fim = time.time()
        tempos.append(fim - inicio)
        print(f"Atualização para {filial} completada em {fim - inicio:.4f} segundos")

    return tempos

# Mostrar distribuição dos dados
def mostrar_distribuicao():
    pipeline = [
        {"$group": {"_id": "$filial", "total_produtos": {"$sum": 1}}},
        {"$sort": {"total_produtos": -1}}
    ]
    distribuicao = list(collection.aggregate(pipeline))
    for filial in distribuicao:
        print(f"{filial['_id']}: {filial['total_produtos']} produtos")
    return distribuicao

if __name__ == "__main__":
    num_filiais = 5
    num_produtos_por_filial = 10000


    # Inserir dados simulados
    print("Inserindo dados simulados...")
    inserir_dados(num_filiais, num_produtos_por_filial)
    print("Dados inseridos.")

    # Testar consultas
    print("\nTestando consultas...")
    tempos_consultas = testar_consultas()

    # Testar atualizações
    print("\nTestando atualizações...")
    tempos_atualizacoes = testar_atualizacoes()

    # Mostrar distribuição dos dados
    print("\nDistribuição dos dados:")
    distribuicao_dados = mostrar_distribuicao()