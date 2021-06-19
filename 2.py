import cv2

import numpy as np


def without_noise(num):
    images = []
    for i in range(1, 6):
        img = cv2.imread(f'2/{num}/{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        images.append(img)

    img_result = np.zeros(images[0].shape, dtype='uint8')
    for image in images:
        img_result += image//len(images)
    cv2.imwrite(f'output{num}.jpg', img_result)


without_noise(1)
without_noise(2)
without_noise(3)
without_noise(4)

img_output1 = cv2.imread('output1.jpg')
img_output2 = cv2.imread('output2.jpg')
img_output3 = cv2.imread('output3.jpg')
img_output4 = cv2.imread('output4.jpg')

# But since OpenCV reads images as arrays, we can concatenate arrays using the inbuilt cv2.hconcat()
# and cv2.vconcat() functions. After that, we display this concatenated image using cv2.imshow().
# cv2.hconcat([img1, img2]) —– horizontally concatenated image as output. Same for cv2.vconcat().
# ___________vertical_________________________
vconcat1 = cv2.vconcat([img_output1, img_output3])
vconcat2 = cv2.vconcat([img_output2, img_output4])
# ___________horizontally_________________________
hconcat = cv2.hconcat([vconcat1, vconcat2])
# ________________saveimg_______________________
cv2.imwrite('resultorg.jpg', hconcat)
cv2.imshow('resultorg', hconcat)
cv2.waitKey()
