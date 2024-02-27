"""Data preparation script."""

import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
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


def split_into_train_and_test(iris_data):

    train_dataset, test_dataset = train_test_split(
        iris_data, test_size=0.33, random_state=4
    )
    return train_dataset, test_dataset


def main():
    """Main."""

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-d", "--destination-folder")
    args = parser.parse_args()

    iris_data = prepare(args.filename)
    # Split into train and test dataset
    train_dataset, test_dataset = split_into_train_and_test(iris_data)

    destination_folder = Path(args.destination_folder)
    train_dataset.to_csv(destination_folder / "train.csv", index=False)
    test_dataset.to_csv(destination_folder / "test.csv", index=False)


if __name__ == "__main__":
    main()
