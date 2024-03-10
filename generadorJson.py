import json
import posicion




def generar_json_data(num_preguntas,quiz_data_dict):
    json_data = {}
    preguntas = quiz_data_dict.get("questions", [])

    for i in range(1, num_preguntas + 1):
        pregunta_key = f"Pregunta{i}"
        opcion_1_key = f"Opcion_1.{i}"
        opcion_2_key = f"Opcion_2.{i}"
        opcion_3_key = f"Opcion_3.{i}"
        posicion_key = f"Posicion{i}"

        if i <= len(preguntas):
            pregunta = preguntas[i-1].get("question", "")
            opciones = preguntas[i-1].get("options", [])
            respuesta_correcta = preguntas[i-1].get("correct_answer", "")
            indice_respuesta = posicion.encontrar_indice(opciones, respuesta_correcta)
            posicion = posicion.obtener_diccionario_por_indice(indice_respuesta)

            json_data[pregunta_key] = pregunta
            json_data[opcion_1_key] = opciones[0] if opciones else ""
            json_data[opcion_2_key] = opciones[1] if len(opciones) > 1 else ""
            json_data[opcion_3_key] = opciones[2] if len(opciones) > 2 else ""
            json_data[posicion_key] = posicion

    # Agregar claves y valores fijos
    json_data["template_id"] = "ca083e1e-8095-4a18-b4cd-2004eb41ddd3"
    json_data["modifications"] = {
        "Music": "https://creatomate.com/files/assets/b5dc815e-dcc9-4c62-9405-f94913936bf5",
        "4e31b834-08c3-4a7e-88d0-bbb69d38a00a": "https://creatomate.com/files/assets/4a6f6b28-bb42-4987-8eca-7ee36b347ee7",
        "859e205a-8a69-41ac-b2ff-bacce9de1c2f": "https://creatomate.com/files/assets/4a6f6b28-bb42-4987-8eca-7ee36b347ee7",
        "Text-2": "Use any video automation tool to replace these text and background assets with your own! 😊",
        "Background-3": "https://creatomate.com/files/assets/4f6963a5-7286-450b-bc64-f87a3a1d8964",
        "Text-3": "Learn how to get started on the Guides & Tutorials page on Creatomate's home page.",
        "Background-4": "https://creatomate.com/files/assets/36899eae-a128-43e6-9e97-f2076f54ea18",
        "Text-4": "Use the template editor to completely customize this video to meet your own needs. 🚀"
    }

    return json_data

# Ejemplo de uso
#cantidad_preguntas = 3  # Cambiar según tus necesidades
#nuevo_json_data = generar_json_data(cantidad_preguntas)
#print(json.dumps(nuevo_json_data, indent=2))