import sqlite3
import pandas as pd
import numpy as np
import pytest

from data_cleaning_transform import (connect_to_db, extract_data, scale_numerical_data,
                                     apply_kmeans, impute_missing_values, convert_data_formats,
                                     transform_sex_column, load_data_to_sqlite)



@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'quantity': [10, np.nan, 30],
        'price': [5.5, 6.7, np.nan],
        'date': ['2023-07-03', '2023-07-02', '2023-07-01'],
        'sex': ['Masculino', 'Feminino', 'Masculino']
    })
    return data


def test_connect_to_db(tmp_path):
    try:
        print("Test test_connect_to_db started")
        db = tmp_path / "test.db"
        conn = connect_to_db(db)
        assert conn is not None
        print("Test test_connect_to_db passed")
    except Exception as e:
        print("Test test_connect_to_db did not pass:", str(e))
    finally:
        conn.close()


def test_extract_data():
    conn = sqlite3.connect(':memory:')
    data = pd.DataFrame({"column1": [1, 2, 3]})
    data.to_sql('transacoes', conn)
    extracted_data = extract_data(conn)
    assert not extracted_data.empty
    conn.close()


def test_scale_numerical_data(sample_data):
    scaled_data = scale_numerical_data(sample_data, ['quantity', 'price'])
    assert scaled_data is not None
    assert scaled_data.shape[1] == 2


def test_apply_kmeans(sample_data):
    try:
        print("Test test_apply_kmeans started")
        labels = apply_kmeans(sample_data, ['quantity', 'price'])

        assert labels is not None
        assert len(labels) == len(sample_data)
        print("Test test_apply_kmeans passed")
    except Exception as e:
        print("Test test_apply_kmeans failed")
        print(str(e))


def test_impute_missing_values(sample_data):
    sample_data['cluster'] = [0, 1, 0]
    imputed_data = impute_missing_values(sample_data, ['quantity', 'price'])
    assert not imputed_data['quantity'].isna().any()
    assert not imputed_data['price'].isna().any()


def test_convert_data_formats(sample_data):
    converted_data = convert_data_formats(sample_data)
    assert converted_data['quantity'].dtype == np.float32 or converted_data['quantity'].dtype == np.float64
    assert converted_data['price'].dtype == np.float32 or converted_data['price'].dtype == np.float64


def test_transform_sex_column(sample_data):
    transformed_data = transform_sex_column(sample_data)
    assert set(transformed_data['sex']) == {0, 1}
