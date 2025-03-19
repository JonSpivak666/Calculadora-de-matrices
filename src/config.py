# src/config.py

import os

# Obtener la ruta absoluta de la carpeta del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "../assets/images")

# Configuración general de la aplicación
APP_TITLE = "Calculadora de Matrices"
APP_SUBTITLE = "Una herramienta matemática con funciones avanzadas"

# Configuración de colores para la interfaz
COLORS = {
    "background": "#ffffff",  # Fondo blanco
    "text": "#333333",        # Texto oscuro
    "primary": "#004d40",     # Verde oscuro elegante
    "secondary": "#ffb300",   # Ámbar
    "accent": "#1976d2"       # Azul
}

# Ruta de las imágenes de los escudos con rutas absolutas
IMAGES = {
    "unam": os.path.abspath(os.path.join(IMAGES_DIR, "Logo_UNAM_A-02.png")),
    "fes": os.path.abspath(os.path.join(IMAGES_DIR, "logo_fes.png")),
    "otro": os.path.abspath(os.path.join(IMAGES_DIR, "logo_ingcivil.png"))
}

# Verificar que los archivos de imagen existen
for key, path in IMAGES.items():
    if not os.path.exists(path):
        print(f"⚠️ Advertencia: No se encontró la imagen '{key}' en '{path}'")


