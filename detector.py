import cv2
import pandas as pd
face_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_alt.xml')
cam=cv2.VideoCapture(0)
#rec=cv2.createLBPHFaceRecognizer();
rec=cv2.face.createLBPHFaceRecognizer();
#rec=cv2.face.LBPHFaceRecognizer_create();
rec.load("recognizer\\trainingData.yml")
#rec.read("recognizer\trainingData.yml")
#print(res)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = img[y:y+h, x:x+w]
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         id,conf=rec.predict(roi_gray)
         font=cv2.FONT_HERSHEY_SIMPLEX
         if id==1:
            id2="Minu"
         elif id==2:
              id2="Anila"
         elif id==3:
              id2="brijesh"
         elif id==8:
              id2="Cyril"
         elif id==10:
               id2="Jeny"
         elif id==12:
               id2="Neenu"
         elif id==40:
                id2="Neha"
         #cv2.putText(img, (x,y+h),str(id),font,255,2,cv2.LINE_AA)
         #cv2.putText(img,id2,(x,y+h),  gray, 4,(255,255,255),2,cv2.LINE_AA)
         cv2.putText(img, id2, (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA) 
         #cv2.putText(cv2.fromarray(img),str(id),(x,y+h),gray,255)
    cv2.imshow('img',img)
    k=cv2.waitKey(30)&0xff
    if k==27:
        break
cam.release()
cv2.destroyAllWindows()
