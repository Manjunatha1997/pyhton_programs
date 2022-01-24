import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = 'D:\\indoData\\datasetjan11\\dents_extra\\dents_extra\\'


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == '35_19_hole_presence':
			# elt.text = 'chamfer_presence'
			print(elt.text)
			cv2.imwrite('D:\\indoData\\datasetjan11\\dents_extra\\35_19_hole_presence\\')


	# tree.write(file)
	# print(file)
		
