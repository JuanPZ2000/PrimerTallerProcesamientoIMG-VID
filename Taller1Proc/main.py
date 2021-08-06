# Juan Pablo Zuluaga C 2021 PUJ Procesamiento de imagenes y video

from basicColor import basicColor
import cv2
import os
import sys


if __name__ == '__main__':
    # Pide la ruta de la imagen
    path = input('Ingrese el path de donde esta ubicada su imagen: ')
    image_name = input('Ingrese el nombre de su imagen: ')
    # Se crea la clase con los argumentos necesarios
    basicColor1 = basicColor(path, image_name)
    # Se usa el metodo displayProperties para ver los MP de la imagen y los canales
    basicColor1.displayProperties()
    # Se usa el metodo para convertir la imagen a BW
    imagen_BW = basicColor1.makeBW()
    # Se le pide al usuario el valor de h, el cual entra como unico argumento al metodo colorize
    h = int(input('Ingrese el valor de hue con el que quiere realizar la funcion colorize: '))
    imagen_colorize = basicColor1.colorize(h)
