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

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')
cursor = conn.cursor()

# Inserir os dados no banco de dados
for i in range(1000):
    transaction_id = i
    customer_name = fake.name()
    customer_address = fake.address().replace('\n', ', ')
    product = random.choice(produtos_jardim)
    quantity = int(fake.random_digit_not_null())
    price = float(fake.random_number(digits=4)) / 100
    date = str(fake.date_between(start_date='-1y', end_date='today'))
    sex = random.choice(['Masculino', 'Feminino'])

    cursor.execute('''
        INSERT INTO transacoes (transaction_id, customer_name, customer_address, product, quantity, price, date, sex)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (transaction_id, customer_name, customer_address, product, quantity, price, date, sex))

# Fazer commit das alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
