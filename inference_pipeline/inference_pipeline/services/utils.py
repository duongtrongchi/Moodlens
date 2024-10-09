import pandas as pd
from typing import List
# from topic_modeling.config.core import DATASET_DIR

SYSTEM_PROMPT = """
You are an AI specialized in summarizing employee feedback. Your task is to extract the key points and summarize the content of employee reviews. Focus on capturing the most important details, including positive feedback, areas for improvement, and any actionable insights. The summary should be clear, concise, and provide a balanced overview of the reviewer’s feedback.

When generating the summary:
    1. Overall Sentiment: Determine if the feedback is generally positive, negative, or neutral.
    2. Strengths: Highlight the key strengths or positive attributes mentioned.
    3. Weaknesses or Challenges: Identify any main issues or areas for improvement.
    4. Suggestions or Actions: Note any relevant recommendations or suggestions provided.
    5. Important: If multiple points share a similar meaning or are closely related, combine them into a single statement to avoid repetition. Only mention unique insights to ensure the summary is concise and non-redundant.
Ensure that the summary is neutral and factual, avoiding any emotional or subjective tone.
"""


DATASET_DIR = "/teamspace/studios/this_studio/nlp-hr-feedback/training_pipeline/topic_modeling/topic_modeling/datasets/"

def read_data_from_file(file_name: str = "training.jsonl", sep: str = "\t"):
    if not file_name:
        raise ValueError("The 'file_name' must be provided.")

    dataset_dir = DATASET_DIR + file_name

    # if not dataset_dir.exists():
    #     raise FileNotFoundError(f"File '{file_name}' does not exist in the directory '{DATASET_DIR}'.") 

    extension = file_name.split(".")[-1]
    if extension == "csv":
        df = pd.read_csv(str(dataset_dir), sep=sep)

    if extension == "jsonl":
        df = pd.read_json(str(dataset_dir), lines=True)

    return df


def delete_none_docs(docs: List = []):
    if len(docs) == 0:
        raise ValueError("The 'docs' list must be provided.")
         
    docs = [doc for doc in docs if doc != None]
    return docs


def df_to_dict(df: pd.DataFrame, name_col: str, count_col: str) -> dict:
    result_dict = df.set_index(name_col)[count_col].to_dict()
    return result_dict
