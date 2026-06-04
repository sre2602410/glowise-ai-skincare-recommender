import os
import pandas as pd
from src.preprocessing import load_data, preprocess_dataframe

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATASET_FILES = [
    "sephora_products.csv",
    "cosmetics.csv",
    "skincare_products.csv",
]


def load_all_datasets(data_dir=None):
    """
    Loads and merges all available skincare datasets into one unified catalog.
    Each file is preprocessed before merge so column schemas align correctly.
    """
    data_dir = data_dir or DATA_DIR
    frames = []

    for filename in DATASET_FILES:
        path = os.path.join(data_dir, filename)
        if not os.path.exists(path):
            continue
        raw = load_data(path)
        if raw is None or raw.empty:
            continue
        df = preprocess_dataframe(raw.copy())
        df["source_dataset"] = filename.replace(".csv", "")
        frames.append(df)

    if not frames:
        return None

    combined = pd.concat(frames, ignore_index=True)
    combined = combined.drop_duplicates(subset=["product_name", "brand"], keep="first")
    return combined.reset_index(drop=True)
