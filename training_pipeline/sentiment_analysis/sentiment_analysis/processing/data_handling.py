from datasets import Dataset
from transformers import BertTokenizer


from sentiment_analysis import __version__
from sentiment_analysis.config.core import config, DATASET_DIR


def load_dataset(file_path=None):
    if not file_path:
        file_path = DATASET_DIR / "training.json"
    dataset = Dataset.from_json(file_path)

    return dataset


def load_tokenizer():
    tokenizer = BertTokenizer.from_pretrained(config.training_config.huggingface_model_id)
    return tokenizer


def save_dataset():
    pass