import cv2
import numpy as np
img1 = cv2.imread("simpsons.jpg")
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

template = cv2.imread("barts_face.jpg",0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = zip(*(np.where(res >= threshold)[::-1]))

for i in loc:
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),1)
    print(i,(i[0]+w,i[1]+h))


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()