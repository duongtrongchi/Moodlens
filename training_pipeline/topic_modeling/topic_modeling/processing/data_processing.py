import pandas as pd 

from strictyaml import load
from typing import List

from topic_modeling.config.core import DATASET_DIR, CONFIG_FILE


def delete_none_docs(docs: List = None):
    if not docs:
        raise ValueError("The 'docs' list must be provided.")
         
    docs = [doc for doc in docs if doc != None]
    return docs
