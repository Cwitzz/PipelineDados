import sqlite3
from faker import Faker
import random

# Criar dados fictícios
fake = Faker()
produtos_jardim = [
    "Vaso de flores",
    "Substrato para plantas",
    "Sementes de flores",
    "Sementes de hortaliças",
    "Ferramentas de jardinagem",
    "Regador",
    "Mangueira de jardim",
    "Adubo orgânico",
    "Adubo químico",
    "Fertilizante para plantas",
    "Vasos autoirrigáveis",
    "Estufa para mudas",
    "Luvas de jardinagem",
    "Tesoura de poda",
    "Pá de jardinagem",
    "Rastelo de jardinagem",
    "Pulverizador",
    "Fio de jardinagem",
    "Estacas para plantas",
    "Rede de proteção para frutas"
]

data = [{
    "transaction_id": i,
    "customer_name": fake.name(),
    "customer_address": fake.address().replace('\n', ', '),
    "product": random.choice(produtos_jardim),
    "quantity": int(fake.random_digit_not_null()),
    "price": float(fake.random_number(digits=4)) / 100,
    "date": str(fake.date_between(start_date='-1y', end_date='today')),
    "sex": random.choice(['Masculino', 'Feminino'])
} for i in range(1000)]


# Conectar ao banco de dados SQLite
# Nota: substitua 'DBFIC.db' pelo nome do seu arquivo de banco de dados
conn = sqlite3.connect('DBFIC.db')
cursor = conn.cursor()

# Inserir os dados no banco de dados
for item in data:
    cursor.execute('''
        INSERT INTO transacoes (transaction_id, customer_name, customer_address, product, quantity, price, date, sexo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (item['transaction_id'], item['customer_name'], item['customer_address'], item['product'], item['quantity'], item['price'], item['date'], item['sex']))

# Fazer commit das alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
