
import cv2
import numpy as np

images = []

for i in range(1, 14):
    img = cv2.imread(f'5/{i}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    images.append(img)

img_result = np.zeros(images[0].shape, dtype='uint8')

for image in images:
    img_result += image//len(images)


cv2.imwrite('result.jpg', img_result)
cv2.imshow('result', img_result)
cv2.waitKey()
