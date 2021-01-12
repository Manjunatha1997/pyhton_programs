import cv2
import os
cam = cv2.VideoCapture("/home/manju/Desktop/magnaflux/overlap.mp4")
out_folder_name = "/home/manju/Desktop/magnaflux/overlap"
image_name = "overlap_"
try:
    if not os.path.exists(out_folder_name):
        os.makedirs(out_folder_name)
except OSError:
    print('Error: Creating directory of',out_folder_name)

currentframe = 0
while (True):
    ret, frame = cam.read()
    if ret:
        name =out_folder_name+'/'+image_name+ str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
