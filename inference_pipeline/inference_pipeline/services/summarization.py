import google.generativeai as genai
from typing import List
import json


def initialize_summarization_model(gemini_api_key, system_prompt: str, model_name: str = "gemini-1.5-flash"):
    genai.configure(api_key=gemini_api_key)
    model=genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt,
        generation_config={"response_mime_type": "application/json"},
    )
    return model


def summarize_employee_reviews(model, reviews: List['str']):
    try:
        response = model.generate_content(reviews)
        return json.loads(response.text)
    except Exception as e:
        return {
            "Error": "Function is under maintenance!"
        }