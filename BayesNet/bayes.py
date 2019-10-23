"""
Author:     Dylan E. Wheeler
Date:       2019 10 22
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the methods necessary to build a 
    Bayesian Map of an image case. A Baysenian Map is a smoothed average
    of a number of images from a given set of training data. 

The map is built by pulling an image from the training file and 
    assigning it to a case. The sum of the training images is stored and 
    then averaged, and then smoothed.

This map is then used to predict the case of new images where 
    the case is not known. 

"""

import imageHandler
import copy

#dimension of each side of a square image
imageSize = imageHandler.imageSize  

#list of all cases for digits 0 through 9
digitCase = [ [], [], [], [], [], [], [], [], [] ,[] ]

#number of samples to be processed from training data
numTrainingSamples = 50

#determine if at the end of a file
def isEndOfFile(fFile):
    tempFile = copy.deepcopy(fFile)
    line = tempFile.readLine()

    #print(line)

    if line == '':
        return True
    else:
        return False
#end is end of file


#map one image to one case
def mapImageToDigitCase(fTrainingImageFile, fTrainingLabelFile):
    global digitCase

    thisImage = imageHandler.readImageFromFile(fTrainingImageFile)
    thisCase = int(fTrainingLabelFile.readline()) 

    #debugging
    imageHandler.printImage(thisImage)
    print(thisCase) 

    digitCase[thisCase].append(thisImage) 
#end map image to case


#transform each case to Bayes Map
def caseToMaps(fCaseList):
    global imageSize
    global numTrainingSamples

    maps = []

    for i in fCaseList:                         #for each case
        tempMap = buildTempMap()                #produce one map for each case
        for j in i:                             #itereate through images in that case
            for k in range(int(imageSize)):     #loop through 2D array of the image
                for l in range(int(imageSize)):
                    if j[k][l] == ' ':          #white pixel
                        None    #do nothing
                    elif j[k][l] == '+':        #grey pixel
                        tempMap[k][l] += 0.5
                    elif j[k][l] == '#':        #black pixel
                        tempMap[k][l] += 1.0
        maps.append(tempMap)
    #end for each case

    #average out the pixels in each case map
    for m in maps:                              #for each case
        for n in range(int(imageSize)):         #loop through 2D array of pixels
            for o in range(int(imageSize)):
                m[n][o] /= numTrainingSamples
    #end for each map

    return maps
#end caseToMaps