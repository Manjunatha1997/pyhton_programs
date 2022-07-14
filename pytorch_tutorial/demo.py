import torch
import os
import glob
import cv2



# Model
model = torch.hub.load('D:\\yolov5_auto', 'yolov5s', pretrained=True)

# Images
dir = 'D:\\yolov5_auto\\data\\images\\*'

res = glob.glob(dir)

imgs = [cv2.imread(img) for img in res]
# Inference
results = model(imgs)
results.print()  # or .show(), .save()

print(results)


# results.save()


