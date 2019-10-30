"""
Author:     Dylan E. Wheeler
Date:       2019 10 22
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the methods necessary to build a 
    Bayesian Map of an image case. A Baysenian Map is a smoothed average
    of a number of images from a given set of training data. 

The map is built by pulling an image from the training file and 
    assigning it to a case. The sum of the training images is stored and 
    then averaged, and then smoothed.

This map is then used to predict the case of new images where 
    the case is not known. 

"""

import imageHandler
import copy 
import toolkit

#dimension of each side of a square image
imageSize = imageHandler.imageSize  

#list of all cases for digits 0 through 9
digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]

#number of samples to be processed from training data
numTrainingSamples = 5000

import bayesTesting


##determine if at the end of a file
#def isEndOfFile(fFile):
#    tempFile = copy.deepcopy(fFile)
#    line = tempFile.readLine()

#    #print(line)

#    if line == '':
#        return True
#    else:
#        return False
##end is end of file


#map one image to one case
def mapImageToDigitCase(fCases, fTrainingImageFile, fTrainingLabelFile):
    thisImage = imageHandler.readImageFromFile(fTrainingImageFile)
    thisCase = int(fTrainingLabelFile.readline()) 

    fCases[thisCase].append(thisImage) 

#end map image to case


#build square a 2D array of 0's of the dimensions of imageSize
def buildTempMap():
    global imageSize
    map = []
    for i in range(int(imageSize)):
        map.append([])
        for j in range(int(imageSize)):
            map[i].append(0) 
    #end for
    return map
#end build temp map


#transform each case to Bayes Map
def caseToMaps(fCaseList):
    global imageSize
    global numTrainingSamples

    #store one map for each case
    maps = []
    #count number of images used to produce each map for averaging
    mapImageCount = []

    for i in fCaseList:                  #for each case
        tempMap = buildTempMap()                #produce one map for each case
        counter = 0
        for j in i:                             #itereate through images in that case
            counter += 1
            for k in range(int(imageSize)):     #loop through 2D array of the image
                for l in range(int(imageSize)):
                    if j[k][l] == ' ':          #white pixel
                        None    #do nothing
                    elif j[k][l] == '+':        #grey pixel
                        tempMap[k][l] += 0.5
                    elif j[k][l] == '#':        #black pixel
                        tempMap[k][l] += 1.0
        maps.append(tempMap)
        mapImageCount.append(counter)
    #end for each case

    #average out the pixels in each case map
    indexCounter = 0
    for m in maps:                              #for each case
        for n in range(int(imageSize)):         #loop through 2D array of pixels
            for o in range(int(imageSize)):
                m[n][o] /= (mapImageCount[indexCounter])
        indexCounter += 1
    #end for each map

    #print(mapImageCount)           #debugging

    return maps
#end caseToMaps


#apply smoothing to a map, the k value is passed as a parameter 
#   as is the map to be smoothed.
def smoothMap(fMap, k):
    global imageSize
    for i in range(imageSize):
        for j in range(imageSize):
            fMap[i][j] = (fMap[i][j] + k)/(1+(k*3))
#end smooth map


#find best k
#   finds the best k value to pass into smoothMap
#   iterates through several k values and keeps track of which is the most accurate.
def findBestK(fOriginalMaps, fTestImages, fTestLabels): 

    kStart = 0.1
    kEnd = 10.0
    kStep = 0.1
    
    bestMap = copy.deepcopy(fOriginalMaps)
    bestK = 0.0
    #bestAccuracy = 0.0
    bestAccuracy = bayesTesting.reportAccuracy(fTestImages, fTestLabels, fOriginalMaps)
    print("Original Accuracy before smoothing: " + str(bestAccuracy)) 

    #for k in toolkit.frange(.1, 10, .1):
    k = kStart
    while k <= kEnd:
        thisMap = copy.deepcopy(fOriginalMaps)

        print("Testing k = " + str(round(k, 1))) 
        for m in thisMap:
            smoothMap(m, k)

        thisAccuracy = bayesTesting.reportAccuracy(fTestImages, fTestLabels, thisMap)
        print("Accuracy of k = " + str(round(k, 1)) + " is " + str(thisAccuracy))
        
        if  thisAccuracy > bestAccuracy: 
            print("Better k value found: " + str(round(k, 1))) 
            bestK = k
            bestMap = copy.deepcopy(thisMap)
            bestAccuracy = thisAccuracy
        k += kStep
    #end k loop

    return bestK
#end find best k


#print a ASCII character heatmap of a map
def printMapAsHeatmap(fMap):
    for j in range(imageHandler.imageSize):
        for k in range(imageHandler.imageSize):
            if fMap[j][k] < .1:
                print('  ',end='')
            elif fMap[j][k] < .2:
                print('_ ',end='')
            elif fMap[j][k] < .3:
                print('. ',end='')
            elif fMap[j][k] < .4:
                print('- ',end='')
            elif fMap[j][k] < .5:
                print('~ ',end='')
            elif fMap[j][k] < .6:
                print('= ',end='')
            elif fMap[j][k] < .7:
                print('+ ',end='')
            elif fMap[j][k] < .8:
                print('% ',end='')
            elif fMap[j][k] < .9:
                print('@ ',end='')
            else:
                print('# ',end='')
        print()
#end print heatmap


#print a 'true' map as a percentage of each pixel
def printTrueMap(fMap, fOmitLow):
    for j in range(imageHandler.imageSize):
        for k in range(imageHandler.imageSize):
            if fOmitLow and fMap[j][k] < 0.05:
                print('     ',end='')
            else:
                print(str("%.2f" % fMap[j][k]) + ' ', end='')
        print()
    print()
#end print truemap




#print a map as a integer value of each pixel
def printIntMap(fMap):
    for j in range(imageHandler.imageSize):
        for k in range(imageHandler.imageSize):
            print(str(math.floor(fMap[j][k]*10)) + ' ', end='')
        print()
    print()
#end print truemap