import os


res = os.listdir('D:\\schneider\\images_with_txt\\images_with_txt\\')

for i in res:
	
	# x = res+i
	# print(x)
	# file_size = os.path.getsize('d:/file.jpg')
	# print(i,os.path.getsize('D:\\schneider\\images_with_txt\\images_with_txt\\'+i))
	if os.path.getsize('D:\\schneider\\images_with_txt\\images_with_txt\\'+i) == 0:
		print('s')
