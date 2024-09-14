import os
import pandas as pd

from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from umap import UMAP

from topic_modeling.config.core import config
from topic_modeling.processing.data_handling import read_data_from_file
from topic_modeling.processing.data_processing import delete_none_docs
from topic_modeling.training_pipeline import get_embeddings, train_bert_topic_model, train_umap


df = read_data_from_file(config.bert_topic_config.training_dataset_name)

docs = df.text.to_list()
docs = delete_none_docs(docs)

corpus_embeddings = get_embeddings(docs=docs)
reduced_embeddings = train_umap(corpus_embeddings)
model = train_bert_topic_model(docs, corpus_embeddings)

