import browser_cookie3 # type: ignore
import os
import time
from pathlib import Path
import sqlite3
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
    print("LISTA NAVEGADORES")
    print("[1] Chrome")
    print("[2] Firefox")
    print("[3] Opera")
    print("[4] Opera GX")
    print("[5] Vivaldi")
    print("[6] Brave")
    print("[7] Todos")
    browser_choose = input("--> ")
    return browser_choose

# Función para obtener cookies del navegador seleccionado
def get_cookies(browser_choose):
    try:
        if browser_choose == "1":
            navegador = browser_cookie3.chrome()
            nombre_navegador = "Chrome"
        elif browser_choose == "2":
            navegador = browser_cookie3.firefox()
            nombre_navegador = "Firefox"
        elif browser_choose == "3":
            navegador = browser_cookie3.opera()
            nombre_navegador = "Opera"
        elif browser_choose == "4":
            navegador = browser_cookie3.opera_gx()
            nombre_navegador = "Opera GX"
        elif browser_choose == "5":
            navegador = browser_cookie3.vivaldi()
            nombre_navegador = "Vivaldi"
        elif browser_choose == "6":
            navegador = browser_cookie3.brave()
            nombre_navegador = "Brave"
        elif browser_choose == "7":
            navegador = browser_cookie3.load()
            nombre_navegador = "Todos"
        else:
            print("Opción no válida.")
            return None, None
        return navegador, nombre_navegador
    except Exception as e:
        print(f"Error al obtener cookies: {e}")
        return None, None

# Función para cerrar aplicaciones del navegador
def cerrar_aplicaciones(nombre_navegador):
    if nombre_navegador == "Chrome":
        os.system("taskkill /IM chrome.exe /F")
    elif nombre_navegador == "Firefox":
        os.system("taskkill /IM firefox.exe /F")
    elif nombre_navegador == "Opera":
        os.system("taskkill /IM opera.exe /F")
    elif nombre_navegador == "Opera GX":
        os.system("taskkill /IM opera.exe /F")
    elif nombre_navegador == "Vivaldi":
        os.system("taskkill /IM vivaldi.exe /F")
    elif nombre_navegador == "Brave":
        os.system("taskkill /IM brave.exe /F")
    elif nombre_navegador == "Todos":
        os.system("taskkill /IM chrome.exe /F")
        os.system("taskkill /IM firefox.exe /F")
        os.system("taskkill /IM opera.exe /F")
        os.system("taskkill /IM vivaldi.exe /F")
        os.system("taskkill /IM brave.exe /F")

# Función para eliminar cookies
def eliminar_cookies(userPath, nombre_navegador, tipo):
    cookies_path = os.path.join(userPath, f"{nombre_navegador}_cookies.txt")
    try:
        with open(cookies_path, "w") as file:
            file.write(f"Eliminando {tipo} de {nombre_navegador}")
        print(f"{tipo} de {nombre_navegador} eliminadas.")
    except Exception as e:
        print(f"Error al eliminar cookies: {e}")

# Función para eliminar todas las cookies
def eliminar_todas_cookies(userPath, nombre_navegador):
    eliminar_cookies(userPath, nombre_navegador, "cookies de sesión")
    eliminar_cookies(userPath, nombre_navegador, "cookies de datos")

# Función para explorar cookies
def explorar_cookies(cookies):
    if not cookies:
        print("No se encontraron cookies.")
        time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        return

    while True:
        print("1. Explorar cookies de sesión")
        print("2. Explorar todas las cookies")
        print("3. Volver al menú principal")
        tipo = input("Elige una opción: ")

        if tipo == "1" or tipo == "2":
            break
        elif tipo == "3":
            return
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    found_cookies = False
    print("Presiona 'q' para dejar de explorar las cookies.")
    for cookie in cookies:
        if tipo == "1" and cookie.expires is None:
            print(cookie)
            found_cookies = True
        elif tipo == "2":
            print(cookie)
            found_cookies = True

        if input() == 'q':
            break

    if not found_cookies:
        print("No se encontraron cookies para la opción seleccionada.")
        time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje

# Función para guardar cookies en una base de datos SQLite
def guardar_cookies(cookies, nombre_navegador):
    if not cookies:
        print("No se encontraron cookies.")
        time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        return

    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    db_path = asksaveasfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")], title="Guardar cookies como")
    root.destroy()  # Destruir la ventana principal de Tkinter

    if not db_path:
        print("No se seleccionó ninguna ruta para guardar las cookies.")
        time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        return

    while True:
        print("1. Guardar cookies de sesión")
        print("2. Guardar todas las cookies")
        print("3. Volver al menú principal")
        tipo = input("Elige una opción: ")

        if tipo == "1" or tipo == "2":
            break
        elif tipo == "3":
            return
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cookies (
                name TEXT,
                value TEXT,
                domain TEXT,
                path TEXT,
                secure INTEGER,
                expires INTEGER
            )
        ''')

        found_cookies = False
        for cookie in cookies:
            if tipo == "1" and cookie.expires is None:
                cursor.execute('''
                    INSERT INTO cookies (name, value, domain, path, secure, expires)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (cookie.name, cookie.value, cookie.domain, cookie.path, cookie.secure, cookie.expires))
                found_cookies = True
            elif tipo == "2":
                cursor.execute('''
                    INSERT INTO cookies (name, value, domain, path, secure, expires)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (cookie.name, cookie.value, cookie.domain, cookie.path, cookie.secure, cookie.expires))
                found_cookies = True

        if not found_cookies:
            print("No se encontraron cookies para la opción seleccionada.")
        else:
            conn.commit()
            print(f"Cookies de {nombre_navegador} guardadas en {db_path}.")
        conn.close()
    except Exception as e:
        print(f"Error al guardar cookies: {e}")
    time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje

# Función para apagar el ordenador
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

# Función principal del menú
def menuInicio():
    while True:
        limpiar_pantalla()
        print("1. Eliminar cookies de sesión")
        print("2. Eliminar cookies persistentes")
        print("3. Eliminar todas las cookies")
        print("4. Explorar cookies")
        print("5. Guardar cookies")
        print("6. Salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            browser_choice = choose_browser()
            userPath = getUserPath()
            cookies, nombre_navegador = get_cookies(browser_choice)
            if cookies:
                cerrar_aplicaciones(nombre_navegador)
                eliminar_cookies(userPath, nombre_navegador, "cookies de sesión")
                apagar()
            else:
                print("No se pudieron obtener las cookies.")
                time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        elif choice == "2":
            browser_choice = choose_browser()
            userPath = getUserPath()
            cookies, nombre_navegador = get_cookies(browser_choice)
            if cookies:
                cerrar_aplicaciones(nombre_navegador)
                eliminar_cookies(userPath, nombre_navegador, "cookies persistentes")
            else:
                print("No se pudieron obtener las cookies.")
                time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        elif choice == "3":
            browser_choice = choose_browser()
            userPath = getUserPath()
            cookies, nombre_navegador = get_cookies(browser_choice)
            if cookies:
                cerrar_aplicaciones(nombre_navegador)
                eliminar_todas_cookies(userPath, nombre_navegador)
            else:
                print("No se pudieron obtener las cookies.")
                time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        elif choice == "4":
            browser_choice = choose_browser()
            cookies, nombre_navegador = get_cookies(browser_choice)
            if cookies:
                explorar_cookies(cookies)
            else:
                print("No se pudieron obtener las cookies.")
                time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        elif choice == "5":
            browser_choice = choose_browser()
            cookies, nombre_navegador = get_cookies(browser_choice)
            if cookies:
                guardar_cookies(cookies, nombre_navegador)
            else:
                print("No se pudieron obtener las cookies.")
                time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
        elif choice == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
            time.sleep(2)  # Pausa de 2 segundos para que el usuario vea el mensaje
            limpiar_pantalla()

if __name__ == "__main__":
    menuInicio()
