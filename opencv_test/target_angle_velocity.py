import cv2 as cv
import numpy as np
import sys
import os
import logging
import geom_util as geom
import roi
import track_conf as tconf

T = tconf.threshold
Roi = roi.ROI()

def balance_pic(image):
    global T
    ret = None
    direction = 0
    for i in range(0, tconf.th_iterations):
        rc, gray = cv.threshold(image, T, 255, 0)
        crop = Roi.crop_roi(gray)

        nwh = cv.countNonZero(crop)
        perc = int(100 * nwh / Roi.get_area())
        if perc > tconf.white_max:
            if T > tconf.threshold_max:
                break
            if direction == -1:
                ret = crop
                break
            T += 10
            direction = 1
        elif perc < tconf.white_min:
            if T < tconf.threshold_min:
                break
            if  direction == 1:
                ret = crop
                break

            T -= 10
            direction = -1
        else:
            ret = crop
            break
    return ret

def adjust_brightness(img, level):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    b = np.mean(img[:,:,2])
    if b == 0:
        return img
    r = level / b
    c = img.copy()
    c[:,:,2] = c[:,:,2] * r
    return cv.cvtColor(c, cv.COLOR_HSV2BGR)

def prepare_pic(image):
    global Roi
    global T
    height, width = image.shape[:2]

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (9, 9), 0) # might be able to reduce the kernel size

    if Roi.get_area() == 0:
        Roi.init_roi(width, height)

    return balance_pic(blurred), width, height

def find_main_countour(image):
    cnts, hierarchy = cv.findContours(image, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    C = None
    if cnts is not None and len(cnts) > 0:
         C = max(cnts, key = cv.contourArea)

    if C is None:
        return None, None

    rect = cv.minAreaRect(C)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    box = geom.order_box(box)
    return C, box

def handle_pic(path, fout = None, show = False):
    image = cv.imread(path)

    if image is None:
        logging.warning(("File not found", path))
        return None, None
    cropped, w, h = prepare_pic(image)
    if cropped is None:
        return None, None
    cont, box = find_main_countour(cropped)
    if cont is None:
        return None, None

    p1, p2 = geom.calc_box_vector(box)
    if p1 is None:
        return None, None

    angle = geom.get_vert_angle(p1, p2, w, h)
    shift = geom.get_horz_shift(p1[0], w)

    return angle, shift

def main():
    for f in os.listdir("images"):
        a, s = handle_pic("images/" + f, show=True)
        if a is not None and s is not None:
            print('File number: {0}, Angle: {1}, Shift: {2}'.format(os.path.splitext(f)[0], int(a), int(s)))

if __name__ == '__main__':
    main()
