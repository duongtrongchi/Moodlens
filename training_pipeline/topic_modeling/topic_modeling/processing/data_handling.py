import pandas as pd

from topic_modeling.config.core import DATASET_DIR


def read_data_from_file(file_name: str = None, sep: str = "\t"):
    if not file_name:
        raise ValueError("The 'file_name' must be provided.")

    dataset_dir = DATASET_DIR / file_name

    if not dataset_dir.exists():
        raise FileNotFoundError(f"File '{file_name}' does not exist in the directory '{DATASET_DIR}'.") 

    extension = file_name.split(".")[-1]
    if extension == "csv":
        df = pd.read_csv(str(dataset_dir), sep=sep)

    if extension == "jsonl":
        df = pd.read_json(str(dataset_dir), lines=True)

    return df