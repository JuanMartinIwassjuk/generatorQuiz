import json
import requests
import audio
import time
import functions_videos
import os
from pathlib import Path
import generatorQuiz
from creatomate import Animation, Image, Element, Composition, Source, Video, Audio
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC,BACKGROUND_IMG,AUTORIZACION


background_list_dict = json.loads(BACKGROUND_IMG)

data = '{ "questions": [ { "question": "Who is known as The King in the NBA?", "options": [ "LeBron James", "Kobe Bryant", "Stephen Curry" ], "correct_answer": "LeBron James" }, { "question": "Which team has won the most NBA championships?", "options": [ "Boston Celtics", "Los Angeles Lakers", "Chicago Bulls" ], "correct_answer": "Boston Celtics" }, { "question": "Which player holds the record for the most points scored in a single NBA game?", "options": [ "Wilt Chamberlain", "Michael Jordan", "Kobe Bryant" ], "correct_answer": "Wilt Chamberlain" }, { "question": "Who is the NBAs all-time leader in assists?", "options": [ "John Stockton", "Magic Johnson", "Steve Nash" ], "correct_answer": "John Stockton" } ] }'

#data = generatorQuiz.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)

quiz_data_dict=json.loads(data)

audio.download_questions_audios_local(quiz_data_dict["questions"])

ruta_audios = Path(os.getcwd()+'/audio')

audioDrive=[]

while len(list(ruta_audios.glob("*")))<NUMBER_OF_QUESTIONS:
    time.sleep(1)


for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
    urlDrive = audio.upload_file_to_google_drive(os.getcwd()+'/audio'+str(index_pregunta)+'.mp3', '/audio'+str(index_pregunta)+'.mp3')
    audioDrive.append(urlDrive)



text_start_anim = Animation(
    time="0 s",
    duration="1.5 s",
    easing="quadratic-out",
    type="text-slide",
    scope="split-clip",
    split="line",
    distance="100%",
    direction="up",
)

text_end_anim = Animation(
    time="end",
    duration="1 s",
    easing="quadratic-out",
    type="text-slide",
    direction="left",
    split="line",
    scope="element",
    distance="200%",
    reversed=True
)

comp_start_anim = Animation(
    time="start",
    duration="1 s",
    transition=True,
    type="wipe",
    fade=False,
    x_anchor="0%",
    end_angle="270°",
    start_angle="270°"
)

stroke_color = [{ "time": "0 s", "value": "#000000" }, { "time": "5.2 s", "value": "#000000" }, { "time": "5.5 s", "value": "#00ff00" }]

source = Source('mp4', 1080, 1920, functions_videos.generar_tiempo_video(NUMBER_OF_QUESTIONS))
background_music = Audio("Music", 18, "0 s", None, True, "b5dc815e-dcc9-4c62-9405-f94913936bf5", "51%", "2 s")
source.elements.append(background_music)
video = Video(source)

#audio = [
#    "https://drive.google.com/uc?export=download&id=1zS_b48WFMOosvi9FPjul-RKYwo-IEfC3",
#    "https://drive.google.com/uc?export=download&id=1Vbg75JkipNkcGY0aeVMavJFfiITvmHyM",
#    "https://drive.google.com/uc?export=download&id=1Vbg75JkipNkcGY0aeVMavJFfiITvmHyM",
#    "https://drive.google.com/uc?export=download&id=1Vbg75JkipNkcGY0aeVMavJFfiITvmHyM"
#]

for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
    composition = Composition("Question" + str(index_pregunta), 1, "8 s")

    question_text = Element("text", track=2, text=question["question"], y="21.80%", fill_color="#000000", background_color="#ffffff")
    question_text.animations.append(text_start_anim)
    question_text.animations.append(text_end_anim)
    composition.elements.append(question_text)

    question_to_speech = Audio("Audio" + str(index_pregunta), 10, "0 s", "2 s", True, audio[index_pregunta], "100%", "0 s")
    composition.elements.append(question_to_speech)

    animation = Animation(easing='linear', type='scale', scope='element', start_scale='120%', fade=False)
    #image = Image(background_list_dict[index_pregunta], 1, 10, True, [])
    #image.animations.append(animation)
    #composition.elements.append(image)

    counter = Image("06311a89-c770-48e1-8a33-b5c1c417c787", 9, 5, True, [], y="81.96%", width="26.062%", height="15.1904%")
    composition.elements.append(counter)

    countdown = Audio("countdown", 10, "0 s", "4.8 s", True, "3b591fe7-e995-4e18-9353-f38c122cc3fb", "100%", "0 s")
    composition.elements.append(countdown)
    correct = Audio("correct", 10, "4.90 s", "1.85 s", True, "530d3905-bd5b-4534-9532-f6657ed03296", "100%", "0 s")
    composition.elements.append(countdown)
    composition.elements.append(correct)

    if index_pregunta > 0:
        composition.animations.append(comp_start_anim)

    for index_opcion, option in enumerate(question["options"]):
        position_y = 52 + (10 * index_opcion)
        option_text = Element("text", track=index_opcion + 3, text=option, y=str(position_y) + "%", fill_color="#ffffff")
        if index_opcion == functions_videos.encontrar_indice(quiz_data_dict["questions"][index_pregunta]["options"],quiz_data_dict["questions"][index_pregunta]["correct_answer"]):
            option_text.stroke_color = stroke_color
        else:
            option_text.stroke_color = "#000000"
        
        composition.elements.append(option_text)

    for i in range(5):
        countdown_text_number = Element("text", track=12, text=str(5 - i), x="54.90%", y="84.96%", z_index=1, time=i, duration="1 s", fill_color="#111111", font_size="15 vmin")
        composition.elements.append(countdown_text_number)

    source.elements.append(composition)



output = json.loads(video.toJSON())

response = requests.post(
 'https://api.creatomate.com/v1/renders',
 headers={
  'Authorization': 'Bearer '+str({AUTORIZACION}),
  'Content-Type': 'application/json',
 },
 json=output
)

audio.eliminar_archivos_en_ruta(os.getcwd()+'/audio')
for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
    audio.eliminar_archivo_de_drive(audioDrive[index_pregunta])


print("todo ok")
