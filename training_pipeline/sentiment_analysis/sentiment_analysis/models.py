from transformers import (
    BertForSequenceClassification,
    BertTokenizer
)

from sentiment_analysis.config.core import config


def build_model(model_id: str = None, num_label: int = None):
    """
    Builds and returns a pre-trained BERT model for sequence classification.

    Args:
        model_id (str, optional): The identifier of the pre-trained model from HuggingFace's model hub.
                                  Defaults to the value specified in the config file if not provided.
        num_label (int, optional): The number of labels for classification. Defaults to the value
                                   specified in the config file if not provided.

    Returns:
        BertForSequenceClassification: A BERT model configured for sequence classification.
    """

    if not model_id:
        model_id = config.training_config.huggingface_model_id

    if not num_label:
        num_label = config.training_config.num_labels

    model = BertForSequenceClassification.from_pretrained(model_id, num_labels=num_label)
    return model
