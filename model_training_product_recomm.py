import sqlite3
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')

# Carregar os dados da tabela 'transacoes'
data = pd.read_sql_query("SELECT * FROM transacoes", conn)

# Criar o objeto Reader para o Surprise
reader = Reader(rating_scale=(1, 5))

# Carregar os dados na estrutura de dados do Surprise
dataset = Dataset.load_from_df(data[['customer_name', 'product', 'price']], reader)

# Dividir os dados em conjunto de treinamento e teste
trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)

# Criar o modelo de filtragem colaborativa
model = SVD()

# Treinar o modelo
model.fit(trainset)

# Fazer previsões para o conjunto de teste
predictions = model.test(testset)

# Obter a lista de todos os clientes únicos
customer_names = data['customer_name'].unique()

# Gerar as recomendações para todos os clientes
recommendations_all = []
for customer_name in customer_names:
    # Obter os itens que o cliente ainda não comprou
    items_to_recommend = data.loc[~data['customer_name'].eq(customer_name), 'product'].unique()

    # Gerar as recomendações para o cliente
    recommendations = []
    for item in items_to_recommend:
        predicted_rating = model.predict(customer_name, item).est
        recommendations.append((item, predicted_rating))

    # Ordenar as recomendações por rating previsto
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Adicionar as recomendações do cliente à lista geral
    recommendations_all.append((customer_name, recommendations[:5]))  # Manter apenas as 5 principais recomendações

# Imprimir as recomendações para todos os clientes
for customer_name, recommendations in recommendations_all:
    print(f"Recomendações para o cliente {customer_name}:")
    for i, (item, rating) in enumerate(recommendations, start=1):
        print(f"{i}. Produto: {item} | Rating previsto: {rating}")
    print()

# Fechar a conexão com o banco de dados
conn.close()
