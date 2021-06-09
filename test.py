import cv2 as cv 
import numpy as np
import pytesseract
import pyttsx3

cap = None
ret = None
frame = None
key = None
engine = pyttsx3.init()


cap = cv.VideoCapture(0)
while True:
  ret , frame = cap.read()
  cv.imshow('Window',frame)
  teks = pytesseract.image_to_string(frame)
  if teks is not None:
    print('Teks nya : ')
    print(teks)
    engine.say(teks)
    engine.runAndWait()
  key = cv.waitKey(2000)
  if key == (ord('q')):
    break
cv.destroyAllWindows()
cap.release()
