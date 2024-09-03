from transformers import BertTokenizer

from datasets import Dataset

from sentiment_analysis import __version__
from sentiment_analysis.config.core import config, DATASET_DIR


# def load_dataset(file_path="/Users/duongtrongchi/engineering/project/nlp-hr-feedback/training_pipeline/sentiment_analysis/sentiment_analysis/datasets/training.jsonl"):
#     if not file_path:
#         file_path = str(DATASET_DIR / config.training_config.training_dataset_name)

#     print(file_path)
#     dataset = Dataset.from_json(file_path)

#     return dataset

def load_dataset(file_path=None):
    if file_path == None:
        file_path = str(DATASET_DIR / config.training_config.training_dataset_name)
    print("FILE PATH: ", file_path)
    dataset = Dataset.from_json(file_path)

    return dataset

def load_tokenizer():
    tokenizer = BertTokenizer.from_pretrained(config.training_config.huggingface_model_id)
    return tokenizer


def save_dataset():
    pass