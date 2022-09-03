from inference import *
from datetime import datetime

predictor = Predictor()
model = predictor.load_model()


predictor3 = Predictor()
predictor3.weights_path = r"C:\Users\Manju\Downloads\latest\exp2\weights\best.pt"
model3 = predictor3.load_model()


cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	frame_c = frame.copy()
	frame2 = cv2.flip(frame_c,1)
	t1 = datetime.now()
	predicted_image, detector_labels, coordinates = predictor.run_inference_hub(model,frame)
	t2 = datetime.now()
	print(f"Total inference time is !!!!! {(t2-t1).total_seconds()} seconds ")
	response = predictor.check_kanban()
	# print(response)

	t1 = datetime.now()
	predicted_image2, detector_labels2, coordinates2 = predictor3.run_inference_hub(model3,frame2)
	t2 = datetime.now()
	print(f"Total inference time is !!!!! {(t2-t1).total_seconds()} seconds ")

	print('**********************************************************************************')

	cv2.imshow('frame',predicted_image)
	cv2.imshow('frame2',predicted_image2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


