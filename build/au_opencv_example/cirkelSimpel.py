#!/usr/bin/env python
import cv2 
import urllib
import numpy as np
import math

# a = [0.37,1.64]
# print a
# a = np.around(a, decimals = 1)
# print a

def get_from_webcam():
    """
    Fetches an image from the webcam
    """
    print "try fetch from webcam..."
    stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
    bytes=''
    bytes+=stream.read(64500)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')

    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        return i
    else:
        print "did not receive image, try increasing the buffer size in line 13:"


def extract_single_color_range(image,hsv,lower,upper):
    """
    Calculates a mask for which all pixels within the specified range is set to 1
    the ands this mask with the provided image such that color information is
    still present, but only for the specified range
    """
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(image,image, mask= mask)
    return res

def init():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
    cv2.imshow("grey",gray)
     
     
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                  param1=50,
                  param2=25,
                  minRadius=15,
                  maxRadius=22)
    circles = np.uint32(np.around(circles))
    for i in circles[0,:]:
    #draw the outer circle
        cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
        cv2.circle(image,(i[0],i[1]),2,(0,0,255),1)
    
        centerPointX = i[0]
        centerPointY = i[1]
    
    cv2.imshow('detected circles',image)
    
    return centerPointX, centerPointY 

     
def pixel2Metric(delta_r,delta_c):
    focal = 3.15*(math.pow(10, -3))
    Z = 0.932
    Sx = (2.550*(math.pow(10, -3)))/640
    Sy = (1.910*(math.pow(10, -3)))/480
    delta_x = (Z*delta_r*Sx)/focal
    delta_y = (Z*delta_c*Sy)/focal
    
    return delta_x,delta_y

    
    # print circles
  
 




lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])

# image = get_from_webcam()
# cv2.imwrite("center.jpg",image)
image = cv2.imread('center.jpg')

cv2.imshow("raw",image)

refX, refY = init()

# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 
# blue_img = extract_single_color_range(image,hsv,lower_blue,upper_blue)
# 
# cv2.imshow("blue",blue_img)


 


# sx = (math.pow(10, -3)*2.550)/640
# sy = (math.pow(10, -3)*1.910)/480


 
image = get_from_webcam()
cv2.imwrite("blueCircle.jpg",image)

image = cv2.imread('blueCircle.jpg')

x, y = init()

delta_r = refX-x
delta_c = refY-y

print delta_r, " ", delta_c

delta_x, delta_y = pixel2Metric(delta_r, delta_c)

print delta_x, " ", delta_y
cv2.waitKey(0)

