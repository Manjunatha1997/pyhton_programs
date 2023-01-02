from glob import glob
from matplotlib.pyplot import imshow
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
import cv2
import glob
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory


for i in glob.glob(r'C:\Users\Manju\Downloads\ups_box\annotat\exp2\crops\model\\*.jpg'):
    out = i.split('\\')[-1]



    img = cv2.imread(i)

    result = ocr.ocr(img, cls=True)
    print(result)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    
    im_show = draw_ocr(img, boxes, txts, scores, font_path='./simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(r"C:\Users\Manju\Downloads\ups_box\annotat\exp2\crops\model\\"+out+'_res.jpg')



