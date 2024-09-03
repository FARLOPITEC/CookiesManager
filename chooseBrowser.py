import browser_cookie3
import requests

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

def get_cookies(browser_choose):
    # Seleccionar el navegador basado en la opción del usuario
    if browser_choose == "1":
        cookies = browser_cookie3.chrome()
    elif browser_choose == "2":
        cookies = browser_cookie3.firefox()
    elif browser_choose == "3":
        cookies = browser_cookie3.opera()      
    elif browser_choose == "4":
        cookies = browser_cookie3.opera_gx()  
    elif browser_choose == "5":
        cookies = browser_cookie3.vivaldi()
    elif browser_choose == "6":
        cookies = browser_cookie3.brave()
    elif browser_choose == "7":
        cookies = browser_cookie3.load()  # Carga las cookies de todos los navegadores compatibles
    else:
        print("Opción no válida.")
        return None

    return cookies

def main():
    browser_choice = choose_browser()
    cookies = get_cookies(browser_choice)

    if cookies:
        url = 'https://www.example.com'
        response = requests.get(url, cookies=cookies)
        print(response.content)

if __name__ == "__main__":
    main()