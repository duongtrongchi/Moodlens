from pathlib import Path
from strictyaml import load
from pydantic import BaseModel

import topic_modeling


PACKAGE_ROOT = Path(topic_modeling.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
DATASET_DIR = PACKAGE_ROOT / "datasets"
CONFIG_FILE = PACKAGE_ROOT / "config.yml"


class AppConfig(BaseModel):
    version_model: str


class BertTopicConfig(BaseModel):
    training_dataset_name: str
    evaluation_dataset_name: str
    sentence_transformers_model_id: str
    language: str
    stop_words_language: str


class UmapConfig(BaseModel):
    n_neighbors: int
    n_components: int
    min_dist: float
    metric: str


class Config(BaseModel):
    # app_config: AppConfig
    bert_topic_config: BertTopicConfig
    umap_config: UmapConfig


def fetch_data_from_yaml(file_path = None):
    if not file_path:
        file_path = CONFIG_FILE

    with open(file_path, "r") as f:
        config_att = load(f.read())

    return config_att


def create_and_validate_config(parser_config = None):
    if not parser_config:
        parser_config = fetch_data_from_yaml()

    _config = Config(
        bert_topic_config=parser_config.data["bert_topic_config"],
        umap_config=parser_config.data["umap_config"]
    )

    return _config


config = create_and_validate_config()



