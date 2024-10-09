from strictyaml import load
from pathlib import Path
from pydantic import BaseModel

import inference_pipeline


PACKAGE_ROOT = Path(inference_pipeline.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_YML = PACKAGE_ROOT / "config.yml"
ENV_PATH = PACKAGE_ROOT / ".env"

class SentimentAnalysisConfig(BaseModel):
    huggingface_model_id: str
    trained_model_path: str
    task: str


class TopicModelConfig(BaseModel):
    trained_path: str


class Config(BaseModel):
    sentiment_analysis_config: SentimentAnalysisConfig
    topic_model_config: TopicModelConfig


def fetch_config_from_yml(config_path=None):
    if not config_path:
        config_path = CONFIG_YML

    with open(config_path, 'r') as f:
        config_att = load(f.read())

    return config_att


def create_and_validate_config(parser_config=None):
    if not parser_config:
        parser_config = fetch_config_from_yml()

    _config = Config(
        sentiment_analysis_config=parser_config.data.get("sentiment_analysis"),
        topic_model_config=parser_config.data.get("topic_modeling"),
    )
    return _config

config = create_and_validate_config()
