import importlib
import itertools
import subprocess
import platform
import sys
import threading
import os
import time
import psutil
from pathlib import Path
from tkinter import Tk, Button, Label, messagebox, OptionMenu, StringVar, ttk

def check_and_install_libraries():
    libraries = ["psutil"]
    for lib in libraries:
        try:
            importlib.import_module(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

check_and_install_libraries()

def getUserPath():
    return str(Path.home())

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

def browser_path_cookies(browser):
    os_system = platform.system()
    user_path = getUserPath()
    
    if os_system == "Windows":
        if browser == "Chrome":
            return user_path + r"\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies"
        elif browser == "Firefox":
            return user_path + r"\AppData\Roaming\Mozilla\Firefox\Profiles\tng6xnez.default-release\cookies.sqlite"
        elif browser == "Edge":
            return user_path + r"\AppData\Local\Microsoft\Edge\User Data\Default\Cookies"
        elif browser == "Opera":
            return user_path + r"\AppData\Roaming\Opera Software\Opera Stable\Cookies"
        elif browser == "Opera GX":
            return user_path + r"\AppData\Roaming\Opera Software\Opera GX Stable\Cookies"
        elif browser == "Vivaldi":
            return user_path + r"\AppData\Local\Vivaldi\User Data\Default\Network\Cookies"
        elif browser == "Brave":
            return user_path + r"\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Network\Cookies"
        else:
            return None
    elif os_system == "Linux":
        if browser == "Chrome":
            return user_path + r"/.config/google-chrome/Default/Cookies"
        elif browser == "Firefox":
            return user_path + r"/.mozilla/firefox/*.default-release/cookies.sqlite"
        elif browser == "Edge":
            return user_path + r"/.config/microsoft-edge/Default/Cookies"
        elif browser == "Opera":
            return user_path + r"/.config/opera/Cookies"
        elif browser == "Opera GX":
            return user_path + r"/.config/opera-gx/Cookies"
        elif browser == "Vivaldi":
            return user_path + r"/.config/vivaldi/Default/Cookies"
        elif browser == "Brave":
            return user_path + r"/.config/BraveSoftware/Brave-Browser/Default/Cookies"
        else:
            return None
    else:
        messagebox.showerror("Error", f"Estás usando un sistema operativo desconocido: {os_system}")
        return None

def delete_session_cookies(browser):
    try:
        os_system = platform.system()
        cookie_path = browser_path_cookies(browser)
        if cookie_path is None:
            messagebox.showerror("Error", f"Navegador {browser} no soportado.")
            return
        if os.path.exists(cookie_path):
            os.remove(cookie_path)
            messagebox.showinfo("Éxito", "Cookies eliminadas con éxito")
        else:
            messagebox.showerror("Error", f"No se pudo encontrar {cookie_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def browser_path_history(browser):
    user_path = os.path.expanduser("~")
    os_system = platform.system()
    
    if os_system == "Windows":
        if browser == "Chrome":
            return user_path + r"\AppData\Local\Google\Chrome\User Data\Default\History"
        elif browser == "Firefox":
            return user_path + r"\AppData\Roaming\Mozilla\Firefox\Profiles\places.sqlite"
        elif browser == "Edge":
            return user_path + r"\AppData\Local\Microsoft\Edge\User Data\Default\History"
        elif browser == "Opera":
            return user_path + r"\AppData\Roaming\Opera Software\Opera Stable\History"
        elif browser == "Opera GX":
            return user_path + r"\AppData\Roaming\Opera Software\Opera GX Stable\History"
        elif browser == "Vivaldi":
            return user_path + r"\AppData\Local\Vivaldi\User Data\Default\History"
        elif browser == "Brave":
            return user_path + r"\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History"
        else:
            return None
    elif os_system == "Linux":
        if browser == "Chrome":
            return user_path + r"/.config/google-chrome/Default/History"
        elif browser == "Firefox":
            return user_path + r"/.mozilla/firefox/*.default-release/places.sqlite"
        elif browser == "Edge":
            return user_path + r"/.config/microsoft-edge/Default/History"
        elif browser == "Opera":
            return user_path + r"/.config/opera/History"
        elif browser == "Opera GX":
            return user_path + r"/.config/opera-gx/History"
        elif browser == "Vivaldi":
            return user_path + r"/.config/vivaldi/Default/History"
        elif browser == "Brave":
            return user_path + r"/.config/BraveSoftware/Brave-Browser/Default/History"
        else:
            return None
    else:
        messagebox.showerror("Error", f"Estás usando un sistema operativo desconocido: {os_system}")
        return None

def delete_session_history(browser):
    try:
        os_system = platform.system()
        
        history_path = browser_path_history(browser)
        if history_path is None:
            messagebox.showerror("Error", f"Navegador {browser} no soportado.")
            return
        
        close_browser(browser)  # Cerrar el navegador antes de eliminar el historial
        
        if os.path.exists(history_path):
            os.remove(history_path)
            messagebox.showinfo("Éxito", "Historial eliminado con éxito")
        else:
            messagebox.showerror("Error", f"No se pudo encontrar {history_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def is_browser_open(browser_name):
    for proc in psutil.process_iter(['name']):
        if browser_name.lower() in proc.info['name'].lower():
            return True
    return False

def close_browser(browser_name):
    def question(browser): 
        quest = messagebox.askyesno("Cerrar navegador", f"El navegador {browser} está abierto. ¿Quieres cerrarlo?")
        if quest:
            os_system = platform.system()
            if os_system == "Windows":
                subprocess.call(["taskkill", "/F", "/IM", f"{browser}.exe"])
            elif os_system == "Linux":
                subprocess.call(["pkill", "-f", browser])
            elif os_system == "Darwin":
                subprocess.call(["pkill", browser])
            else:
                messagebox.showerror("Error", f"Estás usando un sistema operativo desconocido: {os_system}")

def shutdown_system():
    os_system = platform.system()
    if os_system == "Windows":
        subprocess.call(["shutdown", "/s", "/t", "0"])
    elif os_system == "Linux" or os_system == "Darwin":
        subprocess.call(["shutdown", "-h", "now"])
    else:
        messagebox.showerror("Error", f"Estás usando un sistema operativo desconocido: {os_system}")

def main():
    def eliminar_cookies():
        browser_choice = selected_browser.get()
        if is_browser_open(browser_choice):
            close_browser(browser_choice)
        delete_session_cookies(browser_choice)

    def eliminar_historial():
        browser_choice = selected_browser.get()
        if is_browser_open(browser_choice):
            close_browser(browser_choice)
        delete_session_history(browser_choice)

    def eliminar_todo():
        browser_choice = selected_browser.get()
        if is_browser_open(browser_choice):
            close_browser(browser_choice)
        delete_session_cookies(browser_choice)
        delete_session_history(browser_choice)

    def apagar_sistema():
        browser_choice = selected_browser.get()
        if is_browser_open(browser_choice):
            close_browser(browser_choice)
        delete_session_cookies(browser_choice)
        delete_session_history(browser_choice)
        shutdown_system()

    root = Tk()
    root.title("Cookies Manager")
    root.geometry("400x300")  # Tamaño de la ventana aumentado

    selected_browser = StringVar(root)
    selected_browser.set("Chrome")

    browsers = ["Chrome", "Firefox", "Edge", "Opera", "Opera GX", "Vivaldi", "Brave"]

    # Crear un contenedor centrado
    container = ttk.Frame(root)
    container.place(relx=0.5, rely=0.5, anchor='center')

    label_browser = Label(container, text="Choose browser")
    label_browser.grid(row=0, column=0, padx=10, pady=10, sticky='e')  # Label en la primera columna

    browser_menu = OptionMenu(container, selected_browser, *browsers)
    browser_menu.grid(row=0, column=1, padx=10, pady=10, sticky='w')  # Menú desplegable en la segunda columna

    button_width = 20  # Ancho de todos los botones

    btn_eliminar_cookies = Button(container, text="Eliminar cookies", width=button_width, command=eliminar_cookies)
    btn_eliminar_cookies.grid(row=1, column=0, columnspan=2, pady=10)

    btn_eliminar_historial = Button(container, text="Eliminar historial", width=button_width, command=eliminar_historial)
    btn_eliminar_historial.grid(row=2, column=0, columnspan=2, pady=10)

    btn_eliminar_todo = Button(container, text="Eliminar todo", width=button_width, command=eliminar_todo)
    btn_eliminar_todo.grid(row=3, column=0, columnspan=2, pady=10)

    btn_apagar_sistema = Button(container, text="Eliminar todo y apagar", width=button_width, command=apagar_sistema)
    btn_apagar_sistema.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
