import cv2
import os
# Input path, and Path must be ends with '/'
inp_path = '/home/manju/Downloads/m2/'

# Creating output folder path
# Path must be ends with '/'
out_path = '/home/manju/Desktop/task/outt/'

# Create a folder is not exists
if not os.path.isdir(out_path):
    os.mkdir(out_path)

# Reading all files with os module
files = os.listdir(inp_path)
for file in files:
    if file.endswith('.jpg'):
        # Reading all images in the given folder
        img = cv2.imread(inp_path+file,0)

        # Applying adaptive thresholding
        thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

        # Write/Save it into a output folder
        cv2.imwrite(out_path+file,thr)
    else:
        print('skipping file is :',file)