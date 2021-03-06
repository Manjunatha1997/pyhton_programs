import os

import xml.etree.ElementTree as ET

path = '/home/manju/rough_extra/'



files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		tree = ET.parse(path+file)
		root = tree.getroot()
		for elt in tree.iter():
			if elt.tag == 'name' and elt.text == 'Chamfer_Absence':
				print(elt.text)
				elt.text = 'Chamfer_Presence'

		# tree.write(path+file)
		