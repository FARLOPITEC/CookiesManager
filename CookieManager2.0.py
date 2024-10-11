# Versión: 0.2
# Autor: Francisco Fernández Fernández

import importlib
import subprocess
import sys
def check_and_install_libraries():  # Comprobar e instalar librerías necesarias
    # poner las librerías que se necesiten para la ejecución del script en la lista libraries
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
check_and_install_libraries() # Comprobar e instalar librerías necesarias
print("Librerías instaladas correctamente.\n\n")


import os
import time
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Función para obtener la ruta del usuario
def getUserPath():
    return str(Path.home())

# Función para seleccionar navegador
def choose_browser():
    while True:
        print("LISTA NAVEGADORES")
        print("[1] Chrome")
        print("[2] Firefox")
        print("[3] Opera")
        print("[4] Opera GX")
        print("[5] Vivaldi")
        print("[6] Brave")
        print("[7] Todos")
        print("[8] Volver al menú principal")
        browser_choose = input("/--> ")
        if browser_choose in ["1", "2", "3", "4", "5", "6", "7"]:
            return browser_choose
        elif browser_choose == "8":
            return None
        else:
            input(f"Opción [{browser_choose}] no válida.  ENTER para intentar de nuevo.")
            os.system("cls" if os.name == "nt" else "clear")

# Rederigir broeser_choose a su navegador correspondiente



# Función principal del menú
def main():
    while True:
        #limpiar_pantalla() # Limpiar pantalla
        print("      COOKIES MANAGER")
        print("      MENU PRINCIPAL")
        print("_______________________________")
        print("1. Eliminar cookies de sesión")
        print("2. Eliminar cookies persistentes")
        print("3. Eliminar todas las cookies")
        print("4. Comprobar estado de los navegadores")
        print("5. Explorar tokens de inicio de sesión")
        print("6. Explorar cookies")
        print("7. Guardar cookies")
        print("8. Apagado seguro")
        print("9. Salir")
        choice = input("/-->: ")
        os.system("cls" if os.name == "nt" else "clear")

        
        if choice == "9":
            print("Saliendo...")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            break

        elif choice == "1":
            browser_choice = choose_browser()
            print("navegador elegido: ", browser_choice)
            

        elif choice == "2":
            input("En desarrollo...")

        elif choice == "3":
            input("En desarrollo...")

        elif choice == "4":
            input("En desarrollo...")

        elif choice == "5":
            input("En desarrollo...")

        elif choice == "6":
            input("En desarrollo...")
    
        elif choice == "7":
            input("En desarrollo...")

        elif choice == "8":
            input("En desarrollo...")

        else:   # Opción no válida en el menú principal 
            input(f"Opción [{choice}] no válida.  ENTER para intentar de nuevo.")
            os.system("cls" if os.name == "nt" else "clear")

# Punto de entrada del script
if __name__ == "__main__":
    try:    # Control de errores y excepciones 
        main()
    except KeyboardInterrupt: #Comprobar Ctrl + C para salir
        print("\nInterrupción del usuario.")
        print("Saliendo...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        exit(0)
    except Exception as e: # Cualquier otro error
        print(f"Error: {e}")
        print("Saliendo...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        exit(1)
