#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting
import pixelGrouper


print("########## Starting coraline.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')

#read in one image
img = imageHandler.readImageFromFile(trainingImages)    #returns a 5 image
imageHandler.printImage(img)

#test pixel grouping
pixler = pixelGrouper.pixelGrouper(2, 2)

pixler.buildPixelSet(img)

pixler.printPixelGroups()

#start at 8, 10 to get something in the middle
#pixler.addPixelGroup(img, 8, 8)