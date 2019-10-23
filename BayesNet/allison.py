#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting


print("########## Starting allison.py ##########") 

trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')



for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(trainingImages, trainingLabels) 
#

maps = bayesTraining.caseToMaps(bayesTraining.digitCases)

"""
for i in maps:
    bayesTraining.printTrueMap(i, True)
    bayesTraining.printMapAsHeatmap(i)
#
"""

for i in range(1):
    thisImage = imageHandler.readImageFromFile(testImages)
    bayesTesting.compareImageToMaps(thisImage, maps)
#
