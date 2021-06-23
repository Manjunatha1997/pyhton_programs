
import cv2
import redis
import numpy as np


r = redis.StrictRedis(host='localhost',port=6379,password=None)


def video_read(video):

	cap = cv2.VideoCapture(video)

	img_counter = 0

	while True:
		ret, frame = cap.read()

		if ret:
			retval, buffer = cv2.imencode('.jpg', frame)
			img1_bytes = np.array(buffer).tobytes()
			r.set(img_counter,img1_bytes)
			cv2.imshow('image',frame)
			img_counter += 1

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break


	cap.release()
	cv2.destroyAllWindows()


# video = 0

# video_read(video)











