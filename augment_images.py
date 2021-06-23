


# resize 1920x1080
# color_contrast (higher,lower)

# inp : 4 images 
# output :  15 images



import cv2
import glob

path = '/home/manju/Desktop/aug/all/*.jpg'

out = '/home/manju/Desktop/aug/all_out/'

res = glob.glob(path)

for file in res:
	image_name = file.split('/')[-1]
	img = file

	img = cv2.imread(img)
	alpha = 1.5 # Contrast control (1.0-3.0)
	beta = 0 # Brightness control (0-100)

	adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
	adjusted1 = cv2.convertScaleAbs(img, alpha=alpha-3.0, beta=beta)

	resized = cv2.resize(img,(1920,1080))

	cv2.imwrite(out+'original_'+image_name,img)
	cv2.imwrite(out+'highContrast_'+image_name,adjusted1)
	cv2.imwrite(out+'lowContrast_'+image_name,adjusted)
	cv2.imwrite(out+'resized_'+image_name,resized)







