import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('roman-logo.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,4)

for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  crop_face=img[y:y+h,x:x+w]
  cv2.imwrite(str(w)+str(h)+'-face.png',crop_face)

cv2.imshow('img',img)
cv2.imshow("imgcropped",crop_face)
cv2.waitKey()