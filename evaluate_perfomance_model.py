import sqlite3
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Carregar o modelo treinado e os encoders
model = joblib.load('trained_model.pkl')
customer_encoder = joblib.load('customer_encoder.pkl')
product_encoder = joblib.load('product_encoder.pkl')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')

# Carregar os dados da tabela 'transacoes'
data = pd.read_sql_query("SELECT * FROM transacoes_imputadas", conn)

# Codificação de labels para os nomes de clientes e produtos usando os encoders carregados
data['customer_name'] = customer_encoder.transform(data['customer_name'])
data['product'] = product_encoder.transform(data['product'])

# Dividir os dados em conjunto de treinamento e teste
X = data[['customer_name', 'product', 'cluster', 'sex']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fazer previsões para o conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Imprimir métricas de avaliação
print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')
print(f'R-squared (R2): {r2}')

# Fechar a conexão com o banco de dados
conn.close()
