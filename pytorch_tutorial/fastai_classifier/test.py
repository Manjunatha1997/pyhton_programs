import numpy as np
import cv2
import numpy as np

import string
import argparse

# from opt_module import *
from PIL import Image
from fastai.vision import *
# mp.set_start_method('spawn')
def load_classifier(opt):
    device = opt.device
    model=load_learner(opt.fastai_classifier_weights) 
    return model


def get_classifier_prediction(frame,classifier):
    frame=cv2.resize(frame,(224,224))
#     image = cv2.rotate(crop, cv2.ROTATE_90_CLOCKWISE,cv2.flip,cv2.brightnes,cv2) # Working on the rotation
                                
    img = Image(pil2tensor(frame, dtype=np.float32).div_(255))#.div_(255)
    pred=classifier.predict(img)   # getting predictions per frame
    # print(pred[0])
#     print(np.amax(to_np(pred[2])))
#     print(pred)
    prediction = str(pred[0])
#     pred = str(pred[2])
    # print(prediction)
    return prediction ,pred