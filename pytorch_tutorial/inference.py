import torch
import os
import glob
import cv2
import numpy as np


class Predictor():
	def __init__(self):
		self.model_dir = 'D:\\yolov5_auto'
		self.weights_path = 'yolov5s.pt'
		self.common_confidence = 0.1
		self.common_iou = 0.45
		self.line_thickness = None
		## If your renaming labels then defects names should be renamed labels , for ex. your label is 'cell phone' if you want to rename that to 'Mobile Phone' then defecet should be 'Mobile Phone'
		self.defects = ['Cell Phone'] #['bus','chair','tv','bottle','person']
		self.ind_thresh = {} #{'bus':0.1,'person':0.1,'chair':0.1}
		self.rename_labels = {'cell phone':'Cell Phone'} # {'person':'manju'}
		## avoid labels with in the given co-ordinates
		self.avoid_labels_cords = [] # [{'xmin':0,'ymin':82,'xmax':640,'ymax':480}]

		##
		self.detector_predictions = None # This will update from the detector predictions

	def load_model(self):
		model = torch.hub.load(self.model_dir,'custom',path=self.weights_path,source = 'local')
		model.conf = self.common_confidence
		model.iou = self.common_iou
		return model

	def run_inference_hub(self,model, image):
		results = model(image)
		labels = results.pandas().xyxy[0]
		labels = list(labels['name'])
		result_dict = results.pandas().xyxy[0].to_dict()
		labels_ = []
		coordinates = []
		for i in range(len(labels)):
			xmin = list(result_dict.get('xmin').values())[i]
			ymin = list(result_dict.get('ymin').values())[i]
			xmax = list(result_dict.get('xmax').values())[i]
			ymax = list(result_dict.get('ymax').values())[i]
			c = list(result_dict.get('class').values())[i]
			name = list(result_dict.get('name').values())[i]
			confidence = list(result_dict.get('confidence').values())[i]
	
			## avoid labels with the given co ordinates
			skip = None
			if self.avoid_labels_cords:
				for crd in self.avoid_labels_cords:
					if round(xmin) >= crd['xmin'] and round(ymin) >= crd['ymin'] and round(xmax) <= crd['xmax'] and round(ymax) <= crd['ymax']:
						skip = True
			if skip :
				continue


			
			## line width
			line_width = self.line_thickness or max(round(sum(image.shape) / 2 * 0.003), 2)

			## Checking individual threshold for wach label 
			if name in self.ind_thresh:
				try:
					if self.ind_thresh.get(name) <= confidence:

						p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
						
			
						if name:
							namer = self.rename_labels.get(name)
							if namer is None:
								name = name
							else:
								name = namer			
							
							## Bounding color   
							if name in self.defects:
								color = (0,0,255) # Red color bounding box 
							else:
								color = (0,128,0) # Green color bounding box 


							cv2.rectangle(image, p1, p2, color, thickness=line_width, lineType=cv2.LINE_AA)
							
							tf = max(line_width - 1, 1)  # font thickness
							

							w, h = cv2.getTextSize(name, 0, fontScale=line_width / 3, thickness=tf)[0]  # text width, height
							outside = p1[1] - h - 3 >= 0  # label fits outside box
							p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
							cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
							coordinates.append({name:[int(xmin),int(ymin),int(xmax),int(ymax)]})
							
							cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, line_width / 3, (255,255,255),
										thickness=tf, lineType=cv2.LINE_AA)
								
							labels_.append(name)

							
				except:
					pass
			
			## If not individual threshold
			else:
				# line_width or max(round(sum(im.shape) / 2 * 0.003), 2)
				p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))	

				
			
				if name:
					namer = self.rename_labels.get(name)
					if namer is None:
						name = name
					else:
						name = namer
					
					## Bounding color   
					if name in self.defects:
						color = (0,0,255) # Red color bounding box 
					else:
						color = (0,128,0) # Green color bounding box
					
					cv2.rectangle(image, p1, p2, color, thickness=line_width, lineType=cv2.LINE_AA)

					
					tf = max(line_width - 1, 1)  # font thickness
					# tf = self.line_thickness
					w, h = cv2.getTextSize(name, 0, fontScale=line_width / 3, thickness=tf)[0]  # text width, height
					outside = p1[1] - h - 3 >= 0  # label fits outside box
					p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
					cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)  # filled
					coordinates.append({name:[int(xmin),int(ymin),int(xmax),int(ymax)]})

					
					cv2.putText(image, name, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, line_width / 3, (255,255,255),
								thickness=tf, lineType=cv2.LINE_AA)
					labels_.append(name)			
					

		self.detector_predictions = labels_
		for img in results.imgs:
			return img, labels_, coordinates

	def check_kanban(self):
		defect_list = []
		for i in self.detector_predictions:
			if i in self.defects:
				defect_list.append(i)

		if bool(defect_list):
			is_accepted = "Rejected"
		else:
			is_accepted = "Accepted"
		return is_accepted


cap = cv2.VideoCapture(0)
predictor = Predictor()
model = predictor.load_model()

while True:
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	frame_c = frame.copy()
	predicted_image, detector_labels, coordinates = predictor.run_inference_hub(model,frame)
	status = predictor.check_kanban()
	print(status)
	cv2.imshow('frame',predicted_image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
