import cv2
import os
from datetime import datetime

cam = cv2.VideoCapture("/home/manju/Downloads/WIN_20210621_15_13_38_Pro.mp4")
out_folder_name = "/home/manju/Desktop/suprajit_MR235/"
image_name = "MR235"


def video_to_frames(cam,out_folder_name,image_name):

    time = datetime.now()

    time = str(time).split(' ')
    time = time[0]


    if not out_folder_name.endswith('/'):
        out_folder_name = out_folder_name + '/'

    try:
        if not os.path.exists(out_folder_name):
            os.makedirs(out_folder_name)
    except OSError:
        print('Error: Creating directory of',out_folder_name)

    currentframe = 0
    while (True):
        ret, frame = cam.read()
        if ret:
            name =out_folder_name+image_name+'_'+time+ '_' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()


video_to_frames(cam,out_folder_name,image_name)


