import sqlite3
from faker import Faker

# Criar dados fictícios
fake = Faker()
data = [{
    "transaction_id": i,
    "customer_name": fake.name(),
    "customer_address": fake.address().replace('\n', ', '),
    "product": fake.word(ext_word_list=None),
    "quantity": int(fake.random_digit_not_null()),
    "price": float(fake.random_number(digits=4)) / 100,
    "date": str(fake.date_between(start_date='-1y', end_date='today'))
} for i in range(1000)]

# Conectar ao banco de dados SQLite
# Nota: substitua 'meu_banco_de_dados.db' pelo nome do seu arquivo de banco de dados
conn = sqlite3.connect('DBFIC.db')
cursor = conn.cursor()

# Inserir os dados no banco de dados
for item in data:
    cursor.execute('''
        INSERT INTO transacoes (transaction_id, customer_name, customer_address, product, quantity, price, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (item['transaction_id'], item['customer_name'], item['customer_address'], item['product'], item['quantity'], item['price'], item['date']))

# Fazer commit das alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
