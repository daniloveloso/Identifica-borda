import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('teste5.jpg')



img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

arestas = cv2.Canny(img1, 100, 200)

def pint(imgg):

    for y in range (0, len(imgg)):
     for x in range (0, len(imgg[y])):
      cor = imgg[y][x]
      ret = 0
      if cor == 0 & ret == 0:
       cor = 200
       pass
      if cor == 255 & ret == 0:
       ret = 1
      if cor == 255 & ret ==1:
       ret = 0
    return imgg

pint(arestas)

cv2.imshow('te',arestas)
cv2.waitKey()
cv2.destroyAllWindows()