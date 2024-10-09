import pandas as pd
from typing import List
# from topic_modeling.config.core import DATASET_DIR


DATASET_DIR = "/teamspace/studios/this_studio/nlp-hr-feedback/training_pipeline/topic_modeling/topic_modeling/datasets/"

def read_data_from_file(file_name: str = "training.jsonl", sep: str = "\t"):
    if not file_name:
        raise ValueError("The 'file_name' must be provided.")

    dataset_dir = DATASET_DIR + file_name

    # if not dataset_dir.exists():
    #     raise FileNotFoundError(f"File '{file_name}' does not exist in the directory '{DATASET_DIR}'.") 

    extension = file_name.split(".")[-1]
    if extension == "csv":
        df = pd.read_csv(str(dataset_dir), sep=sep)

    if extension == "jsonl":
        df = pd.read_json(str(dataset_dir), lines=True)

    return df


def delete_none_docs(docs: List = []):
    if len(docs) == 0:
        raise ValueError("The 'docs' list must be provided.")
         
    docs = [doc for doc in docs if doc != None]
    return docs


def df_to_dict(df: pd.DataFrame, name_col: str, count_col: str) -> dict:
    result_dict = df.set_index(name_col)[count_col].to_dict()
    return result_dict
