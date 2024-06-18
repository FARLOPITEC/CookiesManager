import os
import time

def cerrar_aplicaciones():
    print("Cerrando aplicaciones...")
    os.system("taskkill /F /IM vivaldi.exe")  # Cierra todas las aplicaciones
    time.sleep(2)  # Espera 2 segundos
    print("Aplicaciones cerradas")

def borrar_cookies():
    cookies_user = input("¿Quieres borrar las Cookies de inicio de sesión? [S/N]: ").lower()
    if cookies_user == "s":
        print("Eliminando cookies...")
        files_to_delete = [
            r"C:\Users\franc\AppData\Local\Vivaldi\User Data\Default\Network\Cookies-journal",
            r"C:\Users\franc\AppData\Local\Vivaldi\User Data\Default\Network\Cookies"

            #para chrome
            #C:\Users\franc\AppData\Local\Google\Chrome\User Data\Default\Network
        ]

        for file_path in files_to_delete:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Archivo {file_path} eliminado.")
            else:
                print(f"El archivo {file_path} no existe.")

def apagar():
    shutdown = input("¿Quieres apagar el ordenador? [S/N]: ").lower()
    if shutdown == "s":
        print("Apagando...")
        time.sleep(1)
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print("Apagando el ordenador...")
        if os.name == "nt":
            os.system("shutdown /s /f /t 0")
    elif shutdown == "n":
        print("Saliendo...")
        time.sleep(1)
    else:
        print("Opción no válida. Inténtalo de nuevo.")

while True:
    close_vivaldi = input("¿Quieres apagar el ordenador? [S/N]: ").lower()

    if close_vivaldi == "s":
        cerrar_aplicaciones()
        borrar_cookies()
        apagar()
        break

    elif close_vivaldi == "n":
        print("Saliendo...")
        time.sleep(1)
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
