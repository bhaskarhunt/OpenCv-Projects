#Create a Folder named imagerotation which will contain the images if you want to save 
import numpy as np
import cv2, os, glob, random
from matplotlib import pyplot as plt
image_center = (100, 100)
shape = (200, 200)
image = cv2.imread('rotate.jpg')
img = cv2.resize(image, shape)
np.random.seed(1)

path = 'imagerotation'
for i in range(20):
    rot  = cv2.getRotationMatrix2D(image_center, i*18, 1.0)
    rotimg = cv2.warpAffine(img, rot, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    cv2.imshow('frame', rotimg)
    cv2.waitKey(200)
    # Comment the part below if you Do not want to save the images
    try:
        filename = 'rot_{}.png'.format(i)
        dest = os.path.join(path, filename)
        cv2.imwrite(dest, rotimg, [cv2.IMWRITE_JPEG_QUALITY, 100])
    except :
        print('image not saved')
