import main
import json
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS,LEVEL_OF_DIFFICULTY,TOPIC
class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def display_question(self, question_number):
        if 0 <= question_number < len(self.questions):
            question_data = self.questions[question_number]
            print(question_data["question"]) # Esta es una pregunta
            for option in question_data["options"]:
                print(option) # Estas son las diferentes opciones de la pregunta
            correct_answer = question_data["correct_answer"] # opcion correcta de la pregunta
            print(f"Correct Answer: {correct_answer}\n")
        else:
            print("Invalid question number.")

# Devuelve la respuesta de la ia en formato json
quiz_data = main.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)

#print(quiz_data)

quiz_data_dict=json.loads(quiz_data)
# crea el Quiz
quiz = Quiz(quiz_data_dict["questions"])

# Display all questions and options with correct answers
for i in range(len(quiz.questions)):
    quiz.display_question(i)