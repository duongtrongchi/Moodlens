from pathlib import Path
from strictyaml import load, YAML

from pydantic import BaseModel

import sentiment_analysis



PACKAGE_ROOT = Path(sentiment_analysis.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL = PACKAGE_ROOT / "trained_models"
CONFIG_PATH = PACKAGE_ROOT / "config.yml"


# print("PACKAGE_ROOT:", PACKAGE_ROOT)
# print("ROOT:", ROOT)
# print("DATA DIR: ", DATASET_DIR)
# print("TRAINED MODEL: ", TRAINED_MODEL)
# print("CONFIG_PATH: ", CONFIG_PATH)

class AppConfig(BaseModel):
    package_name: str


class TrainingConfig(BaseModel):
    huggingface_model_id: str
    training_dataset_name: str
    test_dataset_name: str
    padding: str
    truncation: bool
    shuffle: bool
    batch_zise: int
    num_labels: int
    output_dir: str
    evaluation_strategy: str
    learning_rate: float
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    num_train_epochs: int
    weight_decay: float


class Config(BaseModel):
    app_config: AppConfig
    training_config: TrainingConfig


def fetch_config_from_yml(cfg=None):
    if not cfg:
        cfg = CONFIG_PATH

    with open(cfg, 'r') as f:
        config_att = load(f.read())

    return config_att


def create_and_validate_config(parser_config=None):
    if not parser_config:
        parser_config = fetch_config_from_yml()

    _config = Config(
        app_config=parser_config.data,
        training_config=parser_config.data["training_config"]
    )
    return _config



config = create_and_validate_config()
print(config)

