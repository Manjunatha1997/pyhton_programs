import shutil
import glob
import os
import xml.etree.ElementTree as ET


path = '/home/manju/Downloads/image_data/crop_train_dir/'

out = '/home/manju/Downloads/image_data/train/'



files = os.listdir(path)

for file in files:
	if file.endswith('.xml'):
		xml_file = file
		jpg_file = file.split('.')[0]+'.jpg'
		png_file = file.split('.')[0]+'.png'

		print(xml_file)
		

		tree = ET.parse(path+file)

		for elt in tree.iter():
			if elt.tag == 'name':
				print(elt.text)

				if os.path.isdir(out+elt.text):
					shutil.copyfile(path+xml_file,out+elt.text+'/'+xml_file)
					try:
						shutil.copyfile(path+jpg_file,out+elt.text+'/'+jpg_file)
					except:
						shutil.copyfile(path+png_file,out+elt.text+'/'+png_file)

				else:
					os.mkdir(out+elt.text)
					shutil.copyfile(path+xml_file,out+elt.text+'/'+xml_file)
					try:
						shutil.copyfile(path+jpg_file,out+elt.text+'/'+jpg_file)
					except:
						shutil.copyfile(path+png_file,out+elt.text+'/'+png_file)


		print('******************************************************')