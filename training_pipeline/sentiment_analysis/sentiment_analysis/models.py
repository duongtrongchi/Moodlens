from transformers import (
    BertForSequenceClassification,
    BertTokenizer,
    Trainer,
    TrainingArguments,
    AdamW
)

from sentiment_analysis.config.core import config


def build_model(model_id, num_label):
    tokenizer = BertTokenizer.from_pretrained(model_id)
    model = BertForSequenceClassification.from_pretrained(model_id, num_labels=num_label)
    return tokenizer, model