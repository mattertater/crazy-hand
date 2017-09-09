import cv2
import numpy as np
import time
import os
print("sdikgvubwei")
template_bgr = cv2.imread('template.jpg')
template_gray = cv2.cvtColor(template_bgr, cv2.COLOR_BGR2GRAY)

for filename in os.listdir('frames'):
    fn = "frames\\" + filename
    if os.path.isfile(fn):
        frame_bgr = cv2.imread(fn)
        frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
        w, h = frame_gray.shape[::-1]

        results = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        location = np.where(results >= threshold)

        for pt in zip(*location[::-1]):
            cv2.rectangle(frame_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
            cv2.imshow('Frame', frame_bgr)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# nested loop, look through every template on every frame, and record matches
