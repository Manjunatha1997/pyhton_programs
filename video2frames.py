import cv2
import os
cam = cv2.VideoCapture("/home/manju/Desktop/suprajith/MR192.mp4")
out_folder_name = "MR192"
try:
    if not os.path.exists(out_folder_name):
        os.makedirs(out_folder_name)
except OSError:
    print('Error: Creating directory of',out_folder_name)

currentframe = 0
while (True):
    ret, frame = cam.read()
    if ret:
        name = './'+out_folder_name+'/MR192_' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
