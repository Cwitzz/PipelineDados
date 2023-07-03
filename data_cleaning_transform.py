import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def connect_to_db(db_name):
    return sqlite3.connect(db_name)


def extract_data(conn):
    return pd.read_sql_query("SELECT * FROM transacoes", conn)


def scale_numerical_data(data, numerical_features):
    scaler = StandardScaler()
    return scaler.fit_transform(data[numerical_features])


def apply_kmeans(scaled_data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0).fit(scaled_data)
    return kmeans.labels_


def impute_missing_values(data, numerical_features):
    imputer = SimpleImputer(strategy='mean')
    return imputer.fit_transform(data.groupby('cluster')[numerical_features].transform(lambda x: x.fillna(x.mean())))


def convert_data_formats(data):
    data['quantity'] = data['quantity'].astype(int)
    data['price'] = data['price'].astype(float)
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    return data


def transform_sex_column(data):
    data['sex'] = data['sex'].map({'male': 0, 'female': 1})
    return data


def load_data_to_sqlite(data, conn):
    data.to_sql('transacoes_imputadas', conn, if_exists='replace', index=False)


def main():
    conn = connect_to_db('DBFIC.db')
    data = extract_data(conn)
    numerical_features = ['quantity', 'price']

    scaled_data = scale_numerical_data(data, numerical_features)
    data['cluster'] = apply_kmeans(scaled_data)

    data[numerical_features] = impute_missing_values(data, numerical_features)
    data = convert_data_formats(data)
    data = transform_sex_column(data)

    load_data_to_sqlite(data, conn)

    conn.close()


if __name__ == "__main__":
    main()
