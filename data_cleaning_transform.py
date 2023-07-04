import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np


def connect_to_db(db_name):
    return sqlite3.connect(db_name)


def extract_data(conn):
    return pd.read_sql_query("SELECT * FROM transacoes", conn)


def scale_numerical_data(data, numerical_features):
    scaler = StandardScaler()
    return scaler.fit_transform(data[numerical_features])


def impute_missing_values(data, numerical_features):
    imputer = SimpleImputer(strategy='mean')
    data[numerical_features] = imputer.fit_transform(data[numerical_features])
    return data


def apply_kmeans(data, numerical_features, n_clusters=3):
    # Garantir que os valores NaN são imputados antes de aplicar KMeans
    imputed_data = impute_missing_values(data, numerical_features)
    scaled_data = scale_numerical_data(imputed_data, numerical_features)
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0).fit(scaled_data)
    return kmeans.labels_


def convert_data_formats(data):
    # Convertendo 'quantity' para float em vez de int para acomodar NaNs
    data['quantity'] = data['quantity'].astype(float)
    data['price'] = data['price'].astype(float).round(2)  # Round price to 2 decimal places
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    return data


def transform_sex_column(data):
    # Check the unique values in 'sex' column
    print("Unique values in 'sex' column before transformation: ", data['sex'].unique())

    # Map 'Masculino' to 0 and 'Feminino' to 1, leave NaN as NaN
    data['sex'] = data['sex'].map({'Masculino': 0, 'Feminino': 1, np.nan: np.nan})

    # Check the unique values in 'sex' column after transformation
    print("Unique values in 'sex' column after transformation: ", data['sex'].unique())

    return data


def load_data_to_sqlite(data, conn):
    print("Data to be loaded to SQLite:")
    print(data.head())

    data.to_sql('transacoes_imputadas', conn, if_exists='replace', index=False)


def main():
    conn = connect_to_db('DBFIC.db')
    data = extract_data(conn)
    numerical_features = ['quantity', 'price']
    data['cluster'] = apply_kmeans(data, numerical_features)
    data = convert_data_formats(data)
    data = transform_sex_column(data)

    load_data_to_sqlite(data, conn)

    conn.close()


if __name__ == "__main__":
    main()
