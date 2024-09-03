from transformers import Trainer, TrainingArguments


from sentiment_analysis.models import build_model
from sentiment_analysis.processing.data_handling import load_dataset
from sentiment_analysis.processing.data_processing import (
    label_encoding,
    tokennizor_dataset,
    split_dataset
)


dataset = label_encoding(load_dataset())
tokennizor_ds = tokennizor_dataset(dataset)
train_dataset, valid_dataset = split_dataset(tokennizor_ds)

tokenizer, model = build_model()

training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
)

trainer.train()