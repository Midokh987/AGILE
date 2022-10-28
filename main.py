import cv2
import numpy as nu

img=cv2.imread("img.png", cv2.IMREAD_UNCHANGED)
red_channel=img[:,:,2]
red_img=nu.zeros(img.shape)
red_img[:,:,2]=red_channel
cv2.imwrite('red_img.png',red_img)
t=cv2.imread("red_img.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("img",t)
cv2.waitKey()