import os
import time
import sqlite3
from pathlib import Path

sistemaOperativo = None

def getUserPath():
    return str(Path.home())

def operativeSystem():
    global sistemaOperativo
    if os.name == "nt":
        sistemaOperativo = "Windows"
    elif os.name == "posix":
        sistemaOperativo = "Linux"
    else:
        sistemaOperativo = "Desconocido"
        print("Sistema operativo no soportado para apagar automáticamente.")

def cerrar_aplicaciones():
    print("Cerrando aplicaciones...")
    os.system("taskkill /F /IM vivaldi.exe")  # Cierra todas las aplicaciones
    time.sleep(2)  # Espera 2 segundos
    print("Aplicaciones cerradas")


#Probisional --> Autoencontrar archivo de Cookies
####################################################################################################################################
def deleteJournalCookies(userPath):  #Cookies de navegacion
    print("Eliminando cookies...")
    time.sleep(1)
    deleteJournalCookies_paths = [ os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Network", "Cookies-journal"),
                                 os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Extension Cookies-journal")
    ]
                                 
    for deleteJournalCookies_path in deleteJournalCookies_paths:
        if os.path.exists(deleteJournalCookies_path):
            try:
                os.remove(deleteJournalCookies_path) 
                print(f"Archivo {deleteJournalCookies_path} eliminado.")
            except  Exception as e: 
                print(f"Error al eliminar archivo {deleteJournalCookies_path}: {str(e)}")
        else:
            print(f"El archivo {deleteJournalCookies_path} no existe.") 

def deleteCookies(userPath):  #Cookies de cuentas
    print("Eliminando cookies...")
    time.sleep(1)
    deleteCookies_paths = [
        os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Network", "Cookies"),
        os.path.join(userPath, "AppData", "Local", "Vivaldi", "User Data", "Default", "Extension Cookies")
    ]

    for deleteCookies_path in deleteCookies_paths:
        if os.path.exists(deleteCookies_path):
            try:
                os.remove(deleteCookies_path)
                print(f"Archivo {deleteCookies_path} eliminado.")
            except Exception as e:
                print(f"Error al eliminar archivo {deleteCookies_path}: {str(e)}")
        else:
            print(f"El archivo {deleteCookies_path} no existe.") 
####################################################################################################################################


def apagar():
    print("Apagando...")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Apagando el ordenador...")
    if os.name == "nt":
        os.system("shutdown /s /f /t 0")
    elif os.name == "posix":
        os.system("sudo shutdown -h now")
    else:
        print("Sistema operativo no soportado para apagar automáticamente.")



while True:
    userPath = getUserPath()  # Ruta del usuario
    
    os.system("cls" if os.name == "nt" else "clear")  # Limpiamos la consola

    print("1. Apagar ordenador y borrar cookies")
    print("2. Borrar cookies")
    print("3. Borrar datos de navegación")
    print("4. Salir")
    shutdown = input("Qué quieres hacer: ").lower()

    if shutdown == "1":
        print("Apagando...")
        time.sleep(1)
        cerrar_aplicaciones()
        deleteJournalCookies(userPath)
        deleteCookies(userPath)
        apagar()
        break

    elif shutdown == "2":
        print("Borrando cookies...")
        time.sleep(1)
        cerrar_aplicaciones()
        deleteJournalCookies(userPath)
        deleteCookies(userPath)
        break

    elif shutdown == "3":
        print("Borrando datos de navegación...")
        time.sleep(1)
        cerrar_aplicaciones()
        deleteJournalCookies(userPath)
        break

    elif shutdown == "4":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Saliendo...")
        time.sleep(1)
        break

    else:
        input("Opción no válida. Inténtalo de nuevo.")
