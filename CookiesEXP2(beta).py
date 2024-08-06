import os
import time
from pathlib import Path
import shutil  # Para copiar archivos

sistemaOperativo = None
navegador = None

# Obtenemos la ruta del usuario Ej(C:\Users\franc\)
def getUserPath():
    return str(Path.home())

# Comprobamos el sistema operativo
def operativeSystem():
    global sistemaOperativo
    if os.name == "nt":
        sistemaOperativo = "Windows"
    elif os.name == "posix":
        sistemaOperativo = "Linux"
    else:
        sistemaOperativo = "Desconocido"
        print("Sistema operativo no soportado para apagar automáticamente.")

# Seleccionamos el navegador actualmente (hay 3 opciones)
def seleccionar_navegador():
    global navegador
    print("Elegir navegador")
    print("[1]. Google Chrome")
    print("[2]. Vivaldi")
    print("[3]. Todos")
    inp_navegador = input("--> ")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

    if inp_navegador == "1":
        navegador = "Google Chrome"
    elif inp_navegador == "2":
        navegador = "Vivaldi"
    elif inp_navegador == "3":
        navegador = "Todos"
    else:
        navegador = None
        print("Navegador no válido")
        return None
    
    return navegador

# Cerramos el navegador seleccionado
def cerrar_aplicaciones():
    print("Cerrando aplicaciones...")
    if navegador in ["Vivaldi", "Todos"]:
        os.system("taskkill /F /IM vivaldi.exe")  # Cierra Vivaldi
    if navegador in ["Google Chrome", "Todos"]:
        os.system("taskkill /F /IM chrome.exe")  # Cierra Google Chrome

    time.sleep(2)  # Espera 2 segundos
    print("Aplicaciones cerradas")

# Función para eliminar cookies
def eliminar_cookies(userPath, tipo_cookies):
    global navegador
    if navegador is None:
        print("Navegador no seleccionado. No se pueden eliminar las cookies.")
        return

    print(f"Eliminando {tipo_cookies}...")
    time.sleep(1)

    navegadores = ["Vivaldi", "Google Chrome"] if navegador == "Todos" else [navegador]

    for browser in navegadores:
        if browser == "Vivaldi":
            data_path = "Vivaldi"
        elif browser == "Google Chrome":
            data_path = "Google/Chrome"
        else:
            continue  # Ignorar navegadores no válidos

        paths = {
            "cookies de navegación": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies-journal"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies-journal")
            ],
            "cookies de cuentas": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies")
            ]
        }

        for cookie_type in paths[tipo_cookies]:
            if os.path.exists(cookie_type):
                try:
                    os.remove(cookie_type)
                    print(f"Archivo {cookie_type} eliminado.")
                except Exception as e:
                    print(f"Error al eliminar archivo {cookie_type}: {str(e)}")
            else:
                print(f"El archivo {cookie_type} no existe.")

# Función para explorar cookies
def explorar_cookies(userPath, tipo_cookies):
    global navegador
    if navegador is None:
        print("Navegador no seleccionado. No se pueden explorar las cookies.")
        return

    print(f"Explorando {tipo_cookies}...")
    time.sleep(1)

    navegadores = ["Vivaldi", "Google Chrome"] if navegador == "Todos" else [navegador]

    for browser in navegadores:
        if browser == "Vivaldi":
            data_path = "Vivaldi"
        elif browser == "Google Chrome":
            data_path = "Google/Chrome"
        else:
            continue  # Ignorar navegadores no válidos

        paths = {
            "cookies de navegación": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies-journal"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies-journal")
            ],
            "cookies de cuentas": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies")
            ]
        }

        for cookie_file in paths[tipo_cookies]:
            if os.path.exists(cookie_file):
                print(f"Archivo {cookie_file} encontrado.")
                try:
                    with open(cookie_file, "r", errors="ignore") as file:
                        content = file.read()
                        print(f"Contenido de {cookie_file}:")
                        print(content[:500])  # Imprime los primeros 500 caracteres del archivo
                except Exception as e:
                    print(f"Error al leer archivo {cookie_file}: {str(e)}")
            else:
                print(f"El archivo {cookie_file} no existe.")

# Función para guardar cookies
def guardar_cookies(userPath):
    global navegador
    if navegador is None:
        print("Navegador no seleccionado. No se pueden guardar las cookies.")
        return

    print("Elige la carpeta donde quieres guardar las cookies:")
    destino = input("Ruta de destino: ").strip()
    if not os.path.exists(destino):
        print("La ruta de destino no existe. Creando...")
        os.makedirs(destino)

    print("Guardando cookies...")
    time.sleep(1)

    navegadores = ["Vivaldi", "Google Chrome"] if navegador == "Todos" else [navegador]

    for browser in navegadores:
        if browser == "Vivaldi":
            data_path = "Vivaldi"
        elif browser == "Google Chrome":
            data_path = "Google/Chrome"
        else:
            continue  # Ignorar navegadores no válidos

        paths = {
            "cookies de navegación": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies-journal"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies-journal")
            ],
            "cookies de cuentas": [
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Network", "Cookies"),
                os.path.join(userPath, "AppData", "Local", data_path, "User Data", "Default", "Extension Cookies")
            ]
        }

        for cookie_type in paths:
            for cookie_file in paths[cookie_type]:
                if os.path.exists(cookie_file):
                    try:
                        shutil.copy(cookie_file, destino)
                        print(f"Archivo {cookie_file} copiado a {destino}.")
                    except Exception as e:
                        print(f"Error al copiar archivo {cookie_file}: {str(e)}")
                else:
                    print(f"El archivo {cookie_file} no existe.")

# Apagar el ordenador
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

# Menú principal
def menuInicio():
    while True:
        print("Qué quieres hacer")
        print("[1]. Apagar ordenador y borrar cookies")
        print("[2]. Borrar cookies")
        print("[3]. Borrar datos de navegación")
        print("[4]. Explorar cookies")
        print("[5]. Guardar cookies")
        print("[6]. Salir")
        choice = input("--> ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

# Menú para elegir el tipo de cookies a eliminar
def menuTipoCookies():
    while True:
        print("Qué tipo de cookies quieres manejar")
        print("[1]. Cookies de navegación")
        print("[2]. Cookies de cuentas")
        choice = input("--> ")

        if choice == "1":
            return "cookies de navegación"
        elif choice == "2":
            return "cookies de cuentas"
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

# Programa principal
while True:
    userPath = getUserPath()  # Ruta del usuario
    os.system("cls" if os.name == "nt" else "clear")  # Limpiamos la consola
    
    shutdown = menuInicio()
    navegador = seleccionar_navegador()  # Seleccionar navegador al inicio

    if navegador is None:
        continue  # Volver al menú si el navegador no es válido

    if shutdown == "1":
        print("Apagando...")
        time.sleep(1)
        cerrar_aplicaciones()
        tipo_cookies = menuTipoCookies()  # Elegir tipo de cookies
        eliminar_cookies(userPath, tipo_cookies)
        apagar()
        break

    elif shutdown == "2":
        print("Borrando cookies...")
        time.sleep(1)
        cerrar_aplicaciones()
        tipo_cookies = menuTipoCookies()  # Elegir tipo de cookies
        eliminar_cookies(userPath, tipo_cookies)
        break

    elif shutdown == "3":
        print("Borrando datos de navegación...")
        time.sleep(1)
        cerrar_aplicaciones()
        eliminar_cookies(userPath, "cookies de navegación")
        break

    elif shutdown == "4":
        tipo_cookies = menuTipoCookies()  # Elegir tipo de cookies
        explorar_cookies(userPath, tipo_cookies)

    elif shutdown == "5":
        guardar_cookies(userPath)

    elif shutdown == "6":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Saliendo...")
        time.sleep(1)
        break
