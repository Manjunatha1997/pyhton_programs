import cv2
import os

def video_to_frames(cam,out_folder_name,image_name):

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
            name =out_folder_name+image_name+ str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()


cam = cv2.VideoCapture("/home/manju/magnaflux/crack_video.mp4")
out_folder_name = "/home/manju/magnaflux/crack_video/"
image_name = "crack_video"

video_to_frames(cam,out_folder_name,image_name)




