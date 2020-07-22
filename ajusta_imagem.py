import cv2
import numpy as np
import glob
import os

import time

timestr = time.strftime("%Y%m%d_%H%M%S")


print('\nDigite valores entre 0 e 255')

#Recebe valores de contraste e brilho
contrast = input('\nDigite um valor para o Contraste: ')
brightness = input('\nDigite um valor para o Brilho: ')

imagem = list()

#Varre as imagens no diretorio
for filename in glob.glob('*jpg'):
    print(filename)
    img = cv2.imread(filename)

    # Carrega as imagens
    # Considera 8 bits (0 to 255) por canal de cor
    method = 'opencv_way'   # or 'opencv_way'

    if method == 'numpy_way':
        # Converte para 16 bit (com sinal), permite valores < 0 e valores > 255
        img = np.int16(img)  

        #Formula adaptada do GIMP book(http://pippin.gimp.org/image_processing/chap_point.html)
        img = img*(contrast/127 + 1) - contrast + brightness

        img = np.clip(img, 0, 255)  # Ajusta valores de 0 a 255

        # Converte em 8 bits (sem sinal)
        img = np.uint8(img)

        
    elif method == 'opencv_way':
        b = brightness # brightness
        c = contrast  # contrast

        img = cv2.addWeighted(img, 1. + c/127., img, 0, b-c)
        print('Imagem Ajustada!')
        
    cv2.imwrite(timestr+'_result_%s' % filename, img)
