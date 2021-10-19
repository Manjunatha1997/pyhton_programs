import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = 'D:\\indomim\\indo_auto_data\\cold_material\\'


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == 'cold_material':
			elt.text = 'defect'
			# print(elt.text)


	tree.write(file)
	# print(file)
		
