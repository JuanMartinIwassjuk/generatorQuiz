import openai
import json
from config import API_KEY, MODEL_NAME
def get_openai_response_in_json_format(number_of_questions, number_of_options, difficulty_level, topic):
    
    openai.api_key = API_KEY

    model = MODEL_NAME

    prompt = f"generate {number_of_questions} specific questions with a difficulty level of {difficulty_level} about the topic {topic}"

    messages = [
        {'role': 'system', 'content': f'have {number_of_options} options for each question, including the correct answer, and your response in JSON format like this:openkey "questions": [ openkey "question": "Sample question?", "options": ["Option A", "Option B", "Option C"], "correct_answer": "Option A" closedkey ] closedkey'},
        {'role': 'user', 'content': prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.4 # Nivel de creatividad, el más alto es 1 que podría llegar a ser menos preciso
    )

    json_response = response["choices"][0]["message"]["content"]



    return json_response

    