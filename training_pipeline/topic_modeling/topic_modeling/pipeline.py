from typing import List
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from umap import UMAP
from bertopic import BERTopic

from topic_modeling.config.core import config, TRAINED_MODEL


def get_embeddings(embedding_model_id: str = None, docs: List = None):
    if not embedding_model_id:
        embedding_model_id = config.bert_topic_config.sentence_transformers_model_id
    
    if not docs:
        raise  ValueError("The 'docs' must be provided.")

    model_embedding = SentenceTransformer(embedding_model_id)
    corpus_embeddings = model_embedding.encode(docs)
    return corpus_embeddings


def train_bert_topic_model(docs, corpus_embeddings):
    vectorizer_model = CountVectorizer(stop_words=config.bert_topic_config.stop_words_language)
    model = BERTopic(
        language=config.bert_topic_config.language,
        n_gram_range=(1, 2),
        vectorizer_model=vectorizer_model,
        ).fit(docs, corpus_embeddings)

    return model


def train_umap(corpus_embeddings):
    reduced_embeddings = UMAP(
        n_neighbors=config.umap_config.n_neighbors, 
        n_components=config.umap_config.n_components, 
        min_dist=config.umap_config.min_dist, 
        metric=config.umap_config.metric).fit_transform(corpus_embeddings)
    return reduced_embeddings






