import os
import time
from pathlib import Path

def getUserPatch():
    return "{}\\".format(Path.home())

def cerrar_aplicaciones():
    print("Cerrando aplicaciones...")
    os.system("taskkill /F /IM vivaldi.exe")  # Cierra todas las aplicaciones
    time.sleep(2)  # Espera 2 segundos
    print("Aplicaciones cerradas")

def borrar_cookies(userPath):
    print("Eliminando cookies...")
    try:
        files_to_delete = [
            os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Network", "Cookies-journal"),
            os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Network", "Cookies")
        ]
        

        for file_path in files_to_delete:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Archivo {file_path} eliminado.")
            else:
                print(f"El archivo {file_path} no existe.")
    except:
        print("Cookies no encontradas")



def apagar():
    print("Apagando...")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Apagando el ordenador...")
    if os.name == "nt":
        os.system("shutdown /s /f /t 0")
        #hacerlo valido en linux
    #elif os.name == "posix":
        #os.system("sudo shutdown -h now")
    #else:
       #print("Sistema operativo no soportado para apagar automáticamente.")

while True:
    #Calculamos la ruta del usuario
    userPath = getUserPatch()
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Apagar ordenador y borrar cookies")
    print("2. Borrar cookies")
    print(". Salir")
    shutdown = input("Que quieres hacer: ").lower()

    if shutdown == "1":
        print("Apagando...")
        time.sleep(1)
        cerrar_aplicaciones()
        borrar_cookies(userPath)
        apagar()
        break

    elif shutdown == "2":
        print("Borando cookies...")
        time.sleep(1)
        cerrar_aplicaciones()
        borrar_cookies(userPath)
        break

    elif shutdown == "3":
        print("Saliendo...")
        time.sleep(1)
        break

    else:
        input("Opción no válida. Inténtalo de nuevo.")
        
