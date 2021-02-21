import os

import xml.etree.ElementTree as ET

path = '/home/manju/Desktop/ddd/Manju/'



files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		tree = ET.parse(path+file)
		root = tree.getroot()
		l = [elt.tag for elt in root.iter()]
		if 'name' not in l:
			print(path+file)
				
		