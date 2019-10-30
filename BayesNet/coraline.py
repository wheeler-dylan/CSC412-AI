#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting
import pixelGrouping


print("########## Starting coraline.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')

#read in one image
img = imageHandler.readImageFromFile(trainingImages)    #returns a 5 image
imageHandler.convertAsciiImageToFloatArray(img)
imageHandler.printImage(img)

#test pixel grouping
pixler = pixelGrouping.pixelGrouper(2, 2)

pixler.buildPixelSet(img)

pixler.printPixelGroups()

#start at 8, 10 to get something in the middle
#pixler.addPixelGroup(img, 8, 8)

"""

#generate digit cases
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(trainingImages, trainingLabels) 
#

#build maps from the cases
maps = bayesTraining.caseToMaps(bayesTraining.digitCases)

for i in maps:
    bayesTraining.printMapAsHeatmap(i)
    pixler = pixelGrouping.pixelGrouper(2, 2)
    pixler.buildPixelSet(i)
    pixler.printPixelGroups()
    print()
#
"""