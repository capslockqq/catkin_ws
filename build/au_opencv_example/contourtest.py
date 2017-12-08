#!/usr/bin/env python
import cv2 
import urllib
import numpy as np
import math
	

## Ref image processing
refImage = cv2.imread('oval.jpg')
refGrey = cv2.cvtColor(refImage, cv2.COLOR_BGR2GRAY)
cv2.imshow("refGrey",refGrey)

#edges = cv2.Canny(refGrey,200,230)
#cv2.imshow('Canny',edges)

ret,refTh1 = cv2.threshold(refGrey,30,255,cv2.THRESH_BINARY)
cv2.imshow('RefThresholded',refTh1)
refCnt, refHierarchy = cv2.findContours(refTh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for b in refCnt:
	cv2.drawContours(refImage,[b],0,(255,0,0),2)

cv2.imshow('refContours',refImage)

cntList = []

for i,cnt in enumerate(refCnt):
	area = cv2.contourArea(cnt)
	print area
	print len(refCnt[i])
	if area > 100 and area < 10000:
		cntList.append(refCnt[i])   

print "size new list"
print len(cntList) 
print len(cntList[0])    


refImageNew = cv2.imread('oval.jpg')

#for index in range((len(refCnt)/2)):
#	cv2.drawContours(refImageNew,[refCnt[index]],0,(255,0,0),2)

#for i,cnt in enumerate(cont):
#	cv2.drawContours(single_channel,cont,i,(255,0,0),2)

cv2.drawContours(refImageNew,refCnt,2,(255,0,0),2)

cv2.imshow('refContourNew',refImageNew)
####

cv2.waitKey(0)


