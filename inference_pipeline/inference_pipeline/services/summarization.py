import google.generativeai as genai


def initialize_summarization_model(gemini_api_key, system_prompt: str, model_name: str = "gemini-1.5-flash"):
    genai.configure(api_key=gemini_api_key)
    model=genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt
    )
    return model


def summarize_employee_reviews(model, reviews):
    response = model.generate_content(reviews)
    return response.text