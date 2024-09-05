from transformers import BertTokenizer, pipeline, BertForSequenceClassification

from datasets import Dataset

from sentiment_analysis import __version__
from sentiment_analysis.config.core import config, DATASET_DIR, TRAINED_MODEL


def load_dataset(file_path=None):
    if file_path == None:
        file_path = str(DATASET_DIR / config.training_config.training_dataset_name)

    dataset = Dataset.from_json(file_path)
    return dataset


def load_tokenizer(tokenizer_id=None):
    if not tokenizer_id:
        tokenizer_id = config.training_config.huggingface_model_id

    tokenizer = BertTokenizer.from_pretrained(tokenizer_id)
    return tokenizer


def save_dataset():
    pass


