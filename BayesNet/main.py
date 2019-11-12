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
import pixelGrouping
import oddsRatio


print("########## Starting main.py ##########") 


"""
#####################################################
            SINGLE PIXEL FEATURES
#####################################################
"""
#greet user
print("Hello World. This program will build a Bayesian Probability Network "+
        "that is trained on a set of hand drawn digit images, represented "+
        "here as a 28 by 28 pixel grid of ASCII characters. "+
        "A seperate Bayes model will be built for each digit 0 through 9. "+
        "Then a set of testing data will be compared to the maps and catagorized "+
        "into their estimated digits. Finally a Confusion Matrix will be built "+
        "in order to test the classifier's accuracy.\n\n") 
#input("Press [ENTER] to continue...")

#explain pixel group size and k selection
print("This part of the program will use single pixel features and a "+
      "Laplace smoothing value (k) of 0.1. These values were found to create the "+
      "highest accuracy rating as based off the results from findBestK.py.\n\n")


#open relevant files for training and testing
print("Finding training and testing data...\n\n")
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')


#generate digit cases
digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]
print("Importing data, maping images to digit cases...\n\n") 
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(digitCases, trainingImages, trainingLabels) 
#


#build maps from the cases
print("Building digit models, compiling digit instances into Bayes Maps...\n\n")
maps = bayesTraining.caseToMaps(digitCases, 0.1)
print("Outputing maps/digit probability models...\n") 
thisDigit = 0
for i in maps:
    print("Case/Digit: "+str(thisDigit))
    bayesTraining.printHeatmapKey()
    bayesTraining.printMapAsHeatmap(i)
    print("\nPixel probabilities: (probabilities less than 10% ommitted)")
    bayesTraining.printTrueMap(i, True)
    print()
    thisDigit+=1
#


#build confusion matrix
print("Building confusion matrix, this will show how many images of "+
      "each digit (by row) were classified as each digit (by column).\n")
confusionMatrix = bayesTesting.buildConfusionMatrix(testImages, testLabels, maps)
bayesTesting.printConfusionMatrix(confusionMatrix, maps)
#test the maps accuracy
print("Calculating accuracy rating using single pixel features and k value 0.1...")
print("Accuracy: "+str(bayesTesting.matrixAccuracy(confusionMatrix)*100)+"%\n\n")






"""
#####################################################
            ODDS RATIOS
#####################################################
"""
print("This part of the program will use the most accurate features, "+
      "single pixel features smoothed with k = 0.1, "+
      "and build a set of log odds ratios for the top 4 most "+
      "commonly confused digit pairs.\n\n")

print("Finding most confused number pairs...\n")
mostConfused = oddsRatio.findMostConfusedNumbers(confusionMatrix, 4)
for eachPair in mostConfused:
    print(str(eachPair[0])+" was confused as "+str(eachPair[1])+" "+str(eachPair[2])+" times...")
    bayesTraining.printHeatmapKey()
    bayesTraining.printMapAsHeatmap(maps[eachPair[0]])
    bayesTraining.printHeatmapKey()
    bayesTraining.printMapAsHeatmap(maps[eachPair[1]])
    odds = oddsRatio.buildOddsRatio(maps[eachPair[0]], maps[eachPair[1]])
    oddsRatio.printOddsHeatmapKey()
    oddsRatio.printOddsAsHeatmap(odds)
    print("\n\n")






"""
#####################################################
            PIXEL GROUP FEATURES
#####################################################
"""
print("This next part of the program will build Bayes models based off of "+
      "2 by 2 pixel groups, using a Laplace smoothing value (k) of 0.6. "+
      "While not as accurate as single pixel features, these values were found "+
      "to produce the most accurate results for pixel group based mapping "+
      "according to the results of findBestK.py.\n\n")

#build pixel group based maps
print("Building digit models based off groups...\n\n")
gMaps = pixelGrouping.groupCaseToMaps(digitCases, 2, 2, 0.6)


print("Building confusion matrix for pixel group based maps...\n")
gConfusionMatrix = pixelGrouping.groupConfusionMatrix(testImages, testLabels, gMaps)
bayesTesting.printConfusionMatrix(gConfusionMatrix, gMaps)
print("Calculating accuracy rating using 2 by 2 pixel group features "+
      "and k value 0.6...")
print("Accuracy: "+str(bayesTesting.matrixAccuracy(gConfusionMatrix)*100)+"%\n\n")

pixelGrouping.reportPixelGroupAccuracies()

#exit
input("Press [ENTER] to exit program...")

