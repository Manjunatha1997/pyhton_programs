import glob
import cv2

path = r'D:\Bridgestone\images\splice bare\\'

res = glob.glob(path+'*.bmp')

for file in res:
	print(file)
	img = cv2.imread(file)
	img = cv2.resize(img,(640,480))
	cv2.imwrite(path+file.split('\\')[-1],img)


