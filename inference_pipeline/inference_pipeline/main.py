import uvicorn
from fastapi import FastAPI

from inference_pipeline.api.inference import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "LLM Inference API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)