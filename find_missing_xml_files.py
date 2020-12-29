
import os

def find_missing(path):
	res = os.listdir(path)
	jpg,xml = [],[]

	for i in res:

		if i.endswith('.jpg'):
			k = i.split('.')
			jpg.append(k[0])
		
		else:
			if i.endswith('.xml'):
				k = i.split('.')
				xml.append(k[0])

	count = 0
	for i in jpg:
		if not i in xml:
			count += 1
			print("Missing items are: "+i+".jpg",count)
			# os.remove(path+i+'.jpg')

	print("Total xml are:",len(xml))
	print("Total jpg are:",len(jpg))
	

path = "/home/manju/Desktop/MR192/"

find_missing(path)
