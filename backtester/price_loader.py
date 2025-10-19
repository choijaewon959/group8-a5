import os
import pandas as pd

def load_data():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    data_path = os.path.join(data_dir, "market_data.csv")

    data = pd.read_csv(data_path)
    return pd.Series(data['price'].values.ravel())
