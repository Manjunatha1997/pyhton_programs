import cv2
import numpy as np
img = cv2.imread('/home/manju/Pictures/image.jpg')
img = cv2.resize(img,(640,480))

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(gray_img,127,255,0)
_,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print(contours,type(contours))
print(len(contours))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,0,255),2)

cv2.imshow('image',img)
cv2.imshow('thr',thr)
cv2.waitKey(0)

