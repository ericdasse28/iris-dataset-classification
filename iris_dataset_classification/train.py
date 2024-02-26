"""Train script."""

import argparse
from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.linear_model import LogisticRegression


def train(prepared_dataset_path: Path, model_path: Path):
    """Train dataset located at dataset_path."""

    iris_data = pd.read_csv(prepared_dataset_path)
    X = iris_data.drop(["species"], axis=1).values
    y = iris_data["species"].values

    linear_regressor = LogisticRegression(solver="liblinear")
    trained_model = linear_regressor.fit(X, y)

    dump(trained_model, model_path)


def main():
    """Training main."""

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "dataset")
    parser.add_argument("model-path")

    args = parser.parse_args()
    train(args.dataset, args.model_path)


if __name__ == "__main__":
    main()
