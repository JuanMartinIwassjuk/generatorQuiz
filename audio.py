import openai
import os
import time
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlparse, parse_qs

import os



def download_questions_audios_local(questions):
    for index_pregunta, question in enumerate(questions):
        speech_file_path = Path(__file__).parent / "audio" / (str(index_pregunta) + ".mp3")
        response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=question["question"]

        )

        response.stream_to_file(speech_file_path)



def authenticate():
    creds = None
    
    # Comprueba si ya hay credenciales almacenadas
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    
    # Si no hay credenciales válidas, solicita la autorización del usuario
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://www.googleapis.com/auth/drive']
            )
            creds = flow.run_local_server(port=0)
        
        # Guarda las credenciales para usarlas la próxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def upload_file_to_google_drive(file_path, file_name):
    creds = authenticate()
    drive_service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path, resumable=True)
    
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    
    file_url = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    
    return file_url

def obtener_Url_Del_Archivo_De_Drive(Num_audio):
    file_path = os.getcwd()+'/audio'+str(Num_audio)+'.mp3'
    file_name = '/audio'+str(Num_audio)+'.mp3'
    
    file_url = upload_file_to_google_drive(file_path, file_name)
    
    if file_url:
        print("URL del archivo:", file_url)
        return file_url
    else:
        print("Error al subir archivo a Google Drive.")


def eliminar_archivos_en_ruta(ruta):
    """
    Elimina todos los archivos en la ruta especificada.
    
    :param ruta: La ruta donde se encuentran los archivos a eliminar.
    """
    try:
        # Verificar si la ruta existe y es un directorio
        if os.path.isdir(ruta):
            # Iterar sobre los archivos en la ruta y eliminarlos
            for archivo in os.listdir(ruta):
                ruta_archivo = os.path.join(ruta, archivo)
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                    print(f"Archivo eliminado: {ruta_archivo}")
            print("Todos los archivos han sido eliminados.")
        else:
            print(f"La ruta especificada '{ruta}' no es un directorio válido.")
    except Exception as e:
        print(f"Error al intentar eliminar archivos en la ruta '{ruta}': {e}")


def eliminar_archivo_de_drive(file_url):
    try:
        # Extraer el ID del archivo de la URL
        file_id = file_url.split("/")[5]
        
        # Autenticar
        creds = authenticate()
        drive_service = build('drive', 'v3', credentials=creds)
        
        # Eliminar el archivo
        drive_service.files().delete(fileId=file_id).execute()
        
        print("Archivo eliminado de Google Drive.")
    except Exception as e:
        print(f"Error al intentar eliminar el archivo de Google Drive: {e}")


def obtener_cantidad_archivos_en_carpeta(url_archivo):

    servicio = authenticate()

    # Parsear la URL del archivo para obtener su ID
    id_archivo = parse_qs(urlparse(url_archivo).query)['id'][0]
    
    # Obtener información del archivo
    archivo = servicio.files().get(fileId=id_archivo, fields='parents').execute()
    id_carpeta = archivo.get('parents')[0]
    
    # Obtener la lista de archivos en la carpeta
    resultados = servicio.files().list(q="'{}' in parents and trashed=false".format(id_carpeta),
                                       fields='nextPageToken, files(id)').execute()
    cantidad_archivos = len(resultados.get('files', []))
    return cantidad_archivos