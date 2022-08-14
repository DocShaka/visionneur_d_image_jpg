# Createur < Doc.Shaka >
# -*- coding: utf-8 -*-

# Installation des librairy

import os
from os import *

system("pip install tqdm")
system("pip install io")
system("pip install PySimpleGUI")
system("pip install PIL")
system("cls")


# Import des Librairy

from tqdm import tqdm
import io
import PySimpleGUI as sg
from PIL import Image

# Variables

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

# Ascii Art

print ()
print ( 95 * "_" )
print ("__________________________________Visionneur_d'images_JPG______________________________________")
print ( 95 * "_" )
print ()

# Code Pure

print ()
print ("\tChargement du programme de demandé par l'utilisateur")
print ()
for i in tqdm(range(100000000)): # Range = durée de chargement
    pass
print ()

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load"),
        ],
    ]
    window = sg.Window("Visionneur D'images", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()
