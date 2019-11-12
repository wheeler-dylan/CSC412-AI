#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting
import oddsRatio


print("########## Starting bernard.py ##########") 

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
maps = bayesTraining.caseToMaps(digitCases, 0.1)

for i in maps:
    bayesTraining.printMapAsHeatmap(i)
    print()
#


confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, maps)
bayesTesting.printConfusionMatrix(confusionMatrix, maps)


#test the maps accuracy
print("Accuracy: "+str(bayesTesting.matrixAccuracy(confusionMatrix)*100)+"%")


mostConfused = oddsRatio.findMostConfusedNumbers(confusionMatrix, 4)
for eachPair in mostConfused:
    print(str(eachPair[0])+" was confused as "+str(eachPair[1])+" "+str(eachPair[2])+" times...")
    bayesTraining.printMapAsHeatmap(maps[eachPair[0]])
    print("\n")
    bayesTraining.printMapAsHeatmap(maps[eachPair[1]])
    print("\n")
    odds = oddsRatio.buildOddsRatio(maps[eachPair[0]], maps[eachPair[1]])
    oddsRatio.printOddsAsHeatmap(odds)
    print("\n")
    print("\n\n")


"""
bayesTraining.printMapAsHeatmap(maps[4])
print("\n\n")
bayesTraining.printMapAsHeatmap(maps[9])
print("\n\n")
odds = oddsRatio.buildOddsRatio(maps[4], maps[9])
#bayesTraining.printTrueMap(odds, False)
#print("\n\n")
oddsRatio.printOddsAsHeatmap(odds)
print("\n\n")
print("\n\n")

bayesTraining.printMapAsHeatmap(maps[7])
print("\n\n")
bayesTraining.printMapAsHeatmap(maps[9])
print("\n\n")
odds = oddsRatio.buildOddsRatio(maps[7], maps[9])
#bayesTraining.printTrueMap(odds, False)
#print("\n\n")
oddsRatio.printOddsAsHeatmap(odds)
print("\n\n")
print("\n\n")

bayesTraining.printMapAsHeatmap(maps[8])
print("\n\n")
bayesTraining.printMapAsHeatmap(maps[9])
print("\n\n")
odds = oddsRatio.buildOddsRatio(maps[8], maps[9])
#bayesTraining.printTrueMap(odds, False)
#print("\n\n")
oddsRatio.printOddsAsHeatmap(odds)
print("\n\n")
print("\n\n")
"""


#exit
input("Press [ENTER] to exit program...")