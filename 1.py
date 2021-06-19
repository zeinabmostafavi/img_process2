import cv2
import numpy as np


a = cv2.imread('img_processing2/1/a.tif')
b = cv2.imread('img_processing2/1/b.tif')

a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)

img_result = cv2.subtract(b, a)
rows = img_result.shape[0]
cols = img_result.shape[1]
# __________process_________________
for i in range(rows):
    for j in range(cols):
        img_result[i, j] = 255-img_result[i, j]


cv2.imwrite('result.jpg', img_result)
cv2.imshow('output', img_result)
cv2.waitKey()
