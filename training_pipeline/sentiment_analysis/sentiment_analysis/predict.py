from transformers import pipeline

from sentiment_analysis.config.core import TRAINED_MODEL, config

def inference_model(model_path=None, user_input: list = []):
    if not model_path:
        model_path = str(TRAINED_MODEL / config.training_config.output_dir)

    pipe = pipeline(model=model_path, task="sentiment-analysis")
    return pipe(user_input)


print(inference_model(user_input=["I hate it"]))