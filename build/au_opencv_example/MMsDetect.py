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
	refGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("refGray",refGray)
	
	edges = cv2.Canny(refGray,100,140)
	cv2.imshow('Canny',edges)

	#ret,refTh1 = cv2.threshold(refGray,150,255,cv2.THRESH_BINARY_INV)
	#cv2.imshow('RefThresholded',refTh1)

	refDilated = cv2.dilate(edges,np.ones((2,2),np.uint8))
	cv2.imshow('RefDilated',refDilated)

	refClosed = cv2.morphologyEx(refDilated, cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
	cv2.imshow('RefCload',refClosed)
	print "sidst"
	return refClosed


def cropPic(image):
    croppedImage = image[100:300, 100:600]
    return croppedImage

def sortContourSize(*contourList):
	MMlist = []
	for i,cnt in enumerate(contourList):
		area = cv2.contourArea(cnt)
		if area > 140 and area < 350:
			MMlist.append(contourList[i])
	return MMlist

def shapeMatchingContour(*contourList):
	result = []
	for i,cnt in enumerate(contourList):
		result.append(cv2.matchShapes(MMcntRef[0],cnt,1,0.0)) 
		result[i] += cv2.matchShapes(MMcntRef[1],cnt,1,0.0)
		result[i] += cv2.matchShapes(MMcntRef[2],cnt,1,0.0)
		result[i] = result[i]/3

	return result
    
def extract_single_color_range(image,hsv,lower,upper):
    """
    Calculates a mask for which all pixels within the specified range is set to 1
    the ands this mask with the provided image such that color information is
    still present, but only for the specified range
    """
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(image,image, mask= mask)
    return res

lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])

		#for j,x in MMcntRef 
			#cv2.matchShapes([MMcntRef[j]],contours[i],1,0.0)	

			
#refImage = get_from_webcam()
refImage = cv2.imread('originalRef.jpg')

#refImage = cropPic(refImage)

#cv2.imwrite('originalRef.jpg',refImage)
cv2.imshow('Reference image',refImage)


refClosed = optimizePic(refImage)


#Konturanalyse af reference billede
refCnt, refHierarchy = cv2.findContours(refClosed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

sortContour = []

sortContour = sortContourSize(*refCnt)


for b in sortContour:
	cv2.drawContours(refImage,[b],0,(255,0,0),2)

cv2.imshow('refContours',refImage)

print len(refCnt)

MMcntRef = []

for i,cnt in enumerate(sortContour):
	area = cv2.contourArea(cnt)
	print area
	#if area > 240 and area < 290:
		#MMcnt.append(refCnt[i])

MMcntRef.append(sortContour[0]) #Area = 284
MMcntRef.append(sortContour[1]) #Area = 218
MMcntRef.append(sortContour[2]) #Area = 243.5


newRefImage = cv2.imread('originalRef.jpg')

for b in MMcntRef:
	cv2.drawContours(newRefImage,[b],0,(255,0,0),2)

cv2.imshow('MMs detected',newRefImage)

#Ref processing is done. 3 MMs ref are stored MMcntRef for comparison later
#  
#Now import a live picture from camera and locate MMs
webcamImage = get_from_webcam()
cv2.imwrite('imageCopy.jpg',webcamImage)
imageCopy = cv2.imread('imageCopy.jpg')
imageCopy = cropPic(imageCopy)
#cv2.imshow('ImageFromCamNew',webcamImage)
  
#imageCopy = cropPic(webcamImage)
  
cv2.imshow('cropped',imageCopy)

#Brug extract single color her!!!
  
imgClosed = optimizePic(imageCopy)
   
cv2.imshow('imgclosed',imgClosed)
   
Cnt, refHierarchy = cv2.findContours(imgClosed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
   
for b in Cnt:
	cv2.drawContours(imageCopy,[b],0,(255,0,0),2)
   
cv2.imshow('allContours',imageCopy)
   
contoursSortedList = []
   
contoursSorted = sortContourSize(*Cnt)
   
print len(contoursSorted)
   
imageCopyNew = cv2.imread('imageCopy.jpg')
imageCopyNew = cropPic(imageCopyNew)
   
for b in contoursSorted:
	cv2.drawContours(imageCopyNew,[b],0,(255,0,0),2)
   
cv2.imshow('Found MMs',imageCopyNew)
   
h = 0
## TEST
imageCopyNew1 = cv2.imread('imageCopy.jpg')
imageCopyNew1 = cropPic(imageCopyNew1)
cv2.drawContours(imageCopyNew1,contoursSorted,h,(255,0,0),2)
   
cv2.drawContours(imageCopyNew1,MMcntRef,0,(255,0,0),2)
   
cv2.imshow('imageCopyNew1',imageCopyNew1)
matchResult = shapeMatchingContour(*contoursSorted)
print "Match result:"
print matchResult[h]


cv2.waitKey(0)






