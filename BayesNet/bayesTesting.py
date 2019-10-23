"""
Author:     Dylan E. Wheeler
Date:       2019 10 23
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the methods necessary to test a number of 
    images against Bayes Maps produced in bayesTraining.py
    Functions here will take in images and compare them to the 
    maps to calculate its most similar map and label it 
    by its best candidate. 

Methods will also be included to test the accuracy of this testing module.
    Additionally, methods will be included to report the confusion matrix
    of a given set of test data. 

"""


import imageHandler
import bayesTraining 

digitCases = bayesTraining.digitCases
imageSize = imageHandler.imageSize
numPixels = (imageSize * imageSize)


#pixel alliance compares a pixel from a test image to a
#   pixel from a case, and returns a
#   percentage of how close the test pixel is to
#   the case pixel
def pixelAlliance(fTestPixel, fCasePixel):
    px = 0
    if fTestPixel == '+':
        px = 0.5
    if fTestPixel == '#':
        px = 1.0
    return 1-abs(fCasePixel-px) 
#end pixel alliance


#test an image by comparing to to each map and finding the most similar map
#   returns the index of the map set of which the image is most similar
#   simularity is scored by the averaged sum of pixel alliances over the number of pixels
def compareImageToMaps(fImage, fMapSet):
    global imageSize
    global numPixels

    #convert the image to an array of float values
    img = imageHandler.convertAsciiImageToFloatArray(fImage)
    
    #simularity score for each map
    candidacyScores = []

    for map in fMapSet:          #for each map
        score = 0.00
        for j in range(imageSize):          #for each pixel
            for k in range(imageSize):
                score += pixelAlliance(fImage[j][k], map[j][k]) 
        score /= numPixels
        candidacyScores.append(score)
    #end for
    return candidacyScores.index(max(candidacyScores))      #debugging
#end compare image to maps