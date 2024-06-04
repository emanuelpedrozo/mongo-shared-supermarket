from pymongo import MongoClient
import random
import string
import time

def generate_data(n):
    data = []
    for _ in range(n):
        item = {
            "filial_id": random.randint(1, 10),
            "produto_id": ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            "nome": ''.join(random.choices(string.ascii_letters, k=10)),
            "quantidade": random.randint(1, 1000),
            "preco": round(random.uniform(1, 100), 2)
        }
        data.append(item)
    return data

def main():
    client = MongoClient("mongodb://localhost:27021")
    db = client.supermercado
    collection = db.produtos

    # Gerar dados simulados
    print("Gerando dados simulados...")
    data = generate_data(100000)
    
    # Inserção de dados
    print("Inserindo dados...")
    start_time = time.time()
    collection.insert_many(data)
    end_time = time.time()
    print(f"Tempo de inserção: {end_time - start_time} segundos")

    # Consultas de teste
    print("Consultando dados...")
    start_time = time.time()
    for _ in range(1000):
        filial_id = random.randint(1, 10)
        collection.find_one({"filial_id": filial_id})
    end_time = time.time()
    print(f"Tempo de consulta: {end_time - start_time} segundos")

if __name__ == "__main__":
    main()