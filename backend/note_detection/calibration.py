import cv2
import numpy as np

from note_detection import create_range_mask

class Calibration:
    def __init__(self):
        points = []

    def generate_calibration(self, frame):
        frame = frame[:, 200:-300]

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        black_mask = create_range_mask(hsv, 'black')

        contours, _ = cv2.findContours(black_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        outimg = cv2.cvtColor(np.zeros_like(black_mask), cv2.COLOR_GRAY2BGR)

        

        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.015 * peri, True)
            if len(approx) == 4:
                x,y,w,h = cv2.boundingRect(approx)
                cv2.rectangle(outimg, (x,y), (x+w,y+h), (36,255,12), 2)

    
        cv2.imwrite('calib.png', outimg)

        

    
    def apply_calibration(self, frame):
        return frame



if __name__ == '__main__':
    frame = cv2.imread('board_img.png')
    calib = Calibration()
    calib.generate_calibration(frame)

