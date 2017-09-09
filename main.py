import cv2
import numpy as np
import time
import os

template_bgr = cv2.imread('template.jpg')
template_gray = cv2.cvtColor(template_bgr, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]


for filename in os.listdir('frames'):
    fn = "frames\\" + filename
    if os.path.isfile(fn):
        print(fn)
        frame_bgr = cv2.imread(fn)
        frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

        found = False
        results = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        location = np.where(results >= threshold)

        print(location)

        for pt in zip(*location[::-1]):
            found=True
            cv2.rectangle(frame_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

# only show frame if template match is found, then hit button to move on
        if found:
            cv2.imshow('Frame', frame_bgr)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# escape program if exit is hit
        if cv2.waitKey() == 27:
            cv2.destroyAllWindows()
            exit()



# WE HAVE
# large list of frames
# large list of templates, which are different button presses

# WE NEED TO DO
# detect characters in first frame, make bounding box
# track characetrs throughout the entire match, only search there for
#   corresponding templates
# loop though all frames, and all templates for each character in each frame to find
#   what button the player pressed
# If template matches, record corresponding button press and file number in text log for now
