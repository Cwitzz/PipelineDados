import unittest
from unittest.mock import patch
import pandas as pd
from model_training_product_recomm import *


class TestScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Executado uma vez antes de todos os testes
        cls.conn = connect_to_db(':memory:')
        cls.data = pd.DataFrame({
            'customer_name': ['John', 'Alice', 'Bob'],
            'product': ['A', 'B', 'C'],
            'cluster': [1, 2, 0],
            'sex': [1, 0, 1],
            'price': [10, 20, 30]
        })

        with cls.conn:
            cls.data.to_sql('transacoes_imputadas', cls.conn, index=False, if_exists='replace')

    def test_load_data(self):
        query = "SELECT * FROM transacoes_imputadas"
        result = load_data(self.conn, query)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)

    def test_encode_features(self):
        columns = ['customer_name', 'product']
        data_encoded, encoders = encode_features(self.data, columns)
        self.assertIsInstance(data_encoded, pd.DataFrame)
        self.assertEqual(len(encoders), 2)

    def test_train_model(self):
        X = self.data[['customer_name', 'product', 'cluster', 'sex']]
        y = self.data['price']
        model = train_model(X, y)
        self.assertIsNotNone(model)

    def test_validate_model(self):
        X = self.data[['customer_name', 'product', 'cluster', 'sex']]
        y = self.data['price']
        model = train_model(X, y)
        X_test = X.sample(frac=0.2, random_state=42)
        y_test = y.sample(frac=0.2, random_state=42)
        mse = validate_model(model, X_test, y_test)
        self.assertIsInstance(mse, float)

    @patch('model_training_product_recomm.generate_recommendations')
    @patch('model_training_product_recomm.insert_recommendations_to_table')
    @patch('model_training_product_recomm.joblib.dump')
    def test_main(self, mock_dump, mock_insert, mock_generate):
        mock_generate.return_value = [('John', [('A', 10), ('B', 20)]), ('Alice', [('C', 30)])]
        main()
        self.assertTrue(mock_generate.called)
        self.assertTrue(mock_insert.called)
        self.assertTrue(mock_dump.called)


if __name__ == '__main__':
    unittest.main()
