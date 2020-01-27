import cv2
import numpy as np
import os
import picamera
from time import sleep

# Set whether images should be displayed/saved
show = True
write = False

def main():
    # Images
    #files = [1, 8, 11, 14, 21, 28, 31, 34]
    f = 1
    # Make output image directory
    output_dir = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read image
    #for f in files:
    #camera = picamera.PiCamera()
    #camera.resolution = (640, 480);
    #sleep(2)
    img = '/home/pi/Desktop/NATCAR/opencv_test/inputimg/carpetline.jpg'
    Outputimg = '/home/pi/Desktop/output6.jpg'
    #camera.capture(img)
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    showOriginal(img, f)
    showProcessed(img, f)

def showOriginal(img, f):
    # Show original image
    # cv2.imshow('Original Image', img)

    # Show original image after thresholding
    thresh = 190
    _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original Image Thresholded', img)

    # Save to file
    cv2.imwrite('/home/pi/Desktop/thresh1.jpg', img)

def showProcessed(img, f):
    # Image processing

    # Threshold image first
    thresh = 200
    _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    # nxn mean filter
    n = 9
    mean_filter = np.ones((n, n), np.float32) / (n*n)
    # img = cv2.filter2D(img, -1, mean_filter)

    # nxn median filter
    n = 9
    img = cv2.medianBlur(img, n)

    # nxn bilateral filter
    # n = 5
    # s_sigma = 100 # spatial sigma
    # i_sigma = 100 # intensity sigma
    # img = cv2.bilateralFilter(img, n, s_sigma, i_sigma)

    # nxn Scharr filter
    n = -1
    scharr_x = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=n)))
    scharr_y = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=n)))
    img = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

    # Show processed image
    # cv2.imshow('Processed Image', img)

    # Show processed image after thresholding
    #thresh = 50
    #_, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    # img = cv2.bitwise_not(img)

    # Test morphology

    # Dilation and erosion w/ n iterations
    n = 6
    img = cv2.dilate(img, mean_filter, iterations=n)
    img = cv2.erode(img, mean_filter, iterations=n)

    # Opening
    # img = cv2.morphologyEx(img, cv2.MORPH_OPEN, mean_filter)

    # Closing
    # img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, mean_filter)

    cv2.imshow('Processed Image Thresholded', img)
    cv2.waitKey(0)

    # Save to file
    cv2.imwrite('/home/pi/Desktop/thresh&blur1.jpg', img)

if __name__ == '__main__':
    main()