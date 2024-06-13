import os
import time

while True:
    shutdown = input("¿Quieres apagar el ordenador? [S/N]: ").lower()
    if shutdown == "s":
        print("Cerrando aplicaciones...")
        
        if os.name == "nt":  # Comprobamos que el sistema sea Windows
            os.system("taskkill /F /IM vivaldi.exe")  # Cierra todas las aplicaciones
        time.sleep(10)  # Espera 10 segundos
        print("Aplicaciones cerradas")
        time.sleep(2)

        cookiesUser = input("¿Quieres borrar las Cookies de inicio de sesión? [S/N]: ").lower()
        if cookiesUser == "s":
            print("Eliminando cookies...")

            # Rutas de los archivos a eliminar
            files_to_delete = [
                r"C:\Users\franc\AppData\Local\Vivaldi\User Data\Default\Network\Cookies-journal",
                r"C:\Users\franc\AppData\Local\Vivaldi\User Data\Default\Network\Cookies"
            ]

            for file_path in files_to_delete:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Archivo {file_path} eliminado.")
                else:
                    print(f"El archivo {file_path} no existe.")

        print("Apagando el ordenador...")
        if os.name == "nt":
            os.system("shutdown /s /f /t 0")  # Apaga el ordenador
        break

    elif shutdown == "n":
        print("Saliendo...")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

print("Proceso completado.")
