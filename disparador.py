import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
from config import NUMBER_OF_QUESTIONS

directory_to_watch = os.getcwd()+'/audio'
script_to_run = 'python generatorVideo.py'

# Contador de archivos creados
files_created = 0

# Función para ejecutar el script cuando se creen suficientes archivos
def run_script():
    global files_created
    if files_created >= NUMBER_OF_QUESTIONS:
        print(f"Se han creado {NUMBER_OF_QUESTIONS} audios de voz. Ejecutando el script...")
        time.sleep(8)
        os.system(script_to_run)
        print("ejecutado correctamente, 'ctrl+c' para finalizar")
        files_created = 0
        observer.stop()
        sys.exit()

# Manejador de eventos para monitorizar la creación de archivos
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        global files_created
        if event.is_directory:
            return
        files_created += 1
        print(f"Archivo creado: {event.src_path}")
        run_script()

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(MyHandler(), directory_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
