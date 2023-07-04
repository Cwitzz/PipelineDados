import sqlite3
import pandas as pd
import joblib
import logging
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

logging.basicConfig(level=logging.INFO)


def connect_to_db(db_name):
    return sqlite3.connect(db_name)


def load_data(conn, query):
    return pd.read_sql_query(query, conn)


def train_model(X_train, y_train, n_estimators=100):
    model = RandomForestRegressor(n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return model


def validate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    logging.info(f'Mean Squared Error: {mse}')
    return mse


def generate_recommendations(model, data, top_n=5):
    recommendations_all = []
    unique_customers = data['customer_name'].unique()
    unique_products = data['product'].unique()

    for customer_name in unique_customers:
        recommendations = []
        customer_data = data[data['customer_name'] == customer_name].iloc[0]
        cluster = customer_data['cluster']
        sex = customer_data['sex']

        for product in unique_products:
            features = [customer_name, product, cluster, sex]
            predicted_rating = model.predict([features])[0]
            recommendations.append((product, predicted_rating))

        recommendations.sort(key=lambda x: x[1], reverse=True)
        recommendations_all.append((customer_name, recommendations[:top_n]))

    return recommendations_all


def main():
    # Marca o tempo de início
    start_time = time.time()

    conn = connect_to_db('DBFIC.db')
    data = load_data(conn, "SELECT * FROM transacoes_imputadas")

    X = data[['customer_name', 'product', 'cluster', 'sex']]
    y = data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train, n_estimators=100)
    validate_model(model, X_test, y_test)

    recommendations = generate_recommendations(model, data)

    for customer_name, recs in recommendations:
        logging.info(f"Recomendações para o cliente {customer_name}:")
        for i, (item, rating) in enumerate(recs, start=1):
            logging.info(f"{i}. Produto: {item} | Rating previsto: {rating}")

    joblib.dump(model, 'trained_model.pkl')

    conn.close()

    # Marca o tempo de finalização e calcula a duração
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Tempo de execução: {elapsed_time} segundos")


if __name__ == "__main__":
    main()
