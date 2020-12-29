import numpy as np
import cv2
import glob

files = glob.glob("/home/manju/Desktop/crop_test/*.jpg")

img = cv2.imread("/home/manju/Desktop/crop_test/40.jpg")
img = cv2.resize(img,(800,600))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread("/home/manju/Desktop/crop_temp.jpg", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

thr = 0.68

loc = np.where(res >= thr)[::-1]
loc = zip(*loc)
for i in loc:
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(255,0,0),2)
    print(w,h,i)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
