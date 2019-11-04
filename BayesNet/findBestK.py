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
        accuracy 75.5%

    0.6 when using 2x2 pixel groups for mapping
        accuracy 71.2%

"""

import imageHandler
import bayesTraining
import bayesTesting
import pixelGrouping
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

#find best k for multiple pixel groups:
groupK = kStart
while groupK < kEnd:
    print("Testing k = " + str(round(groupK, 1))) 
    
    theseMaps = pixelGrouping.groupCaseToMaps(digitCases, 2, 2, groupK)

    if groupK == kStart:
        bestMaps = copy.deepcopy(theseMaps) 

    thisAccuracy = pixelGrouping.groupAccuracyRating(testImages, testLabels, theseMaps)

    print("Accuracy of k = " + str(round(groupK, 1)) + " is:")
    print('%.9f'%thisAccuracy)
    
    if  thisAccuracy > bestAccuracy: 
        print("Better k value found: " + str(round(groupK, 1))) 
        bestK = groupK
        bestMaps = copy.deepcopy(theseMaps)
        bestAccuracy = thisAccuracy
    
    groupK += kStep
    theseMaps = None
    #kIndex += 1
    print("\n\n")

print("Best k value found: " + str(bestK)) 
print('%.9f'%bestAccuracy)







#find best k for singe pixel groups:
"""
monoK = kStart
while monoK <= kEnd:
    print("Testing k = " + str(round(monoK, 1))) 
    
    theseMaps = bayesTraining.caseToMaps(digitCases, monoK)

    if monoK == kStart:
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
    print("Accuracy of k = " + str(round(monoK, 1)) + " is:")
    print('%.9f'%thisAccuracy)
    
    if  thisAccuracy > bestAccuracy: 
        print("Better k value found: " + str(round(monoK, 1))) 
        bestK = monoK
        bestMaps = copy.deepcopy(theseMaps)
        bestAccuracy = thisAccuracy
    
    monoK += kStep
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
"""




#exit
input("Press [ENTER] to exit program...")