import requests
import json
import os
from g4f.client import Client
import time
import posicion
import generadorJson
import main
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS,LEVEL_OF_DIFFICULTY,TOPIC
client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": """Generate a trivia question about 
    geography and 3 possible answers. The response must only contain this 
    information in the next format: 
      { \"question\": \"content\", 
      \"first_answer\": \"content\", 
      \"second_answer\": \"content\", 
      \"third_answer\": \"content\", 
      \"correct_answer\": 0, 1, 2 }"""}
    ]
)

print(response.choices[0].message.content)

data = main.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)

quiz_data_dict=json.loads(data)

# Tomar la pregunta actual del conjunto de preguntas
question_data = quiz_data_dict["questions"][0]

    # Hacer la solicitud POST
response = requests.post(
        "https://api.creatomate.com/v1/renders",
        headers={
            'Authorization': 'Bearer 9c435d749d23460ea0b27611a122b4f9fc671b86d2c2012e9a71166f5e60d226794199805fdd225cc642df09154f5153',
            'Content-Type': 'application/json',
        },
        json=generadorJson.generar_json_data(NUMBER_OF_QUESTIONS,quiz_data_dict)
)

# time.sleep(60)

# def downloadfile(name,url):
#     name=name+".mp4"
#     r=requests.get('https://cdn.creatomate.com/renders/fbec7f72-2573-4685-bc8f-21d8ddadbc0e.mp4')
#     print ("****Connected****")
#     f=open(name,'wb');
#     print("Donloading.....")
#     for chunk in r.iter_content(chunk_size=255): 
#         if chunk: # filter out keep-alive new chunks
#             f.write(chunk)
#     print("Done")
#     f.close()

# downloadfile()