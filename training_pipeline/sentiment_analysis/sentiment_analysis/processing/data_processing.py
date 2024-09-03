from datasets import Dataset

from sentiment_analysis.config.core import config
from sentiment_analysis.processing.data_handling import load_tokenizer


def label_encoding(dataset):
    """
    Encodes the labels of the dataset into numerical format for training.

    Args:
        dataset (Dataset): The input dataset containing text and label fields.

    Returns:
        Dataset: The dataset with labels encoded as integers.
    """
    def label_to_index(example):
        """
        Converts string labels to numerical format.

        Args:
            example (dict): A single data example containing text and label fields.

        Returns:
            dict: The data example with the label converted to an integer.
        """
        label2index = {"Positive": 1, "Negative": 0}
        example['label'] = label2index[example['label']]
        return example

    dataset = dataset.map(label_to_index)
    return dataset


def tokennizor_dataset(dataset):
    """
    Tokenizes the dataset using a pre-defined tokenizer.

    Args:
        dataset (Dataset): The input dataset to be tokenized.

    Returns:
        Dataset: The tokenized dataset with padding and truncation applied.
    """
    tokenizer = load_tokenizer()

    def tokenize_function(examples):
        """
        Tokenizes a single example in the dataset.

        Args:
            examples (dict): A single data example containing text.

        Returns:
            dict: The tokenized data example.
        """
        return tokenizer(
            str(examples['text']),
            padding=config.training_config.padding,
            truncation=config.training_config.truncation
        )

    tokenized_datasets = dataset.map(tokenize_function)
    return tokenized_datasets


def split_dataset(tokenized_datasets):
    """
    Splits the tokenized dataset into training and validation sets.

    Args:
        tokenized_datasets (Dataset): The tokenized dataset to split.

    Returns:
        Tuple[Dataset, Dataset]: A tuple containing the training and validation datasets.
    """
    if not tokenized_datasets:
        pass

    train_testvalid = tokenized_datasets.train_test_split(test_size=0.2)
    train_dataset = train_testvalid['train']
    valid_dataset = train_testvalid['test']

    return train_dataset, valid_dataset



