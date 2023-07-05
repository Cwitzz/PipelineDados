import sqlite3

# Modularizando a função


def insert_recommendations_to_table(recommendations):
    conn = sqlite3.connect('DBFIC.db')
    cursor = conn.cursor()

    for customer_name, recs in recommendations:
        for product, rating in recs:
            cursor.execute("INSERT INTO recomendacoes (customer_name, product, rating) VALUES (?, ?, ?)",
                           (customer_name, product, rating))

    conn.commit()
    conn.close()
