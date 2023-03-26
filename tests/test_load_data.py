import os
import pandas as pd
import pytest

from load_data import load_data


def test_load_data_should_return_a_dataframe_from_a_csv_file():
    expected_dataframe = pd.DataFrame(
        {
            "sepal_length_cm": [5.1, 4.9, 4.7, 7.0, 6.5],
            "sepal_width_cm": [3.5, 3.0, 3.2, 3.2, 3.0],
            "petal_length_cm": [1.4, 1.4, 1.3, 4.7, 5.5],
            "petal_width_cm": [0.2, 0.2, 0.2, 1.4, 1.8],
            "species": [
                "Iris-setosa",
                "Iris-setosa",
                "Iris-setosa",
                "Iris-versicolor",
                "Iris-virginica",
            ],
        }
    )
    csv_path = "tests/data/iris_data_test.csv"

    loaded_data = pd.read_csv(csv_path)

    assert isinstance(loaded_data, pd.DataFrame)
    assert all(loaded_data.columns == expected_dataframe.columns)
    assert loaded_data.equals(expected_dataframe)
