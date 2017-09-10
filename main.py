import cv2, time, os, numpy as np

# initialize variables
threshold = 0.97

# create dictionary of filenames and occurances in all frames
occurances = {}
right = 0
wrong = 0

for trans in os.listdir('trans'):
    # splitext is to get rid of the file extension
    key = os.path.splitext(trans)[0]
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
        for trans in os.listdir('trans'):
            # splitext is to get rid of the file extension
            key = os.path.splitext(trans)[0]
            move = trans.split('_TRANS')

            # find the corresponding mask for the current transparent template
            for mask in os.listdir('masks'):
                moveMask = mask.split('_MASK')
                if move[0] == moveMask[0]:
                    break
            ms = "masks\\" + moveMask[0]
            mask = cv2.imread(ms)
            # set name of file to grab, can't just be trans
            tn = "trans\\" + trans

            # read in file, convert to grayscale, get width and height for later
            template_bgr = cv2.imread(tn)
            template_gray = cv2.cvtColor(template_bgr, cv2.COLOR_BGR2GRAY)
            w, h = template_gray.shape[::-1]
            data = np.zeros((h, w, 3), dtype=np.uint8)

            # set if a match in the frame has been found or not to false
            found = False
            results = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCORR_NORMED, data, mask)
            location = np.where(results >= threshold)
            rects = 0
            for pt in zip(*location[::-1]):
                if rects > 2:
                    break
                found=True
                rects += 1
                cv2.rectangle(frame_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    # only show frame if template match is found, then hit button to move on
            if found:
                cv2.imshow("Found " + trans, frame_bgr)
                ch = cv2.waitKey()
                if ch == 49:
                    #correct pairing, add to occurances, press 1
                    right += 1
                    occurances[key] += 1
                    cv2.destroyAllWindows()

                if ch == 48:
                    # incorrect pairing, add to occurances, press 0
                    wrong += 1
                    cv2.destroyAllWindows()


                if cv2.waitKey() == 27:
                    # exit program if escape is hit
                    cv2.destroyAllWindows()
                    exit()

print(occurances)
print("Correct: " + str(right))
print("Wrong: " + str(wrong))

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
