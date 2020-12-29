import os


import xml.etree.ElementTree as ET


path = '/home/manju/Downloads/m2_done/m2/'

files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		print(file)
		print('-'*50)
		tree = ET.parse(path+file)
		root = tree.getroot()

		for elt in root.iter():
			# print(elt.tag,elt.text)
			if elt.tag == 'name':
				print(elt.tag,elt.text)
				elt.text = 'updated...'
				print(elt.tag,elt.text)
		print('*'*50)

		tree.write(path+file)
		