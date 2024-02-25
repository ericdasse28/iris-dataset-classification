"""Data preparation script."""

import argparse
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def prepare(path_to_iris_data: Path) -> pd.DataFrame:
    """Prepare data."""

    iris_data = pd.read_csv(path_to_iris_data, header=None)

    # Column names were missing. Add them for better understandability
    iris_data.columns = [
        "sepal_length_cm",
        "sepal_width_cm",
        "petal_width_cm",
        "petal_length_cm",
        "species",
    ]

    # Turn target variable into integer
    encoder = LabelEncoder()
    iris_data["species"] = encoder.fit_transform(iris_data["species"])

    return iris_data


def main():
    """Main."""

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-d", "--destination-path")
    args = parser.parse_args()

    iris_data = prepare(args.filename)
    iris_data.to_csv(args.destination_path)


if __name__ == "__main__":
    main()
