import requests
import json
import os
from g4f.client import Client
import time
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

question_data=quiz_data_dict["questions"][0]

json = {
  "template_id": "ca083e1e-8095-4a18-b4cd-2004eb41ddd3",
  "modifications": {
    "Music": "https://creatomate.com/files/assets/b5dc815e-dcc9-4c62-9405-f94913936bf5",
    "4e31b834-08c3-4a7e-88d0-bbb69d38a00a": "https://creatomate.com/files/assets/4a6f6b28-bb42-4987-8eca-7ee36b347ee7",
    "Pregunta": question_data["question"],
    "Opcion_1": question_data["options"][0],
    "Opcion_2": question_data["options"][1],
    "Opcion_3": question_data["options"][2],
    "859e205a-8a69-41ac-b2ff-bacce9de1c2f": "https://creatomate.com/files/assets/4a6f6b28-bb42-4987-8eca-7ee36b347ee7",
    "Text-2": "Use any video automation tool to replace these text and background assets with your own! 😊",
    "Background-3": "https://creatomate.com/files/assets/4f6963a5-7286-450b-bc64-f87a3a1d8964",
    "Text-3": "Learn how to get started on the Guides & Tutorials page on Creatomate's home page.",
    "Background-4": "https://creatomate.com/files/assets/36899eae-a128-43e6-9e97-f2076f54ea18",
    "Text-4": "Use the template editor to completely customize this video to meet your own needs. 🚀"
  }
}

response = requests.post(
    "https://api.creatomate.com/v1/renders",
    headers={
  'Authorization': 'Bearer 9c435d749d23460ea0b27611a122b4f9fc671b86d2c2012e9a71166f5e60d226794199805fdd225cc642df09154f5153',
  'Content-Type': 'application/json',
 },
 json=json
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