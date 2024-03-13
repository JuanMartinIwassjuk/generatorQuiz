#Generación del Video

Para crear un video , seguir los siguientes pasos:

1. descargar las siguientes dependencias de python en el bash:

pip install requests

pip install openai

2. debes tener una cuenta de "creatomate.com" y obtener el código de autorización para enviar el request: debe ser algo así:
c623356c25cf47a999df4684c11d6bc8af5g486da8ac9ab718atkc26ada2f5cb37981ab32767cd0561936e91e3e08b01

3. Crear el archivo de configuración
En la carpeta principal del proyecto, crea un archivo llamado "config.py".

1. Configuración del archivo
Abre el archivo "config.py" y personalízalo según tus preferencias para diseñar el Quiz y enviar el request. Asegúrate de incluir las siguientes características:

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

# Las imágenes de fondo de cada pregunta, deberán venir en formato json
BACKGROUND_IMG='["url_imagen_pregunta_1","url_imagen_pregunta_2"]'

# La autorización para el envío del request mencionado anteriormente
AUTORIZACION='c623356c25cf47a999df4684c11d6bc8af5g486da8ac9ab718atkc26ada2f5cb37981ab32767cd0561936e91e3e08b01'


El archivo para que funcione correctamente deberia quedar algo así:
![Los valores proporcionados para "API_KEY" y "autorizacion" son meramente ejemplos ilustrativos y no tienen la funcionalidad real de acceso.](https://github.com/JuanMartinIwassjuk/generatorQuiz/blob/main/ejemploConfig.png?raw=true)

Aclaracion: Los valores proporcionados para "API_KEY" y "AUTORIZACION" son meramente ejemplos ilustrativos y no tienen la funcionalidad real de acceso.

