from typing import List
from fastapi import APIRouter

from inference_pipeline.schemas.inference import SentimentAnalysisInput, TopicModelInput
from inference_pipeline.services.topic_modeling import predict_topic
from inference_pipeline.services.sentimet_analysis import classifier

router = APIRouter()


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