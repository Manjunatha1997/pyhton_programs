from fastai.vision import *
from fastai.metrics import error_rate, accuracy, FBeta
from fastai.metrics import  *
from fastai.imports import *
import torchvision
from fastai import *
from fastai.torch_core import *
from fastai.layers import *
# from torchvision.models.densenet import densenet121
# from torchvision.models.vgg import vgg19_bn
import torchvision.models as TorchModels 
from sklearn.metrics import *
import warnings
warnings.filterwarnings('ignore')


dataset_dir = 'D:\indomim_tirupati\indoData\segregated\chamfer_thread_out'


path = Path(dataset_dir)

data = ImageDataBunch.from_folder(path, train='train', valid='test', 
                                  ds_tfms=get_transforms(do_flip=False),no_check=True,
                                  size=224, bs=2, num_workers=8)


learn = cnn_learner(data, models.resnet50, metrics = [accuracy])


learn.fit_one_cycle(100, 1e-3)

learn.save("best.hd5")


