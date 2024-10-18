# Versión: 0.5
# Autor: Francisco Fernández Fernández


import importlib
import itertools
import subprocess


def check_and_install_libraries():  # Comprobar e instalar librerías necesarias
    libraries = ["psutil", "browser_cookie3"]
    for lib in libraries:
        try:
            importlib.import_module(lib)
        except ImportError:
            install = input(f"La librería {lib} no está instalada. ¿Quieres instalarla? (s/n): ").strip().lower()
            if install == 's':
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            else:
                print(f"La librería {lib} es necesaria para el funcionamiento del script. Saliendo...")
                exit(1)

check_and_install_libraries()  # Comprobar e instalar librerías necesarias
print("Librerías instaladas correctamente.\n\n")

import platform     # librería para obtener el sistema operativo
import sys
import threading
import os
import time
import psutil
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Función para obtener la ruta del usuario
def getUserPath():
    return str(Path.home())

# Función para elegir el navegador
def choose_browser():
    print("Elige un navegador:")
    print("___________________")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    print("4. Opera")
    print("5. Opera GX")
    print("6. Vivaldi")
    print("7. Brave")
    print("8. Todos los navegadores")
    print("9. Volver al menú principal")
    choice = input("/-->: ").strip()
    browsers = { "1": "Chrome", "2": "Firefox", "3": "Edge", "4": "Opera", "5": "Opera GX", "6": "Vivaldi", "7": "Brave", "8": [ "Chrome", "Firefox", "Edge", "Opera", "Opera GX", "Vivaldi", "Brave"]}
    return browsers.get(choice, None)

# Función para comprobar si el navegador está abierto
def is_browser_open(browser_name):
    if isinstance(browser_name, list):
        open_browsers = []
        for browser in browser_name:
            for proc in psutil.process_iter(['name']):
                if browser.lower() in proc.info['name'].lower():
                    open_browsers.append(browser)
                    break
        if open_browsers:
            print(f"Los siguientes navegadores están abiertos: {', '.join(open_browsers)}.")
            return open_browsers
        else:
            print("Ninguno de los navegadores está abierto.")
            return []
    else:
        for proc in psutil.process_iter(['name']):
            if browser_name.lower() in proc.info['name'].lower():
                print(f"{browser_name} está abierto.")
                return [browser_name]
        print(f"{browser_name} no está abierto.")
        return []
# 1ª ley del programador: Si funciona aunque no sepas el xq, no lo toques.
# Función para cerrar el navegador
def close_browser(browser_name):
    def question(browser): 
        quest = input(f"El navegador {browser} está abierto. ¿Quieres cerrarlo? [Y/N]: ").strip().lower()
        if quest in ["y", "s"]:
            os_system = platform.system() # platform.system --> librería para obtener el sistema operativo
            if os_system == "Windows":
                subprocess.call(["taskkill", "/F", "/IM", f"{browser}.exe"])
            elif os_system == "Linux":
                subprocess.call(["pkill", "-f", browser])
            elif os_system == "Darwin":
                subprocess.call(["pkill", browser])
            else:
                print(f"Estás usando un sistema operativo desconocido: {os_system}")

    if isinstance(browser_name, list):
        for browser in browser_name:
            question(browser)
    else:
        question(browser_name)

# Función para eliminar cookies de
def delete_session_cookies():
    def browser_path(browser):
        os_system = platform.system() # platform.system --> librería para obtener el sistema operativo
        if os_system == "Windows":
            if browser == "Chrome":
                return getUserPath() + r"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network" #(Cookies, Cookies-journal)
            elif browser == "Firefox":
                return getUserPath() + r"\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\tng6xnez.default-release\\cookies.sqlite" #(cookies.sqlite) tanto persistentes como de sesión
            elif browser == "Edge":
                return getUserPath() + r"\\AppData\\Local\\Microsoft\\Edge\\User Data\Default" # Comprobar
            elif browser == "Opera":
                return getUserPath() + r"\\AppData\\Roaming\\Opera Software\\Opera Stable" # Comprobar
            elif browser == "Opera GX":
                return getUserPath() + r"\\AppData\\Roaming\\Opera Software\\Opera GX Stable" # Comprobar
            elif browser == "Vivaldi":
                return getUserPath() + r"\\AppData\\Local\\Vivaldi\\User Data\\Default\\Network" #(Cookies, Cookies-journal) 
            elif browser == "Brave":
                return getUserPath() + r"\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Network\\" #(Cookies, Cookies-journal)
            else:
                return None
                
        elif os_system == "Linux":
            print("En desarollo")
        elif os_system == "Darwin":
            print("En desarollo")
        else:
            print(f"Estás usando un sistema operativo desconocido: {os_system}")



    
# añadir script q elimine datos de navegación (History, caché, Visited Links, etc)

# Función principal del menú
def main():
    while True:
        print("      COOKIES MANAGER")
        print("      MENU PRINCIPAL")
        print("_______________________________")
        print("1. Eliminar cookies")
        print("2. Eliminar datos de navegación")
        print("3. Eliminar todo")
        print("4. Explorar tokens de inicio de sesión")
        print("5. Explorar cookies")
        print("6. Guardar cookies")
        print("7. Apagado seguro")
        print("8. Salir")
        choice = input("/-->: ").strip()
        limpiar_pantalla()

        if choice == "8":
            print("Saliendo...")
            loading_animation()
            limpiar_pantalla()
            break

        elif choice == "1":
            browser_choice = choose_browser()
            if browser_choice is None:
                continue
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    if is_browser_open(browser):
                        close_browser(browser)
            else:
                if is_browser_open(browser_choice):
                    close_browser(browser_choice)
            input("Presiona Enter para continuar...")
            

        elif choice in ["2", "3", "4", "5", "6", "7"]:
            input("En desarrollo...")

        else:
            input(f"Opción [{choice}] no válida. ENTER para intentar de nuevo.")
            limpiar_pantalla()





# Animación de salida
def loading_animation():
    stop_loading = False
    def animate():
        nonlocal stop_loading
        for c in itertools.cycle(['/', '\\']):
            if stop_loading:
                break
            print(c, end='\r')
            time.sleep(0.5)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(2)
    stop_loading = True
    t.join()

# Punto de entrada del script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción del usuario.")
        print("Saliendo...")
        time.sleep(1)
        limpiar_pantalla()
        exit(0)
    except Exception as e:
        print(f"Error: {e}")
        print("Saliendo...")
        time.sleep(1)
        limpiar_pantalla()
        exit(1)
