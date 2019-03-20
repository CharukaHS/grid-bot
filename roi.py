''' Define Range of Interest '''
import numpy as np
import cv2

vertices = np.array([[300,220],[0, 320], [0, 440], [20, 420], [780, 420], [800, 440], [800, 320], [500,220]])

def roi(img):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, [vertices], 225)
    masked = cv2.bitwise_and(img, mask)
    return masked

