Generación del Quiz
Para incorporar un Quiz a tu proyecto, seguir los siguientes pasos:

1. Crear el archivo de configuración
En la carpeta principal del proyecto, crea un archivo llamado "config.py".

2. Configuración del archivo
Abre el archivo "config.py" y personalízalo según tus preferencias para diseñar el Quiz. Asegúrate de incluir las siguientes características:

API_KEY = 'api_key'

# Nombre del modelo de OpenAI
MODEL_NAME = 'modelo_de_chatgtp'

# Número de preguntas en el Quiz
NUMBER_OF_QUESTIONS = 4

# Número de opciones por pregunta
NUMBER_OF_OPTIONS = 2

# Nivel de dificultad del Quiz (opciones: 'fácil', 'normal', 'difícil')
LEVEL_OF_DIFFICULTY = 'normal'

# Tema del Quiz
TOPIC = 'history'

3. Personalización
Ajusta los valores de API_KEY, MODEL_NAME, NUMBER_OF_QUESTIONS, NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY y TOPIC según tus necesidades y preferencias.