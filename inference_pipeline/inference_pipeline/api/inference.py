import os
from dotenv import load_dotenv

from typing import List
from fastapi import APIRouter

from inference_pipeline.schemas.inference import SentimentAnalysisInput, TopicModelInput
from inference_pipeline.services.topic_modeling import predict_topic
from inference_pipeline.services.sentimet_analysis import classifier
from inference_pipeline.services.summarization import initialize_summarization_model, summarize_employee_reviews
from inference_pipeline.services.utils import SYSTEM_PROMPT
from inference_pipeline.config.core import ENV_PATH


router = APIRouter()
load_dotenv(dotenv_path=ENV_PATH)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@router.post("/sentiment-analysis/")
async def generate_text(input_data: SentimentAnalysisInput):
    try:
        generated_text = classifier(input_data.prompt)
        return {"generated_text": generated_text}
    except Exception as e:
        return {"error": str(e)}


@router.post("/predict-topic/")
async def generate_topic(input_data: TopicModelInput):
    try:
        data = predict_topic(input_data.docs)
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}


@router.post("/summarize-employee-reviews/")
async def summarize_reviews(reviews: List[str]):
    try:
        model = initialize_summarization_model(GOOGLE_API_KEY, SYSTEM_PROMPT)
        result = summarize_employee_reviews(model, reviews)
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}