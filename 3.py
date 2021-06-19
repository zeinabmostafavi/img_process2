import cv2
import numpy as np


a = cv2.imread('3/brdorg.bmp')
b = cv2.imread('3/brdtsst.bmp')

b = cv2.resize(b, (960, 1280))

a = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
b = cv2.cvtColor(b, cv2.COLOR_RGB2GRAY)

rows, cols = a.shape


img_result = cv2.subtract(b, a)*2

cv2.imwrite('resultboard.jpg', img_result)
cv2.imshow('resultboard', img_result)
cv2.waitKey()
