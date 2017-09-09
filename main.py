import cv2, time, os, numpy as np

# initialize variables
threshold = 0.875

# create dictionary of filenames and occurances in all frames
occurances = {}

for template in os.listdir('templates'):
    # splitext is to get rid of the file extension
    key = os.path.splitext(template)[0]
    occurances[key] = 0

# loop through all frame files
for frame in os.listdir('frames'):
    # set name of file to grab, can't just be filename
    fn = "frames\\" + frame

    if os.path.isfile(fn):
        # read in file and convert to grayscale
        frame_bgr = cv2.imread(fn)
        frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

        # another for loop here to check every template on the frame
        for template in os.listdir('templates'):
            # splitext is to get rid of the file extension
            key = os.path.splitext(template)[0]

            # set name of file to grab, can't just be template
            tn = "templates\\" + template

            # read in file, convert to grayscale, get width and height for later
            template_bgr = cv2.imread(tn)
            template_gray = cv2.cvtColor(template_bgr, cv2.COLOR_BGR2GRAY)
            w, h = template_gray.shape[::-1]

            # set if a match in the frame has been found or not to false
            found = False
            results = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            location = np.where(results >= threshold)

            for pt in zip(*location[::-1]):
                found=True
                cv2.rectangle(frame_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    # only show frame if template match is found, then hit button to move on
            if found:
                occurances[key] += 1
                cv2.imshow("Found " + template, frame_bgr)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # exit program if escape is hit
            if cv2.waitKey() == 27:
                cv2.destroyAllWindows()
                exit()

print(occurances)

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
