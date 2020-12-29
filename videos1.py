import cv2
import datetime

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cap.set(3,640)
cap.set(4,480)

while cap.isOpened():
    ret, frame = cap.read()
    date = str(datetime.datetime.now())
    # text = cv2.putText(frame,"hello world",(10,50),1,cv2.FONT_HERSHEY_COMPLEX,(255,433,233),3)
    # date = cv2.putText(frame,date,(10,100),1,cv2.FONT_HERSHEY_COMPLEX,(122,211,222),1)
    # line = cv2.line(frame,(200,100),(100,200),(234,213,222),5)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
