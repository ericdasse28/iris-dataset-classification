import pandas as pd
import pytest


@pytest.fixture
def iris_dataframe_1():
    return pd.DataFrame(
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
