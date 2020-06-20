import cv2, os, glob, sys
import numpy as np
from matplotlib import pyplot as plt

if len(sys.argv) == 3:
    background = cv2.imread(sys.argv[1])
    image = cv2.imread(sys.argv[2])
elif len(sys.argv) == 2:
    print('ERROR :plese provide two image paths "Backround image" and "Test image"')
else :
    print('No input provided')
    print('running on sample images')
    background = cv2.imread('background.jpg')
    image = cv2.imread('testforground.jpg')


shape = (200, 200)
bg = cv2.resize(background, shape)
# gbg = cv2.cvtColor(bg, cv2.COLOR_RGB2GRAY)
gbg = bg[:,:,2]
img = cv2.resize(image, shape)
gimg = img[:,:,2]
# gim = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.subplot(1,2,1),plt.imshow(bg),plt.title('Background Image') #thumb
plt.subplot(1,2,2),plt.imshow(img),plt.title('Test image') #erode1
plt.show()
sub_image = gbg - gimg
abssub_img = cv2.absdiff(gbg, gimg)
plt.subplot(1,2,1),plt.imshow(sub_image),plt.title('Subtraction') #thumb
plt.subplot(1,2,2),plt.imshow(abssub_img),plt.title('Absolute Subtraction') #erode1
plt.show()
kernel = np.ones((9, 9), np.uint8) 

gausianabs = cv2.GaussianBlur(abssub_img,(3,3),0 )
plt.title("HIstogramm for given Image'  ")
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
#hist function is used to plot the histogram of an image.
plt.hist(abssub_img)
plt.show()

_, binary = cv2.threshold(gausianabs, 50, 255, cv2.THRESH_BINARY)
eroded = cv2.erode(binary, kernel, iterations=1)
# binaryimage = [binary, binary, binary]
plt.subplot(1,2,1),plt.imshow(binary),plt.title('binary_image') #thumb
plt.subplot(1,2,2),plt.imshow(eroded),plt.title('Erroded') #erode1
plt.show()
dark = np.zeros((200, 200, 3), np.uint8)
dark[:,:,0] = cv2.bitwise_and(img[:,:,0], eroded)
dark[:,:,1] = cv2.bitwise_and(img[:,:,1], eroded)
dark[:,:,2] = cv2.bitwise_and(img[:,:,2], eroded)
plt.subplot(1,3,1),plt.imshow(img),plt.title('Input') #erode1
plt.subplot(1,3,2),plt.imshow(bg),plt.title('Background') #erode1
plt.subplot(1,3,3),plt.imshow(dark[:,:,:]),plt.title('Result') #erode1
# plt.imshow(dst)
plt.show()

