# 08/02/2024
# Day - 007

import sys
import os

# Agregar la ruta de la carpeta 'hangman_5' al sys.path
# Para que Python pueda encontrar los módulos en esa carpeta
sys.path.append(os.path.join(os.path.dirname(__file__), '..\hangman5')) 

# Ahora puedes importar el módulo 'hangman_art'
import hangman_art

print(hangman_art.logo)