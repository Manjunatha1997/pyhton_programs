import os
import xml.etree.ElementTree as ET

path = r'E:\11_july_2022_indomim\dent_cum40_flagged\dent_cum40_flagged\\'

def all_class_names(path):
	class_names = []
	files = os.listdir(path)
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(path+file)
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)
					# print(file)
				if elt.tag == 'name' and elt.text == 'solder_bridge':
					print(file)
		

		

	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)

	# print(class_names)
	print(temp)

all_class_names(path)

# ['RedSpring', 'Screws', 'Spring_Absence', 'Spring_Presence']
# ['RedSpring', 'Screws', 'Spring_Absence', 'Spring_Presence']


# RedSpring = 643 + 159
# Screws = 1947 + 484
# Spring_Absence = 457 + 118
# Spring_Presence = 2112 + 519