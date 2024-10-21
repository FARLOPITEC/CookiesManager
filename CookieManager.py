# Versión: 0.4.8
# Autor: Francisco Fernández Fernández

import importlib
import itertools
import subprocess
import platform     # librería para obtener el sistema operativo
import sys
import threading
import os
import time
import psutil
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

# Comprobar e instalar librerías necesarias
#--------------------------------------------------------------------------------------------------------------
def check_and_install_libraries():  
    libraries = ["psutil"]
    for lib in libraries:
        try:
            importlib.import_module(lib)
        except ImportError:
            install = input(f"La librería {lib} no está instalada. ¿Quieres instalarla? [Y/N]: ").strip().lower()
            if install == 's' or install == 'y':
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            else:
                print(f"La librería {lib} es necesaria para el funcionamiento del script. Saliendo...")
                exit(1)

check_and_install_libraries()  # Comprobar e instalar librerías necesarias
print("⭐Librerías instaladas correctamente.\n")
#--------------------------------------------------------------------------------------------------------------

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Función para obtener la ruta del usuario
def getUserPath():
    return str(Path.home())

# Función para la animación de carga
def loading_animation():
    stop_loading = False
    def animate():
        nonlocal stop_loading
        for c in itertools.cycle(['/', '\\']):
            if stop_loading:
                break
            print(c, end='\r')
            time.sleep(0.3)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(2)
    stop_loading = True
    t.join()

# Función para elegir el navegador
def choose_browser():
    print("╔══════════════════════════════╗")
    print("║       COOKIES MANAGER        ║")   
    print("║      ELIGE UN NAVEGADOR      ║")
    print("╚══════════════════════════════╝\n")
    print("⭐ Elige un navegador:")
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
    if choice == "1":
        return "Chrome"
    elif choice == "2":
        return "Firefox"
    elif choice == "3":
        return "Edge"
    elif choice == "4":
        return "Opera"
    elif choice == "5":
        return "Opera GX"
    elif choice == "6":
        return "Vivaldi"
    elif choice == "7":
        return "Brave"
    elif choice == "8":
        return ["Chrome", "Firefox", "Edge", "Opera", "Opera GX", "Vivaldi", "Brave"]
    elif choice == "9":
        return None
    else:
        print("Opción no válida.")
        return choose_browser()

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


# Función para obtener la ruta de las cookies del navegador
def browser_path_cookies(browser):
    os_system = platform.system()
    user_path = getUserPath()
    
    if os_system == "Windows":
        if browser == "Chrome":
            return user_path + r"\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies"
        elif browser == "Firefox":
            return user_path + r"\AppData\Roaming\Mozilla\Firefox\Profiles\tng6xnez.default-release\cookies.sqlite"
        elif browser == "Edge":
            return user_path + r"\AppData\Local\Microsoft\Edge\User Data\Default\Cookies" # X comprobar    #Mejor no uses Edge 🤢🤮
        elif browser == "Opera":
            return user_path + r"\AppData\Roaming\Opera Software\Opera Stable\Cookies" # X comprobar 
        elif browser == "Opera GX":
            return user_path + r"\AppData\Roaming\Opera Software\Opera GX Stable\Cookies" # X comprobar
        elif browser == "Vivaldi":
            return user_path + r"\AppData\Local\Vivaldi\User Data\Default\Network\Cookies"
        elif browser == "Brave":
            return user_path + r"\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Network\Cookies"
        else:
            return None
    elif os_system == "Linux":
        print("En desarrollo...")
    elif os_system == "Darwin":
        print("En desarrollo...")
    else:
        print(f"Estás usando un sistema operativo desconocido: {os_system}")
  
# Función para eliminar las cookies de sesión del navegador
def delete_session_cookies(browser):
    try:
        os_system = platform.system()
        
        if isinstance(browser, list):
            for b in browser:
                cookie_path = browser_path_cookies(b)
                if cookie_path is None:
                    print(f"Navegador {b} no soportado.")
                    continue
                
                if os_system == "Windows":
                    if os.path.exists(cookie_path):
                        subprocess.run(['del', cookie_path], shell=True, check=True)
                        print("Cookies eliminadas con éxito")
                    else:
                        print(f"No se pudo encontrar {cookie_path}.")
                elif os_system == "Linux":
                    if os.path.exists(cookie_path):
                        subprocess.run(['rm', cookie_path], check=True)
                        print("Cookies eliminadas con éxito")
                    else:
                        print(f"No se pudo encontrar {cookie_path}.")
                elif os_system == "Darwin":
                    print("En desarrollo...")
                else:
                    print(f"Estás usando un sistema operativo desconocido: {os_system}")
        else:
            cookie_path = browser_path_cookies(browser)
            if cookie_path is None:
                print(f"Navegador {browser} no soportado.")
                return
            
            if os_system == "Windows":
                if os.path.exists(cookie_path):
                    subprocess.run(['del', cookie_path], shell=True, check=True)
                    print("Cookies eliminadas con éxito")
                else:
                    print(f"No se pudo encontrar {cookie_path}.")
            elif os_system == "Linux":
                if os.path.exists(cookie_path):
                    subprocess.run(['rm', cookie_path], check=True)
                    print("Cookies eliminadas con éxito")
                else:
                    print(f"No se pudo encontrar {cookie_path}.")
            elif os_system == "Darwin":
                print("En desarrollo...")
            else:
                print(f"Estás usando un sistema operativo desconocido: {os_system}")
    except Exception as e:
        print(f"Error: {e}")


 
# Función para eliminar el historial
def browser_path_history(browser):
    user_path = os.path.expanduser("~")
    os_system = platform.system()
    
    if os_system == "Windows":
        if browser == "Chrome":
            return user_path + r"\AppData\Local\Google\Chrome\User Data\Default\History"
        elif browser == "Firefox":
            return user_path + r"\AppData\Roaming\Mozilla\Firefox\Profiles\places.sqlite"
        elif browser == "Edge":
            return user_path + r"\AppData\Local\Microsoft\Edge\User Data\Default\History" # X comprobar   #Mejor no uses Edge 🤢🤮
        elif browser == "Opera":
            return user_path + r"\AppData\Roaming\Opera Software\Opera Stable\History" # X comprobar
        elif browser == "Opera GX":
            return user_path + r"\AppData\Roaming\Opera Software\Opera GX Stable\History" # X comprobar
        elif browser == "Vivaldi":
            return user_path + r"\AppData\Local\Vivaldi\User Data\Default\History"
        elif browser == "Brave":
            return user_path + r"\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History"
        else:
            return None
    elif os_system == "Linux":
        print("En desarrollo...")
    elif os_system == "Darwin":
        print("En desarrollo...")
    else:
        print(f"Estás usando un sistema operativo desconocido: {os_system}")


# Función para eliminar el historial de navegación
def delete_session_history(browser):
    try:
        os_system = platform.system()
        
        if isinstance(browser, list):
            for b in browser:
                history_path = browser_path_history(b)
                if history_path is None:
                    print(f"Navegador {b} no soportado.")
                    continue
                
                close_browser(b)  # Cerrar el navegador antes de eliminar el historial
                
                if os_system == "Windows":
                    if os.path.exists(history_path):
                        os.remove(history_path)
                        print("Historial eliminado con éxito")
                    else:
                        print(f"No se pudo encontrar {history_path}.")
                elif os_system == "Linux":
                    if os.path.exists(history_path):
                        os.remove(history_path)
                        print("Historial eliminado con éxito")
                    else:
                        print(f"No se pudo encontrar {history_path}.")
                elif os_system == "Darwin":
                    print("En desarrollo...")
                else:
                    print(f"Estás usando un sistema operativo desconocido: {os_system}")
        else:
            history_path = browser_path_history(browser)
            if history_path is None:
                print(f"Navegador {browser} no soportado.")
                return
            
            close_browser(browser)  # Cerrar el navegador antes de eliminar el historial
            
            if os_system == "Windows":
                if os.path.exists(history_path):
                    os.remove(history_path)
                    print("Historial eliminado con éxito")
                else:
                    print(f"No se pudo encontrar {history_path}.")
            elif os_system == "Linux":
                if os.path.exists(history_path):
                    os.remove(history_path)
                    print("Historial eliminado con éxito")
                else:
                    print(f"No se pudo encontrar {history_path}.")
            elif os_system == "Darwin":
                print("En desarrollo...")
            else:
                print(f"Estás usando un sistema operativo desconocido: {os_system}")
    except Exception as e:
        print(f"Error: {e}")

# Función principal del menú
def main():
    while True:
        print("╔══════════════════════════════╗")
        print("║       COOKIES MANAGER        ║")   
        print("║        MENU PRINCIPAL        ║")
        print("╚══════════════════════════════╝\n")
        print("⭐ Que quieres hacer:")
        print("1. Eliminar cookies")
        print("2. Eliminar historial de navegación")
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

        elif choice == "1": # Eliminar cookies
            print("╔══════════════════════════════╗")
            print("║       Eliminar cookies       ║")
            print("╚══════════════════════════════╝")
            browser_choice = choose_browser()
            if browser_choice is None:
                continue

            # Cerrar navegador
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    if is_browser_open(browser):
                        close_browser(browser)
            else:
                if is_browser_open(browser_choice):
                    close_browser(browser_choice)

            # Borrar cookies
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    delete_session_cookies(browser)
                    
            else:
                delete_session_cookies(browser_choice)
                
            print("Proceso completado.")
            input("Presiona ENTER para continuar...")
            limpiar_pantalla()

        elif choice == "2": # Eliminar historial
            print("╔══════════════════════════════╗")
            print("║      Eliminanr historial     ║")
            print("╚══════════════════════════════╝")
            browser_choice = choose_browser()
            if browser_choice is None:
                continue

            # Cerrar navegador
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    if is_browser_open(browser):
                        close_browser(browser)
            else:
                if is_browser_open(browser_choice):
                    close_browser(browser_choice)

            # Borrar historial
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    delete_session_history(browser)
            else:
                delete_session_history(browser_choice)

            print("Proceso completado.")
            input("Presiona ENTER para continuar...")
            limpiar_pantalla()

        elif choice == "3": # Eliminar cookies e historial
            print("╔══════════════════════════════╗")
            print("║ Eliminar cookies e historial ║")
            print("╚══════════════════════════════╝")
            browser_choice = choose_browser()
            if browser_choice is None:
                continue

            # Cerrar navegador
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    if is_browser_open(browser):  
                        close_browser(browser)
            else:
                if is_browser_open(browser_choice):
                    close_browser(browser_choice)

            # Borrar cookies
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    delete_session_cookies(browser)
            
            # Borrar historial
            if isinstance(browser_choice, list):
                for browser in browser_choice:
                    delete_session_history(browser)
            else:
                delete_session_history(browser_choice)

            print("Proceso completado.")
            input("Presiona ENTER para continuar...")
            limpiar_pantalla()

        elif choice in [ "4", "5", "6", "7"]:
            input("En desarrollo...")

        else:
            input(f"Opción [{choice}] no válida. ENTER para intentar de nuevo.")
            limpiar_pantalla()

        
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

#Comentado para registrar los errores a corregir   
    except Exception as e:
        print(f"Error: {e}")
        print("Saliendo...")
        time.sleep(1)
        limpiar_pantalla()
        exit(1)
    
