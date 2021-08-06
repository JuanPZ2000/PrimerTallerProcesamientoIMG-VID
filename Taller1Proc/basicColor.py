# basicColor
# Juan Pablo Zuluaga C 2021 PUJ Procesamiento de imagenes y video
import cv2
import os
import numpy as np


class basicColor:

    def __init__(self, path, image_name):
        # Con el path y el image_name se tiene el path_file de la imagen a procesar
        path_file = os.path.join(path, image_name)
        # Se lee la imagen del path_file
        self.image = cv2.imread(path_file)
        # Se rectifica que la imagen exista en el pc
        assert self.image is not None, "No hay ninguna imagen en  {}".format(path_file)

    def displayProperties(self):
        # Se toma el ancho y el alto de la imagen, se divide en 1M para tener el numero de MP de la imagen
        n_pixeles = self.image.shape[0] * self.image.shape[1] / 1000000
        print('Esta imagen tiene ' + str(n_pixeles) + ' MP')
        print('Y tiene ' + str(self.image.shape[2]) + ' canales')

    def makeBW(self):
        # Se realiza la conversion de la imagen a grises
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Se realiza el metodo otsu
        ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Se le da un nombre a la ventana donde aparecera la iamgen
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        # Se muestra la imagen
        cv2.imshow("Image", Ibw_otsu)
        # Se le da un tamaño a la ventana donde se mostrara la imagen
        cv2.resizeWindow("Image", 1280, 720)
        # Se muestra la imagen hasta que se cierre la ventana
        cv2.waitKey(0)
        # Se retorna la imagen
        return Ibw_otsu

    def colorize(self, h):
        # Se pregunta si h esta entre el rango permitido
        if 0 <= h <= 179:
            #Se convierte la imagen a formato HSV
            image_HSV = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            # Se separa la imagen en tres matrices diferentes
            H, S, V = cv2.split(image_HSV)
            # Se toma el h que el usuario ingreso y se multiplica por una matriz igual de grande a H original
            h_aux = h * np.ones_like(H)
            # Se une la nueva imagen con el nuevo h
            image_merge = cv2.merge((h_aux, S, V))
            # Se convierte la imagen a BGR
            image_final = cv2.cvtColor(image_merge, cv2.COLOR_HSV2BGR)
            # Se da un nombre a la ventana donde se mostrara la imagen
            cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
            # Se muestra la imagen
            cv2.imshow("Image", image_final)
            # Se le da un tamaño a la ventana donde se mostrara la imagen
            cv2.resizeWindow("Image", 1280, 720)
            # Se muestra la imagen hasta que se cierre la ventana
            cv2.waitKey(0)
            # Se retorna la imagen mostrada
            return image_final
        # Se evalua el caso donde el h ingresado no sea valido
        else:
            print('El numero ingresado de h no es valido, por favor ingrese un numero entre 0 y 179')
