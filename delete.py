import os

import xml.etree.ElementTree as ET

path = '/home/manju/Desktop/ddd/Manju/'


class_names = []

files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		tree = ET.parse(path+file)
		root = tree.getroot()
		for elt in root.iter():
			if elt.tag == 'name':
				class_names.append(elt.text)


print(set(class_names))
				
		