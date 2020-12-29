import os
import glob
import shutil

path = "/home/manju/Pictures/Webcam/"

out_path = "/home/manju/Pictures/RH/2SSP/"

files = os.listdir(path)

#starting count should be ZERO
count = 487
for file in files:
	count += 1
	os.rename(path+file,path+'batch_67_'+str(count)+'.jpg')

result = ""

for i in os.listdir("/home/manju/Pictures/Webcam/"):

	shutil.copyfile(path+i,out_path+i)

	result = result+i.split('.')[0]+ ','
	# result.append(i.split('.')[0])
print(result[:-1])

shutil.rmtree(path)