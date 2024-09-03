from transformers import Trainer, TrainingArguments

from sentiment_analysis.config.core import config, TRAINED_MODEL
from sentiment_analysis.models import build_model
from sentiment_analysis.processing.data_handling import load_dataset
from sentiment_analysis.processing.data_processing import (
    label_encoding,
    tokennizor_dataset,
    split_dataset
)


def training_pipeline():
    dataset = label_encoding(load_dataset())
    tokennizor_ds = tokennizor_dataset(dataset)
    train_dataset, valid_dataset = split_dataset(tokennizor_ds)

    model = build_model(
        model_id=config.training_config.huggingface_model_id,
        num_label=config.training_config.num_labels
    )

    training_args = TrainingArguments(
        output_dir=f"{TRAINED_MODEL}/{config.training_config.output_dir}",
        eval_strategy=config.training_config.evaluation_strategy,
        learning_rate=config.training_config.learning_rate,
        per_device_train_batch_size=config.training_config.per_device_train_batch_size,
        per_device_eval_batch_size=config.training_config.per_device_eval_batch_size,
        num_train_epochs=config.training_config.num_train_epochs,
        weight_decay=config.training_config.weight_decay,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
    )

    trainer.train()


if __name__ == "__main__":
    training_pipeline()