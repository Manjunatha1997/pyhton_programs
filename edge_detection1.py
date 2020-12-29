import cv2
import glob

files = glob.glob('/home/manju/Desktop/task/*.jpg')

for i in files:
    img = cv2.imread(i)
    img = cv2.GaussianBlur(img,(5,5),0)

    edge_detect_img = cv2.Canny(img,100,150)

    cv2.imshow(i[25:], edge_detect_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()