#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting


print("########## Starting bernard.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')


#generate digit cases
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(trainingImages, trainingLabels) 
#

#build maps from the cases
maps = bayesTraining.caseToMaps(bayesTraining.digitCases)


#test the maps accuracy
#print(bayesTesting.reportAccuracy(testImages, testLabels, maps))

for i in maps:
    bayesTraining.printMapAsHeatmap(i)
    print()
#

confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, maps)
bayesTesting.printConfusionMatrix(confusionMatrix, maps)
