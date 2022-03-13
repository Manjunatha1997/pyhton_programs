
import cv2

def resize_image(image_path,required_image_size):
    img = cv2.imread(image_path)
    cv2.resize(img,required_image_size[0],required_image_size[1])
    cv2.imwrite(image_path,img)

resize_image('sample_image.jpg',['640','480'])


