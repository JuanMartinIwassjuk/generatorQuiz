import json

import requests
import position
import generatorQuiz
from creatomate import Animation, Image, Element, Composition, Source, Video, Audio
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC,BACKGROUND_IMG
def cargar_datos_desde_json(json_data):
    return json.loads(json_data)

def crear_animacion_texto_inicio():
    return {
        "time": "0 s",
        "duration": "1.5 s",
        "easing": "quadratic-out",
        "type": "text-slide",
        "scope": "split-clip",
        "split": "line",
        "distance": "100%",
        "direction": "up",
    }

def crear_animacion_texto_fin():
    return {
        "time": "end",
        "duration": "1 s",
        "easing": "quadratic-out",
        "type": "text-slide",
        "direction": "left",
        "split": "line",
        "scope": "element",
        "distance": "200%",
        "reversed": True
    }

def crear_animacion_composicion_inicio():
    return {
        "time": "start",
        "duration": "1 s",
        "transition": True,
        "type": "wipe",
        "fade": False,
        "x_anchor": "0%",
        "end_angle": "270°",
        "start_angle": "270°"
    }

def generar_colores_trazo():
    return [{"time": "0 s", "value": "#000000"},
            {"time": "5.2 s", "value": "#000000"},
            {"time": "5.5 s", "value": "#00ff00"}]

def crear_fuente():
    return Source('mp4', 1080, 1920, "20 s")

def crear_musica_fondo():
    return Audio("Music", 18, "0 s", None, True, "b5dc815e-dcc9-4c62-9405-f94913936bf5", "51%", "2 s")

def crear_video(source):
    return Video(source)

def crear_composicion(nombre, duration):
    return Composition(nombre, 1, duration)

def crear_texto_elemento(texto, y_pos, fill_color="#000000", background_color="#ffffff"):
    return Element("text", track=2, text=texto, y=y_pos, fill_color=fill_color, background_color=background_color)

def crear_animacion_escala():
    return Animation(easing='linear', type='scale', scope='element', start_scale='120%', fade=False)

def crear_imagen(nombre_imagen, duracion):
    return Image(nombre_imagen, 1, duracion, True, [])

def crear_contador():
    return Image("06311a89-c770-48e1-8a33-b5c1c417c787", 9, 5, True, [], y="81.96%", width="26.062%", height="15.1904%")

def crear_audio(nombre, duracion, start_time, end_time, loop, audio_id, volume, delay):
    return Audio(nombre, duracion, start_time, end_time, loop, audio_id, volume, delay)

def crear_texto_contador(numero, x_pos, y_pos):
    return Element("text", track=12, text=str(numero), x=x_pos, y=y_pos, z_index=1, time=0, duration="1 s", fill_color="#111111", font_size="15 vmin")

def procesar_preguntas(quiz_data_dict, background_list_dict, source):
    for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
        composition = crear_composicion("Question" + str(index_pregunta), "8 s")

        question_text = crear_texto_elemento(question["question"], "21.80%")
        question_text.animations.extend([crear_animacion_texto_inicio(), crear_animacion_texto_fin()])
        composition.elements.append(question_text)

        animation = crear_animacion_escala()
        image = crear_imagen(background_list_dict[index_pregunta], 10)
        image.animations.append(animation)
        composition.elements.append(image)

        composition.elements.append(crear_contador())
        composition.elements.append(crear_audio("countdown", 10, "0 s", "4.8 s", True, "3b591fe7-e995-4e18-9353-f38c122cc3fb", "100%", "0 s"))
        composition.elements.append(crear_audio("correct", 10, "4.90 s", "1.85 s", True, "530d3905-bd5b-4534-9532-f6657ed03296", "100%", "0 s"))

        if index_pregunta > 0:
            composition.animations.append(crear_animacion_composicion_inicio())

        for index_opcion, option in enumerate(question["options"]):
            position_y = 52 + (10 * index_opcion)
            option_text = crear_texto_elemento(option, str(position_y) + "%", fill_color="#ffffff")
            if index_opcion == position.encontrar_indice(question["options"], question["correct_answer"]):
                option_text.stroke_color = generar_colores_trazo()
            else:
                option_text.stroke_color = "#000000"
            composition.elements.append(option_text)

        for i in range(5):
            composition.elements.append(crear_texto_contador(5 - i, "54.90%", "84.96%"))

        source.elements.append(composition)

    return source

if __name__ == "__main__":
    
    background_list_dict = cargar_datos_desde_json(BACKGROUND_IMG)
    #data = '{"questions": [ { "question": "Which event marked the end of World War II in Europe?", "options": ["The signing of the Treaty of Versailles", "The dropping of the atomic bomb on Hiroshima", "The unconditional surrender of Nazi Germany"], "correct_answer": "The unconditional surrender of Nazi Germany" }, { "question": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln"], "correct_answer": "George Washington" } ]}'
    data = generatorQuiz.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)
    quiz_data_dict = cargar_datos_desde_json(data)
    
    source = crear_fuente()
    source.elements.append(crear_musica_fondo())
    
    video = crear_video(source)
    
    source = procesar_preguntas(quiz_data_dict, background_list_dict, source)
    
    output = json.loads(video.toJSON())

    response = requests.post(
'https://api.creatomate.com/v1/renders',
headers={
'Authorization': 'Bearer c663356c21cf47a999df4684c11d6bc8af5f486da8ac9ab718afbc26ada2f5cb37981ab32767cd0565936e91e3e08b10',
'Content-Type': 'application/json',
},
json=output
)
