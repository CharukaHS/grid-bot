import time
import numpy as np
from PIL import ImageGrab
import cv2

import roi

def draw_lines(img, lines):
    try:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(img,(x1,y1),(x2,y2),(255,0,0),10)
    except:
        pass

def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    processed_image = cv2.Canny(processed_image, threshold1 = 50, threshold2 = 150)
    processed_image = cv2.GaussianBlur(processed_image, (5,5), 0)
    processed_image = roi.roi(processed_image)

    lines = cv2.HoughLinesP(processed_image, rho=1, theta=np.pi/180, threshold=180, minLineLength=100, maxLineGap=15)
    draw_lines(original_image, lines)

    # processed_image = cv2.addWeighted()
    return original_image

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_image(screen)
    print('FPS {}'.format(1/(time.time()-last_time)))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break