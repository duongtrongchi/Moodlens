from pydantic import BaseModel


class TextGenerationInput(BaseModel):
    prompt: str