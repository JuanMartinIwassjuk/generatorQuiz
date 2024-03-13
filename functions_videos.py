import json

import json

def generarArchivoDeljson(json):
    with open("resultado_json","w") as arch:
     arch.write(json.toJSON())


def generar_tiempo_video(cant_preguntas):
    resultado = str(cant_preguntas * 8) + ' s'
    return resultado

def obtener_diccionario_por_indice(indice):
    diccionarios = [
        {"x": 84, "y": 42},
        {"x": 84, "y": 50},
        {"x": 84, "y": 58}
    ]

    if 0 <= indice < len(diccionarios):
        return diccionarios[indice]
    else:
        return None  # Manejar el caso de índice fuera de rango

def encontrar_indice(lista, cadena):
    try:
        indice = lista.index(cadena)
        return indice
    except ValueError:
        # Si no se encuentra la cadena en la lista, se devuelve -1
        return -1


#data = '{"questions": [ { "question": "Which event marked the end of World War II in Europe?", "options": ["The signing of the Treaty of Versailles", "The dropping of the atomic bomb on Hiroshima", "The unconditional surrender of Nazi Germany"], "correct_answer": "The unconditional surrender of Nazi Germany" }, { "question": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln"], "correct_answer": "George Washington" } ]}'
#quiz_data_dict=json.loads(data)
#indice = encontrar_indice(quiz_data_dict["questions"][0]["options"],quiz_data_dict["questions"][0]["correct_answer"])
#print(obtener_diccionario_por_indice(indice))