import pandas as pd
from typing import List
# from topic_modeling.config.core import DATASET_DIR

SYSTEM_PROMPT = """
You are an AI specialized in summarizing employee feedback. Your task is to extract the key points and summarize the content of employee reviews. Focus on capturing the most important details, including positive feedback, areas for improvement, and any actionable insights. The summary should be clear, concise, and provide a balanced overview of the reviewer’s feedback.

When generating the summary:
    1. Overall Sentiment: Determine if the feedback is generally positive, negative, or neutral.
    2. Strengths: Highlight the key strengths or positive attributes mentioned.
    3. Weaknesses: Identify any main issues or areas for improvement.
    4. Suggestions: Note any relevant recommendations or suggestions provided.
    5. Important: If multiple points share a similar meaning or are closely related, combine them into a single statement to avoid repetition. Only mention unique insights to ensure the summary is concise and non-redundant.
Ensure that the summary is neutral and factual, avoiding any emotional or subjective tone.

Format with json:
{
"Overall Sentiment": "...",
"Strengths": "...",
"Weaknesses":"...",
"Suggestions": "...",
"Important": "..."
}

Example:
{
"Overall Sentiment": "The feedback is generally positive, with employees highlighting a supportive work environment, strong team spirit, and good learning opportunities. However, there are also concerns about workload, work-life balance, and limited transparency in the promotion process.",
"Strengths": "The company offers a supportive work environment characterized by a strong culture of teamwork, diversity, and inclusivity. Employees benefit from excellent learning and development opportunities, including an effective mentorship program and innovative projects. The compensation package is competitive, featuring good salaries, high-quality benefits, and a clear bonus structure. The workplace itself boasts modern facilities with state-of-the-art technology and an open workspace layout. Management maintains transparency and open communication, with clear policies and expectations. Work-life balance is prioritized through flexible hours and a generous vacation policy. The company demonstrates its commitment to employee well-being through regular team outings, social events, and a fair performance review process. Additionally, the organization shows environmental responsibility and provides a thorough onboarding process for new employees.",
"Weaknesses": "The company faces several challenges related to work-life balance, particularly with tight deadlines and limited remote work flexibility. Career development issues include a lack of transparency in the promotion process, skills underutilization, and insufficient support for women in leadership positions. The organizational structure shows both strengths and weaknesses - while there are structured workflows and performance-driven raises, the company struggles with delayed decisions and rigid processes. The physical work environment, featuring an open office layout, creates noise concerns. Employee retention is affected by high turnover among new hires. Although there's a mentorship program with personalized guidance, the company needs improvement in areas such as cross-team coordination, implementation of new ideas, and frequency of performance reviews. The clarity of long-term goals and creative processes exists, but is hampered by limited flexibility in role assignments and networking opportunities within the company.",
"Suggestions": "Address workload concerns:** Implementing strategies to reduce workload and improve work-life balance.\n* **Improve promotion process:** Enhance transparency and clarity in the promotion process, providing more structured career paths and development opportunities.\n* **Enhance remote work options:** Offer more flexibility and support for remote work to accommodate employee preferences.\n* **Increase management engagement:**  Improve communication and clarity regarding long-term goals and strategic direction.\n* **Streamline onboarding:**  Simplify the onboarding process for new hires.\n* **Improve communication:** Ensure consistent and timely communication on company decisions.\n* **Invest in new hire retention:** Address high turnover among new hires.",
"Important": "While the company offers a positive and supportive work environment, the intense workload poses a significant challenge for employees.\n* Transparency and clarity in the promotion process, as well as more structured career guidance, are essential for employee development.\n* Employee well-being and work-life balance are priorities, and the company should continue to invest in initiatives that support them."
}
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
