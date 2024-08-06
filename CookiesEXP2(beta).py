import os
import time
from pathlib import Path

sistemaOperativo = None
navegador = None

#Optenemos la ruta del usuario Ej(C:\Users\franc\)
def getUserPath():
    return str(Path.home())

#Comprobamos el sistema operativo
def operativeSystem():
    global sistemaOperativo
    if os.name == "nt":
        sistemaOperativo = "Windows"
    elif os.name == "posix":
        sistemaOperativo = "Linux"
    else:
        sistemaOperativo = "Desconocido"
        print("Sistema operativo no soportado para apagar automáticamente.")

#Selecionamos el navegador actualmetente 2
def seleccionar_navegador():
    global navegador
    print("Elegir navegador")
    print("[1]. Google Chrome")
    print("[2]. Vivaldi")
    print("[3]. Todos")
    inp_navegador = input("--> ")

    if inp_navegador == "1":
        navegador = "Google Chrome"
    elif inp_navegador == "2":
        navegador = "Vivaldi"
    else:
        navegador = "Navegador no válido"

    print(f"Navegador seleccionado: {navegador}")
    return navegador

#Cerramos el navegador selecionado
def cerrar_aplicaciones():
    print("Cerrando aplicaciones...")
    if navegador == "Vivaldi":
        os.system("taskkill /F /IM vivaldi.exe")  # Cierra Vivaldi
    elif navegador == "Google Chrome":
        os.system("taskkill /F /IM chrome.exe")  # Cierra Google Chrome
    elif navegador == "Todos":
        os.system("taskkill /F /IM vivaldi.exe")  # Cierra Vivaldi
        os.system("taskkill /F /IM chrome.exe")  # Cierra Google Chrome

    time.sleep(2)  # Espera 2 segundos
    print("Aplicaciones cerradas")


#Borramos las cookies de navegacion 
#·································································································#
def deleteJournalCookies(userPath):  # Cookies de navegación
    global navegador
    print("Eliminando cookies de navegación...")
    time.sleep(1)

    if navegador == "Vivaldi":
        data_path = "Vivaldi"
    elif navegador == "Google Chrome":
        data_path = "Google/Chrome"

    deleteJournalCookies_paths = [
        os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies-journal"),
        os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies-journal")
    ]

    for deleteJournalCookies_path in deleteJournalCookies_paths:
        if os.path.exists(deleteJournalCookies_path):
            try:
                os.remove(deleteJournalCookies_path) 
                print(f"Archivo {deleteJournalCookies_path} eliminado.")
            except Exception as e: 
                print(f"Error al eliminar archivo {deleteJournalCookies_path}: {str(e)}")
        else:
            print(f"El archivo {deleteJournalCookies_path} no existe.") 

#Borramos las cookies de cuentas
def deleteCookies(userPath):  # Cookies de cuentas
    global navegador
    print("Eliminando cookies de cuentas...")
    time.sleep(1)

    if navegador == "Vivaldi":
        data_path = "Vivaldi"
    elif navegador == "Google Chrome":
        data_path = "Google/Chrome"

    deleteCookies_paths = [
        os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies"),
        os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies")
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
#·································································································#

#Apagar el ordenador
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

def menuInicio():
    print("")
    print("[1]. Apagar ordenador y borrar cookies")
    print("[2]. Borrar cookies")
    print("[3]. Borrar datos de navegación")
    print("[4]. Salir")
    return input("Qué quieres hacer: ").lower()

while True:
    userPath = getUserPath()  # Ruta del usuario
    
    os.system("cls" if os.name == "nt" else "clear")  # Limpiamos la consola
    seleccionar_navegador()  # Seleccionar navegador al inicio
    shutdown = menuInicio()

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
