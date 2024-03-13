#Generación del Video

Para crear un video , seguir los siguientes pasos:

1. descargar las siguientes dependencias de python en el bash:

pip install requests
pip install openai


2. Crear el archivo de configuración
En la carpeta principal del proyecto, crea un archivo llamado "config.py".

3. Configuración del archivo
Abre el archivo "config.py" y personalízalo según tus preferencias para diseñar el Quiz. Asegúrate de incluir las siguientes características:

# Key para consultarle a la api de OpenAI
API_KEY = 'api_key'

# Nombre del modelo de OpenAI
MODEL_NAME = 'modelo_de_chatgtp'

# Número de preguntas en el Quiz
NUMBER_OF_QUESTIONS = 2

# Número de opciones por pregunta
NUMBER_OF_OPTIONS = 3

# Nivel de dificultad del Quiz (opciones: 'very_easy','easy','easy-normal', 'normal','normal-hard', 'hard','very_hard')
LEVEL_OF_DIFFICULTY = 'normal'

# Tema del Quiz
TOPIC = 'history'

# Las imagenes de fondo de cada pregunta, deberán venir en formato json
BACKGROUND_IMG='["https://creatomate.com/files/assets/4a6f6b28-bb42-4987-8eca-7ee36b347ee7", "url_imagen_pregunta_1","url_imagen_pregunta_2"]'



![Texto alternativo](url_de_la_imagen)

