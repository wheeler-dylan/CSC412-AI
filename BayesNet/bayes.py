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


#determine if at the end of a file
def isEndOfFile(fFile):
    tempFile = copy.deepcopy(fFile)
    line = tempFile.readLine()

    #print(line)

    if line == '':
        return True
    else:
        return False


#map one image to one case
def mapImageToCase(fTrainingImageFile, fTrainingLabelFile):
    global digitCase

    thisImage = imageHandler.readImageFromFile(fTrainingImageFile)
    thisCase = int(fTrainingLabelFile.readline()) 

    #debugging
    imageHandler.printImage(thisImage)
    print(thisCase) 

    digitCase[thisCase].append(thisImage) 


    