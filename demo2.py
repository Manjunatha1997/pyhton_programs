
import cv2
import numpy as np


img = cv2.imread('/home/manju/Downloads/MSIL/ushas_Mastic_Sealant_04_16/img6_msil_14_5_16_04_2021_26 (cp).jpg')
img = cv2.imread('/home/manju/Downloads/MSIL/Ex/break4.jpg')
img = cv2.resize(img,(800,500))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr = cv2.threshold(gray,55,255,1)



cv2.imshow('image',img)
cv2.imshow('gray',gray)
cv2.imshow('thr',thr)

cv2.waitKey(0)



