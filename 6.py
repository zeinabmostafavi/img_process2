import cv2
import numpy as np


a = cv2.imread('6/Mona_Lisa.jpg')
a = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)

row, col = a.shape
mask = np.zeros((row, col), dtype='uint8')
mask[0:row, 0:80] = 30
mask[0:900, 80:col] = 30
img_result = (a//2 + mask//2)*3

cv2.imwrite('resultmonalisa.jpg', img_result)
cv2.imshow('resultmonalisa', img_result)
cv2.waitKey()
