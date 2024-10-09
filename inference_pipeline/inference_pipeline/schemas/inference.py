from pydantic import BaseModel
from typing import List

class SentimentAnalysisInput(BaseModel):
    prompt: str

class TopicModelInput(BaseModel):
    docs: List[str]