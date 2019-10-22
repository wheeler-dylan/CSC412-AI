#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayes

print("########## Starting allison.py ##########") 

fileName = "files/digitdata/trainingimages"

file = open(fileName, 'r')


#for i in range(5):
#    image1 = imageHandler.readImageFromFile(file)
#    imageHandler.printImage(image1) 


testTrainingImages = open("files/digitdata/tinyTrainingImages", 'r')
testTrainingLabels = open("files/digitdata/tinyTrainingLabels", 'r')


#while (not bayes.isEndOfFile(testFile1)): 
    

bayes.mapImageToCase(testTrainingImages, testTrainingLabels) 
bayes.mapImageToCase(testTrainingImages, testTrainingLabels) 
bayes.mapImageToCase(testTrainingImages, testTrainingLabels) 
bayes.mapImageToCase(testTrainingImages, testTrainingLabels) 

