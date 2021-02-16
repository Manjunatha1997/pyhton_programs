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


cam = cv2.VideoCapture("/media/manju/60FC-164B/chamfer presence_rh/WIN_20210212_17_26_11_Pro.mp4")
out_folder_name = "/media/manju/60FC-164B/Chamfer_Presence_RH"
image_name = "Chamfer_Presence_"

video_to_frames(cam,out_folder_name,image_name)




