import os
import glob


files = glob.glob("/home/manju/Desktop/pavithra/171120/imp/manju/K50T60_Glossy/*")

for file in files:
    os.rename(file,file+".jpg")