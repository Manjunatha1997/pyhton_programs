
from genericpath import isdir
from glob import glob
import os
import xml.etree.ElementTree as ET
import cv2
import shutil



def move_file(in_file,out_dir):
	if not os.path.exists(in_file):
		return "input file does not exists"

	base_file = os.path.basename(in_file)
	out_file = os.path.join(out_dir,base_file)

	if not os.path.isdir(out_dir):
		os.makedirs(out_dir)
		shutil.move(in_file,out_file)
	else:
		shutil.move(in_file,out_file)
	return True

def find_all_classes(path):
	class_names = []
	files = os.listdir(os.path.join(path))
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(os.path.join(path,file))
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)				
	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)
	return temp	


def find_extra_images(input_path,remove=False,move=None):
	"""

	"""
	## check path 
	if not os.path.exists(input_path):
		return "incorrect path"

	check_file_type = ['jpg','JPG','png','PNG','bmp','BMP']

	files = os.listdir(input_path)
	images, xmls = [], []

	for file in files:
		file_name = file.split('.')[0]
		file_type = file.split('.')[-1]

		if (file_type in check_file_type) and (file_type != 'xml'): 
			images.append(file_name+'.'+file_type)
		if file_type == 'xml':
			xmls.append(file_name)

	extra_images = []

	for img in images:
		imgg = img.split('.')[0]
		imgg = imgg.replace(input_path,'')
		if not imgg in xmls:
			extra_images.append(os.path.join(input_path, img))


	if remove == True:
		for ff in extra_images:
			os.remove(ff)
		# return extra_images,len(extra_images),"Deleted extra images"
		return {'extra_images':extra_images,'count':len(extra_images),'message':"Deleted extra images"}


	if move:
		for ff in extra_images:
			mf = move_file(ff,move)
		return {'extra_images':extra_images,'count':len(extra_images),'message':f"moved extra images to {move}"}

	return {"extra_images":extra_images,"count":len(extra_images),"message":f"found extra {len(extra_images)} images"}


def find_no_class_names(input_path,remove=False):
	if not os.path.isdir(input_path):
		return f"{input_path} path does not exists."
	
	files = os.listdir(input_path)
	empty_names = []
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(os.path.join(input_path,file))
			root = tree.getroot()
			l = [elt.tag for elt in root.iter()]
			if 'name' not in l:
				empty_names.append(os.path.join(input_path,file))
	print(empty_names,'**********')
	if remove == True:
		for ef in empty_names:
			os.remove(ef)
		return f"{len(empty_names)} files deleted."
	return empty_names


def rename_class_name(folder_path, old_class, new_class):
	if not os.path.isdir(folder_path):
		return {"message":"Folder not exists"}

	files = glob(os.path.join(folder_path,'*.xml'))
	for file in files:
		tree = ET.parse(file)
		for elt in tree.iter():
			if elt.tag == 'name' and elt.text == old_class:
				elt.text = new_class
		tree.write(file)

	return {"message":f"changed from {old_class} to {new_class}"}

if __name__ =="__main__":
	# resp= find_extra_images(r'D:\sansera_conrod_burr\burr\test',remove=True,move=None)
	# # resp = find_no_class_names(r'D:\sansera_conrod_burr\burr\test',remove=True)
	# print(resp)

	resp = rename_class_name(r'D:\sansera_conrod_burr\burr\test')
	print(resp)

	




