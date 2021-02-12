import os
import shutil
import xml.etree.ElementTree as ET


inp_path = "/home/manju/Desktop/test/"

xml_file = "/home/manju/Desktop/suprajit_13/MR_20.xml"

####################################################################

if not inp_path.endswith('/'):
	inp_path = inp_path+'/'


res  = os.listdir(inp_path)

for file in res:
	f = file.split('.')[0]+'.xml'	
	shutil.copyfile(xml_file,inp_path+f)
	

path = inp_path
files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		
		tree = ET.parse(path+file)
		
		for elt in tree.iter():
			if elt.tag == 'folder':
				elt.text = (path.split('/')[-2])

			if elt.tag == 'filename':
				elt.text = file.split('.')[0]+'.jpg'

			if elt.tag == 'path':
				elt.text = (path+file.split('.')[0]+'.jpg')

		tree.write(path+file)