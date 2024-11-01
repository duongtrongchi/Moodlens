import mlflow
from transformers import Trainer, TrainingArguments, pipeline

from sentiment_analysis.config.core import config, TRAINED_MODEL
from sentiment_analysis.metrics import compute_metrics
from sentiment_analysis.models import build_model
from sentiment_analysis.processing.data_handling import load_dataset, load_tokenizer
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
    tokenizer = load_tokenizer()

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
        compute_metrics=compute_metrics
    )

    mlflow.set_experiment("Employees Classifier Training")
    with mlflow.start_run() as run:
        trainer.train()
        trainer.evaluate()

    tuned_pipeline = pipeline(
        task="text-classification",
        model=trainer.model,
        batch_size=8,
        tokenizer=tokenizer,
        device="cpu",
    )

    model_config = {"batch_size": 8}

    # Infer the model signature, including a representative input, the expected output, and the parameters that we would like to be able to override at inference time.
    signature = mlflow.models.infer_signature(
        ["This is a test!", "And this is also a test."],
        mlflow.transformers.generate_signature_output(
            tuned_pipeline, ["This is a test response!", "So is this."]
        ),
        params=model_config,
    )


    with mlflow.start_run(run_id=run.info.run_id):
        model_info = mlflow.transformers.log_model(
            transformers_model=tuned_pipeline,
            artifact_path="fine_tuned",
            signature=signature,
            input_example=["Pass in a string", "And have it mark as spam or not."],
            model_config=model_config,
        )

    model.save_pretrained(f"{TRAINED_MODEL}/{config.training_config.output_dir}")
    tokenizer.save_pretrained(f"{TRAINED_MODEL}/{config.training_config.output_dir}")


if __name__ == "__main__":
    training_pipeline()