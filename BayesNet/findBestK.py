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

    0.2 when using 2x3 pixel groups for mapping
        accuracy 69.5%

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

#open file to output results of k seraching
kSearchResults = open("kSearchResults.txt", "a")

digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(digitCases, trainingImages, trainingLabels) 
#


#list of cases to find most accurate k
#mapsWithDifferentK = []
bestK = 0.0
bestAccuracy = 0.0

#find best k for pixel groups 2x2 through 4x4:
bestGroupHeight = 2
bestGroupWidth = 2
while groupHeight <= 4:
    while groupWidth <= 4:

        kStart = 0.0
        kEnd = 10.0
        kStep = 0.1
        groupK = kStart

        while groupK < kEnd:
            print("Testing k = " + str(round(groupK, 1))) 
            print("Group Height = " + str(groupHeight)) 
            print("Group Width = " + str(groupWidth)) 
            kSearchResults.write("Testing k = " + str(round(groupK, 1)) + "\n") 
            kSearchResults.write("Group Height = " + str(groupHeight) + "\n") 
            kSearchResults.write("Group Width = " + str(groupWidth) + "\n") 
            
            theseMaps = pixelGrouping.groupCaseToMaps(digitCases, groupHeight, groupWidth, groupK)

            if groupK == kStart:
                bestMaps = copy.deepcopy(theseMaps) 

            thisAccuracy = pixelGrouping.groupAccuracyRating(testImages, testLabels, theseMaps)

            print("Accuracy of k = " + str(round(groupK, 1)) + " is:")
            print('%.9f'%thisAccuracy)
            kSearchResults.write("Accuracy of k = " + str(round(groupK, 1)) + " is:" + "\n")
            kSearchResults.write(str(round(thisAccuracy,9)) + "\n")
            
            if  thisAccuracy > bestAccuracy: 
                print("Better k value found: " + str(round(groupK, 1))) 
                kSearchResults.write("Better k value found: " + str(round(groupK, 1)) + "\n") 
                bestK = groupK
                bestMaps = copy.deepcopy(theseMaps)
                bestAccuracy = thisAccuracy
                bestGroupHeight = groupHeight
                bestGroupWidth = groupWidth
    
            groupK += kStep
            theseMaps = None
            #kIndex += 1
            print("\n\n")
            kSearchResults.write("\n\n")
        # end while k < kEnd

        groupWidth += 1
    #end while width < 4
    groupHeight += 1
#end for height

print("Best k value found: " + str(bestK)) 
print('%.9f'%bestAccuracy)
print("Best group height found: " + str(bestGroupHeight)) 
print("Best group width found: " + str(bestGroupWidth)) 
kSearchResults.write("Best k value found: " + str(bestK) + "\n") 
kSearchResults.write(str(round(thisAccuracy,9)) + "\n")
kSearchResults.write("Best group height found: " + str(bestGroupHeight) + "\n") 
kSearchResults.write("Best group width found: " + str(bestGroupWidth) + "\n") 





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