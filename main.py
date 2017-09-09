import cv2
import numpy as np
import time

frame_bgr = cv2.imread('frame.jpg')
frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

results = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
location = np.where(results >= threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(frame_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', frame_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
