#!/usr/bin/env python
import cv2 
import urllib
import numpy as np
import math

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

def optimizePic(image):
	refGray = cv2.cvtColor(refImage, cv2.COLOR_BGR2GRAY)
	cv2.imshow("refGray",refGray)

	ret,refTh1 = cv2.threshold(refGray,150,255,cv2.THRESH_BINARY_INV)
	cv2.imshow('RefThresholded',refTh1)

	refDilated = cv2.dilate(refTh1,np.ones((3,3),np.uint8))
	cv2.imshow('RefDilated',refDilated)

	refClosed = cv2.morphologyEx(refDilated, cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
	cv2.imshow('RefCload',refClosed)
	return refClosed


refImage = get_from_webcam()
#refImage = cv2.imread('originalRef.jpg')
cv2.imshow('FromWebcam',refImage)

cv2.waitKey(0)
