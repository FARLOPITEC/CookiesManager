# CookiesManager

## Descripción
CookiesManager es una herramienta desarrollada en Python para gestionar las cookies de varios navegadores web. Esta herramienta permite eliminar cookies, historial y realizar otras acciones de privacidad en navegadores como Chrome, Firefox, Edge, Opera, Opera GX, Vivaldi y Brave.

## Instalación
Para utilizar este script, necesitas instalar las librerías `browser-cookie3` y `psutil`. Puedes instalarlas usando el siguiente comando:

## Uso
El script proporciona una interfaz gráfica para gestionar las cookies y el historial de los navegadores. Para ejecutar el script, simplemente usa el siguiente comando:
`python CookiesManagerGraphics.py`

También puedes ejecutar el script mediante un archivo batch que oculta la consola:
@echo off
cd "ruta del archivo"
start "" pythonw CookiesManagerGraphics.py

## Funcionalidades
Eliminar Cookies: Elimina las cookies de un navegador específico.
Eliminar Historial: Elimina el historial de navegación de un navegador específico.
Eliminar Todo: Elimina tanto las cookies como el historial de un navegador específico.
Eliminar Todo y Apagar: Elimina las cookies y el historial, y apaga el sistema.

## Navegadores Soportados
Google Chrome
Mozilla Firefox
Microsoft Edge
Opera
Opera GX
Vivaldi
Brave

```sh
pip install browser-cookie3 psutil
