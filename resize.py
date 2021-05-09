import glob
import cv2

path = '/home/manju/Downloads/ms_24_res/'

res = glob.glob(path+'*.jpg')

for file in res:
	print(file)

	img = cv2.imread(file)

	img = cv2.resize(img,(1080,720))
	cv2.imwrite(path+file.split('/')[-1],img)


