"""
Author:     Dylan E. Wheeler
Date:       2019 10 23
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file runs the main code for this assignment. 
    It takes in a set of training images and build a 
    set of digit cases for each digit 0 through 9.
    
    These cases are then compiled into bayes maps 
    for each digit.

    The maps are then tested against a new set of test images and
    an accuracy rating and confusion matrix are reported.

"""


import imageHandler
import bayesTraining
import bayesTesting


print("########## Starting main.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')


#generate digit cases
digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(digitCases, trainingImages, trainingLabels) 
#

#build maps from the cases
maps = bayesTraining.caseToMaps(bayesTraining.digitCases, 0.1)


#test the maps accuracy
print(bayesTesting.reportAccuracy(testImages, testLabels, maps))


#build confusion matrix
confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, maps)
bayesTesting.printConfusionMatrix(confusionMatrix, maps)



#exit
input("Press [ENTER] to exit program...")