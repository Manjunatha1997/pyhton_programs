import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = r'E:\11_july_2022_indomim\new_defects_chamfer_burr_\new_defects_chamfer_burr_\\'


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == 'thread_presence_112':
			elt.text = 'thread_absence_112'
			print(elt.text)
			# cv2.imwrite('D:\\indoData\\datasetjan11\\dents_extra\\35_19_hole_presence\\')


	tree.write(file)
	print(file)
		
