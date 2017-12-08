#!/usr/bin/env python
import cv2 
import urllib
import numpy as np
import math


## Ref image processing
refImage = cv2.imread('mmtest1.jpg')
refGrey = cv2.cvtColor(refImage, cv2.COLOR_BGR2GRAY)
cv2.imshow("refGrey",refGrey)

#edges = cv2.Canny(refGrey,200,230)
#cv2.imshow('Canny',edges)

ret,refTh1 = cv2.threshold(refGrey,125,255,cv2.THRESH_BINARY)
cv2.imshow('RefThresholded',refTh1)
refCnt, refHierarchy = cv2.findContours(refTh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for b in refCnt:
	cv2.drawContours(refImage,[b],0,(255,0,0),2)

cv2.imshow('refContours',refImage)

print "RefLength"
print len(refCnt[40])
print "hier"
print len(refHierarchy)

refImageNew = cv2.imread('mmtest1.jpg')

#for index in range((len(refCnt)/2)):
#	cv2.drawContours(refImageNew,[refCnt[index]],0,(255,0,0),2)

#for i,cnt in enumerate(cont):
#	cv2.drawContours(single_channel,cont,i,(255,0,0),2)

cv2.drawContours(refImageNew,refCnt[40],0,(255,0,0),2)

cv2.imshow('refContourNew',refImageNew)
####


image = cv2.imread('oval.jpg')
cv2.imshow("raw",image)
cv2.imwrite("original.jpg",image)

print "idiot"

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("grey",gray)

ret,th1 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

cv2.imshow('thresholded',th1)

contours, hierarchy = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#for b in range(:
#	cv2.drawContours(gray,contours[1],0,(255,0,0),2)

cv2.imshow('contours',gray)
print "lengthcontours"
print len(contours)
#print contours[1]

print 'match'
hej = cv2.matchShapes([contours[4]],contours[2],1,0.0)

#print hej


#ellipse = cv2.fitEllipse(contours[4])
#cv2.ellipse(image,ellipse,(0,255,0),2)

#ellipse = cv2.fitEllipse(contours[2])
#cv2.ellipse(image,ellipse,(0,255,0),2)

cv2.imshow('ellipses',image)

cv2.waitKey(0)

