from transformers import pipeline
import torch

from inference_pipeline.config.core import config


model_name = config.sentiment_analysis_config.huggingface_model_id
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
classifier = pipeline(config.sentiment_analysis_config.task, model=model_name)
