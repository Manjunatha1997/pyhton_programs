import os
import glob
import xml.etree.ElementTree as ET
import cv2

path = 'C:\\Users\\lovel\\OneDrive\\Desktop\\plasmo\\plasmo_dataset\\images\\test\\'


# files = os.listdir(path)
files = glob.glob(path+'*.xml')


for file in files:

	tree = ET.parse(file)
	root = tree.getroot()
	for elt in tree.iter():
		# if elt.tag == 'name' and elt.text == 'Top_Right':
		if elt.tag == 'name' and elt.text == 'Bolt_Presence':
			elt.text = 'Bolts_Presence'
			print(elt.text)


	tree.write(file)
	# print(file)
		
