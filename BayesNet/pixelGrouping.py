"""
Author:     Dylan E. Wheeler
Date:       2019 10 30
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the functions to train and build a 
    Bayesian Map based off of pixel groups as opposed to 
    individual pixels.

"""


import imageHandler
import bayesTraining
import bayesTesting
import math
imageSize = imageHandler.imageSize 
numTrainingSamples = bayesTraining.numTrainingSamples
numTests = bayesTesting.numTests

#define pixel grouper class
#   this object will have a set height and width in 
#   terms of the number of pixels, and
#   a list containing the pixel group values
#   drawn from training images
class pixelGrouper:
    def __init__(this, fHeight, fWidth):
        this.height = fHeight
        this.width = fWidth
        this.pixelGroups = []
    #end initializer


    #begin at certain coordinates and add one group of
    #   width and height to the set
    def addPixelGroup(this, fImage, fRowStart, fColStart):
        thisGroup = []
        for i in range(this.height):
            for j in range(this.width):
                thisGroup += fImage[fRowStart+i][fColStart+j]
        this.pixelGroups.append(thisGroup)
        thisGroup = []
    #end add pixel group


    #take in an image and add all its groups to the set
    def buildPixelSet(this, fImage):
        global imageSize
        for i in range(imageSize-(this.height)):
            for j in range(imageSize-(this.width)):
                this.addPixelGroup(fImage, i, j)
    #end buildPixelSet


    #print this objects pixel groups
    def printPixelGroups(this):
        for i in range(len(this.pixelGroups)):
            print(this.pixelGroups[i], end=' ')
            if (i+1) % (imageSize-(this.width)) == 0:
                print("\n")
    #end printPixelGroups 
#end pixelGrouper class




#functions to train maps based off pixel groups instead of individual pixels

#groupMapBuilder
#   parameters: case list
#   returns: map list
def groupCaseToMaps(fCaseList, fGroupHeight, fGroupWidth, fK):
    global imageSize
    global numTrainingSamples

    numGroups = (imageSize - fGroupHeight)*(imageSize - fGroupWidth) 


    """
    #create list of maps to return
    caseGroups = []
    #count number of images used to produce each map for averaging
    mapImageCount = []


    for i in range(len(fCaseList)):                 #for each case
        caseGroups.append([])                 #produce one map for each case
        counter = 0
        for j in fCaseList[i]:                     #itereate through images in that case
            counter += 1
            tempPixelGrouper = pixelGrouper(fGroupHeight, fGroupWidth)
            tempPixelGrouper.buildPixelSet(j) 
            caseGroups[i].append(tempPixelGrouper)

        mapImageCount.append(counter)
    #end for each case

    #average out the pixels in each case map
    groupsOfMaps = []
    #indexCounter = 0
    for eachCase in caseGroups:  #for each case
        thisMapGrouper = pixelGrouper(fGroupHeight, fGroupWidth)
        for eachGroup in range(numGroups):
            thisMapGrouper.pixelGroups.append([])
            for p in range(fGroupHeight * fGroupWidth):
                thisMapGrouper.pixelGroups[eachGroup].append(0)
            for eachList in eachCase[eachGroup]:
                for eachPixel in range(fGroupHeight * fGroupWidth):
                    if eachCase[eachGroup].pixelGroups[numGroups][eachPixel] == ' ':
                        None
                    elif eachCase[eachGroup].pixelGroups[numGroups][eachPixel] == '+':
                        thisMapGrouper.pixelGroups[numGroups][eachPixel] += 0.5
                    elif eachCase[eachGroup].pixelGroups[numGroups][eachPixel] == '#':
                        thisMapGrouper.pixelGroups[numGroups][eachPixel] += 1.0
    #    indexCounter += 1
    #end for each map

    #print(mapImageCount)           #debugging
    """

    maps = []

    mapsIndex = 0
    for eachCase in fCaseList:

        #build map structure
        maps.append(pixelGrouper(fGroupHeight, fGroupWidth))
        for g in range(numGroups):
            maps[mapsIndex].pixelGroups.append([])
            for p in range(fGroupHeight * fGroupWidth):
                maps[mapsIndex].pixelGroups[g].append(0.0)

        
        #sum the total of pixels from every image and add to map
        imageIndex = 0
        for eachImage in eachCase:
            #imageHandler.printImage(eachImage)
            #print("Image Index: " + str(imageIndex)) 
            thisGroup = pixelGrouper(fGroupHeight, fGroupWidth) 
            thisGroup.buildPixelSet(eachImage)
            for eachGroup in range(numGroups):
                for eachPixel in range(fGroupHeight * fGroupWidth):
                    if thisGroup.pixelGroups[eachGroup][eachPixel] == ' ':
                        None
                    elif thisGroup.pixelGroups[eachGroup][eachPixel] == '+':
                        maps[mapsIndex].pixelGroups[eachGroup][eachPixel] += 0.5
                    elif thisGroup.pixelGroups[eachGroup][eachPixel] == '#':
                        maps[mapsIndex].pixelGroups[eachGroup][eachPixel] += 1.0
                    else:
                        print("ERROR")
                #print(maps[mapsIndex].pixelGroups[eachGroup][eachPixel])
            imageIndex += 1
        
        #averaging and smoothing
        for g in range(numGroups):
            for p in range(fGroupHeight * fGroupWidth):
                maps[mapsIndex].pixelGroups[g][p] += fK
                maps[mapsIndex].pixelGroups[g][p] /= (imageIndex + (fK * (3**(fGroupWidth * fGroupHeight))))

        mapsIndex += 1


    return maps
#end groupCaseToMaps


#report simularity between two pixel groups lists
def pixelGroupAlliance(fTestGroup, fCaseGroup):
    gx = 0.0
    for g in range(len(fTestGroup.pixelGroups)):
        qx = 0
        for p in range(len(fTestGroup.pixelGroups[g])):
            qx += bayesTesting.pixelAlliance(fTestGroup.pixelGroups[g][p], fCaseGroup.pixelGroups[g][p])
        if qx > 0:
            gx += math.log(qx)
    
    gx /= len(fTestGroup.pixelGroups)

    return gx



#find the accuracy rating of group based maps
def groupAccuracyRating(fTestImages, fTestLabels, fMaps):
    global numTests
    fTestImages.seek(0)
    fTestLabels.seek(0)

    groupHeight = fMaps[0].height
    groupWidth = fMaps[0].width

    accuracy = 0.0
    
    for i in range(numTests):
        #grab image and label
        thisImage = imageHandler.readImageFromFile(fTestImages)
        labelText = fTestLabels.readline()
        labelText.rstrip('\n')
        labelInt = int(labelText)

        #build pixel group for image
        thisImageGroup = pixelGrouper(groupHeight, groupWidth)
        thisImageGroup.buildPixelSet(thisImage) 

        #compare image to each case and find best match
        bestAlliance = 0.0
        index = 0
        bestGuess = 0
        for m in fMaps:
            imgAlliance = pixelGroupAlliance(thisImageGroup, m) 
            print(imgAlliance)
            if imgAlliance > bestAlliance:
                bestAlliance = imgAlliance
                bestGuess = index
            index += 1
        print("\n\n")

        if bestGuess == labelInt:
            accuracy += 1
        
    #end for i 

    accuracy /= numTests

    return accuracy 