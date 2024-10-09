from typing import List
from bertopic import BERTopic

from inference_pipeline.services.utils import delete_none_docs, df_to_dict
from inference_pipeline.config.core import config


MODEL_PATH = config.topic_model_config.trained_path
model = BERTopic.load(MODEL_PATH)

def predict_topic(docs: List['str']):
    docs = delete_none_docs(docs)[:500]

    topics, probabilities = model.fit_transform(docs)
    df = model.get_topic_info()

    temp_df = df.copy()
    results = df_to_dict(temp_df, "Name", "Count")

    return results


