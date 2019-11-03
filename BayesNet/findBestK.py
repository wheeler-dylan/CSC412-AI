"""
Author:     Dylan E. Wheeler
Date:       2019 11 03
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file is designed to find the k value which 
    returns the highest accuracy rating when used to
    smooth image case maps. 

After running this code, the best k value found was
    0.1 when using single pixel features for mapping. 

"""

import imageHandler
import bayesTraining
import bayesTesting
import copy


print("########## Starting findBestK.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')


#list of cases to find most accurate k
mapsWithDifferentK = []
kStart = 0.0
kEnd = 10.0
kStep = 0.1
bestK = 0.0
bestAccuracy = 0.0
#kIndex = 0

digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(digitCases, trainingImages, trainingLabels) 
#

#for k in toolkit.frange(.1, 10, .1):
k = kStart
while k <= kEnd:
    print("Testing k = " + str(round(k, 1))) 
    
    theseMaps = bayesTraining.caseToMaps(digitCases, k)

    if k == 0.0:
        bestMaps = copy.deepcopy(theseMaps) 

    #for i in theseMaps:
    #    bayesTraining.printMapAsHeatmap(i)
    #    print()
    #
    #bayesTraining.printTrueMap(theseMaps[8], True)

    #mapsWithDifferentK.append(theseMaps)

    #confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, theseMaps)
    #bayesTesting.printConfusionMatrix(confusionMatrix, theseMaps)

    thisAccuracy = bayesTesting.reportAccuracy(testImages, testLabels, theseMaps)
    print("Accuracy of k = " + str(round(k, 1)) + " is:")
    print('%.9f'%thisAccuracy)
    
    if  thisAccuracy > bestAccuracy: 
        print("Better k value found: " + str(round(k, 1))) 
        bestK = k
        bestMaps = copy.deepcopy(theseMaps)
        bestAccuracy = thisAccuracy
    
    k += kStep
    theseMaps = None
    #kIndex += 1
    print("\n\n")

print("Best k value found: " + str(bestK)) 
for i in bestMaps:
    bayesTraining.printMapAsHeatmap(i)
    print()
#

confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, bestMaps)
bayesTesting.printConfusionMatrix(confusionMatrix, bestMaps)


#test the maps accuracy
print(bayesTesting.reportAccuracy(testImages, testLabels, bestMaps))



#exit
input("Press [ENTER] to exit program...")