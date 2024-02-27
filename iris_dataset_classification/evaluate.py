"""Evaluation script."""

import argparse
import json
from pathlib import Path

import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score


def evaluate(
    model_path: Path,
    test_dataset_path: Path,
    metrics_path: Path = None,
):
    """Evaluate model located at `model_path` on test data
    located at `test_dataset_path`."""

    model = load(model_path)
    test_data = pd.read_csv(test_dataset_path)
    X_test = test_data.drop("species", axis=1).values
    y_test = test_data["species"].values

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    metrics = {"accuracy": accuracy}

    # Saving metrics
    if metrics_path:
        metrics_path.write_text(json.dumps(metrics))


def main():
    """Main."""

    parser = argparse.ArgumentParser()
    parser.add_argument("model-path")
    parser.add_argument("--test-dataset-path")
    parser.add_argument("--metrics-path")

    args = parser.parse_args()
    evaluate(args.model_path, args.test_dataset_path, args.metrics_path)


if __name__ == "__main__":
    main()
