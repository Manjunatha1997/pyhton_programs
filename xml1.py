import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = '/home/manju/Desktop/bewww/train/'

out_path = '/home/manju/Desktop/bewww/Top_Right/'

if not os.path.isdir(out_path):
	os.mkdir(out_path)

# files = os.listdir(path)
files = glob.glob(path+'*.xml')


c = 0
for file in files:
	img = file.split('.')[0] + '.jpg'
	img = cv2.imread(img)
	
	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == 'Top_Right':
			print(elt.tag)

			# dic = {}
			
			# for i in elt:
			# 	dic[i.tag] = int(i.text)

			# # crop_img = img[ymin:ymax, xmin:xmax]
			
			# crop_img = img[dic['ymin']:dic['ymax'],dic['xmin']:dic['xmax']]
			# # cv2.imwrite(out_path+str(c)+'.jpg',crop_img)
			# c += 1
			# dic = {}
			


	# tree.write(path+file)
		
