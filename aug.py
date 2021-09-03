import glob
import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import os,shutil
import xml.etree.ElementTree as ET
import xml
import cv2
import xmltodict
import json
import xml.etree.cElementTree as e
import numpy as np
import uuid 
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import sys
import time
import threading
from multiprocessing import Process


path = 'C:\\Users\\lovel\\OneDrive\\Desktop\\testaug\\'

res = os.listdir(path)

print(res)

for file in res:
    if file.endswith('.xml'):
        tree = e.parse(path+file)
        for elt in tree.iter():
            print(elt.tag)

            


