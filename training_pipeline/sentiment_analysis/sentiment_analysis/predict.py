import os

from transformers import pipeline

from sentiment_analysis.config.core import TRAINED_MODEL, config

def inference_model(model_path=None, user_input: list = []):
    if not model_path:
        model_path = str(TRAINED_MODEL / config.training_config.output_dir)

    if os.path.exists(model_path) and os.path.isdir(model_path):
        pipe = pipeline(model=model_path, task="sentiment-analysis")
        return pipe(user_input)
    else:
        raise FileNotFoundError(f"The folder '{model_path}' does not exist.")


print(inference_model(user_input=["I hate it"]))