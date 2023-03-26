import pandas as pd


def load_data(csv_path):
    loaded_dataframe = pd.read_csv(csv_path)
    return loaded_dataframe
