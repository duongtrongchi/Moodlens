from fastapi import APIRouter
from inference_pipeline.models.huggingface_model import classifier
from inference_pipeline.schemas.inference import TextGenerationInput


router = APIRouter()


@router.post("/generate/")
async def generate_text(input_data: TextGenerationInput):
    try:
        
        generated_text = classifier(input_data.prompt)
        
        return {"generated_text": generated_text}
    
    except Exception as e:
        return {"error": str(e)}