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
import math

digitCases = bayesTraining.digitCases
imageSize = imageHandler.imageSize
numPixels = (imageSize * imageSize)
numTests = 1000


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
#   simularity is scored by the averaged sum of the log of pixel alliances 
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
                pA = pixelAlliance(fImage[j][k], map[j][k])
                if  pA > 0:
                    score += math.log(pA)
        candidacyScores.append(score)
    #end for
    return candidacyScores.index(max(candidacyScores))     
#end compare image to maps


#find the accuracy rating when testing a set of tests
#   takes in the test image file and test label file
#   takes in the list of bayes maps
#   returns a float value of teh percantage of accuracy
def reportAccuracy(fTestImages, fTestLabels, fMaps):
    global numTests
    fTestImages.seek(0)
    fTestLabels.seek(0)

    accuracy = 0.0
    
    for i in range(numTests):
        thisImage = imageHandler.readImageFromFile(fTestImages)
        labelText = fTestLabels.readline()
        labelText.rstrip('\n')
        labelInt = int(labelText)
        #print(labelInt)
        if (labelInt == compareImageToMaps(thisImage, fMaps)):
            accuracy += 1
    #end for i 

    accuracy /= numTests

    return accuracy 
#end report accuracy 


#build confusion matrix
def buildConfusionMatrix(fTestImages, fTestLabels, fMaps):
    global numTests
    fTestImages.seek(0)
    fTestLabels.seek(0)

    #initialize matrix
    matrix = []
    for i in range(len(fMaps)):
        matrix.append([])
        for j in range(len(fMaps)):
            matrix[i].append(0) 
    #end for i j

    for i in range(numTests):
        thisImage = imageHandler.readImageFromFile(fTestImages)
        labelText = fTestLabels.readline()
        labelText.rstrip('\n')
        labelInt = int(labelText)
        #print(labelInt)
        guess = compareImageToMaps(thisImage, fMaps)
        matrix[labelInt][guess] += 1
    #end for i

    return matrix
#end build matrix


#TODO: convert from counters to percentages
#print confusion matrix
def printConfusionMatrix(fMatrix, fMaps):
    print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
    for i in range(len(fMaps)):
        print(str(i)+'\t', end='')
        for j in range(len(fMaps)):
            print(str(fMatrix[i][j]) + '\t', end='')
        print() 
    #end for
#end print matrix