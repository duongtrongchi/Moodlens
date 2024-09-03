from datasets import Dataset
from torch.utils.data import DataLoader

from sentiment_analysis.config.core import config
from sentiment_analysis.processing.data_handling import load_tokenizer


def label_encoding(dataset):
    def label_to_index(example):
        label2index = {"Positive": 1, "Negative": 0}
        example['label'] = label2index[example['label']]
        return example

    dataset = dataset.map(label_to_index)
    return dataset


def tokennizor_dataset(dataset):
    tokenizer = load_tokenizer()

    def tokenize_function(examples):
        return tokenizer(str(examples['text']), padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function)
    return tokenized_datasets


def split_dataset(tokenized_datasets):
    if not tokenized_datasets:
        pass

    train_testvalid = tokenized_datasets.train_test_split(test_size=0.2)
    train_dataset = train_testvalid['train']
    valid_dataset = train_testvalid['test']

    # train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=8)
    # valid_dataloader = DataLoader(valid_dataset, batch_size=8)

    return train_dataset, valid_dataset