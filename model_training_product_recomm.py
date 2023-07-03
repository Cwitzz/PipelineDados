import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')

# Carregar os dados da tabela 'transacoes'
data = pd.read_sql_query("SELECT * FROM transacoes", conn)

# Codificação de labels para os nomes de clientes e produtos
# Basicamente transformando nomes dos clientes e produtos em números para facilitar o aprendizado de máquina
customer_encoder = LabelEncoder()  # Criando as variáveis para os nomes já codificados
product_encoder = LabelEncoder()
data['customer_name'] = customer_encoder.fit_transform(data['customer_name'])  # Atribuindo as novas variáveis aos
data['product'] = product_encoder.fit_transform(data['product'])              # respectivos

# Dividir os dados em conjunto de treinamento e teste
# O modelo de treinamento é cartesiano, as características são nome do cliente e produto
# O que eu quero prever é o preço
X = data[['customer_name', 'product']]
y = data['price']
# test size 0.2 significa que 20% dos dados serão usados para o teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Criar o modelo de regressão usando RandomForest
model = RandomForestRegressor()

# Treina o modelo
model.fit(X_train, y_train)

# Fazer previsões para o conjunto de teste
predictions = model.predict(X_test)

# Gerar recomendações para todos os clientes
recommendations_all = []
unique_customers = customer_encoder.classes_   # usando esse metodo .classes_ obtemos o codigo de cada cliente
unique_products = product_encoder.classes_      # Mesma coisa do comentário up


# Loop para cada nome de cliente em unique_customers , para cada um a variavel encoded_customer_name recebe
# o valor codificado do nome do cliente usando o transform
for customer_name in unique_customers:
    encoded_customer_name = customer_encoder.transform([customer_name])[0]
    recommendations = []
    # Usando o modelo treinado para prever o rating de cada cliente para determinados produtos
    # Passando o cliente codificado e o produito codificado como entry
    # A previsão é armazenada em predicted_rating
    for product in unique_products:
        encoded_product = product_encoder.transform([product])[0]
        predicted_rating = model.predict([[encoded_customer_name, encoded_product]])[0]
        # Adc uma tupla ctd nome do produto e rating previsto à var recommmendations
        recommendations.append((product, predicted_rating))

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
