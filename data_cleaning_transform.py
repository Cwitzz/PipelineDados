import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('DBFIC.db')

# Etapa 1: Extração de Dados
data = pd.read_sql_query("SELECT * FROM transacoes", conn)

# Etapa 2: Identificar Valores Nulos
missing_data = data.isnull().sum()

# Etapa 3: Preparação de Dados para o K-means(Normalização)
numerical_features = ['quantity', 'price']  # lista das colunas numéricas
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numerical_features])

# Etapa 4: Aplicar K-means para Imputação
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(scaled_data)
data['cluster'] = kmeans.labels_

# Preenchendo os valores nulos com a média dos valores do cluster correspondente
imputer = SimpleImputer(strategy='mean')
data[numerical_features] = imputer.fit_transform(data.groupby('cluster')[numerical_features].transform(lambda x: x.fillna(x.mean())))

# Etapa 5: Correção de formatos de dados
# Converter 'quantity' para int
data['quantity'] = data['quantity'].astype(int)

# Converter 'price' para float
data['price'] = data['price'].astype(float)

# Converter 'date' para o formato padrão de data YYYY-MM-DD
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

# Etapa 6: Carregar os Dados Transformados de Volta ao SQLite

data.to_sql('transacoes_imputadas', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()
