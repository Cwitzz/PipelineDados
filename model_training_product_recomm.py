import sqlite3
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')

# Carregar os dados da tabela 'transacoes'
data = pd.read_sql_query("SELECT * FROM transacoes", conn)

# Codificação de labels para os nomes de clientes e produtos
customer_encoder = LabelEncoder()
product_encoder = LabelEncoder()
data['customer_name'] = customer_encoder.fit_transform(data['customer_name'])
data['product'] = product_encoder.fit_transform(data['product'])

# Dividir os dados em conjunto de treinamento e teste
X = data[['customer_name', 'product']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de regressão usando RandomForest
model = RandomForestRegressor()

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões para o conjunto de teste
predictions = model.predict(X_test)

# Gerar recomendações para todos os clientes
recommendations_all = []
unique_customers = customer_encoder.classes_
unique_products = product_encoder.classes_

for customer_name in unique_customers:
    encoded_customer_name = customer_encoder.transform([customer_name])[0]
    recommendations = []
    for product in unique_products:
        encoded_product = product_encoder.transform([product])[0]
        predicted_rating = model.predict([[encoded_customer_name, encoded_product]])[0]
        recommendations.append((product, predicted_rating))

    # Ordenar as recomendações por rating previsto
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Adicionar as recomendações do cliente à lista geral
    recommendations_all.append((customer_name, recommendations[:5]))

# Imprimir as recomendações para todos os clientes
for customer_name, recommendations in recommendations_all:
    print(f"Recomendações para o cliente {customer_name}:")
    for i, (item, rating) in enumerate(recommendations, start=1):
        print(f"{i}. Produto: {item} | Rating previsto: {rating}")
    print()

# Salvar o modelo treinado e os encoders em arquivos
joblib.dump(model, 'trained_model.pkl')
joblib.dump(customer_encoder, 'customer_encoder.pkl')
joblib.dump(product_encoder, 'product_encoder.pkl')

# Fechar a conexão com o banco de dados
conn.close()
