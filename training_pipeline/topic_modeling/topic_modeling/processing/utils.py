from bertopic import BERTopic

from topic_modeling.config.core import TRAINED_MODEL


def load_bert_topic_model(model_id: str = None):
    model_path = TRAINED_MODEL / model_id

    if not model_id:
        raise ValueError("The 'model_id' must be provided.")

    if not model_path.exists():
        raise FileNotFoundError(f"File '{model_path}' does not exist in the directory '{TRAINED_MODEL}'.")

    loaded_model = BERTopic.load(model_path)
    return loaded_model


def save_bert_topic_model(model, model_id):
    if not model_id:
        raise ValueError("The 'model_id' must be provided.")

    print(f"Model saved at {str(TRAINED_MODEL / model_id)}")

    model.save(str(TRAINED_MODEL / model_id), serialization="pickle")