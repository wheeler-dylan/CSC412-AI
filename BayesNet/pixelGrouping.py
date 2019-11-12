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
            #print(imgAlliance)
            if imgAlliance > bestAlliance:
                bestAlliance = imgAlliance
                bestGuess = index
            index += 1
        #print("\n\n")

        if bestGuess == labelInt:
            accuracy += 1
        
    #end for i 

    accuracy /= numTests

    return accuracy 
#end group accuracy rating


#build confusion matrix using groups
def groupConfusionMatrix(fTestImages, fTestLabels, fMaps):
    global numTests
    fTestImages.seek(0)
    fTestLabels.seek(0)

    groupHeight = fMaps[0].height
    groupWidth = fMaps[0].width

    #initialize matrix
    matrix = []
    for i in range(len(fMaps)):
        matrix.append([])
        for j in range(len(fMaps)):
            matrix[i].append(0) 
    #end for i j

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
            #print(imgAlliance)
            if imgAlliance > bestAlliance:
                bestAlliance = imgAlliance
                bestGuess = index
            index += 1
        #print("\n\n")

        matrix[labelInt][bestGuess] += 1
    #end for i

    return matrix
#end build matrix


#output pixel grouping results for reporting
#   these numbers are derived from findBestK
def reportPixelGroupAccuracies():
    print("Below are the results of accuracies for various tested pixel groups:")
    print("Height:\tWidth:\tk-value:\tAccuracy:")
    print("2  \t2  \t0.6 \t\t71.2%")
    print("2  \t4  \t0.1 \t\t67.4%")
    print("4  \t2  \t0.0 \t\t66.9%")
    print("4  \t4  \t0.0 \t\t63.5%")
    print("2  \t3  \t0.2 \t\t69.5%")
    print("3  \t2  \t0.2 \t\t69.5%")
    print("3  \t3  \t0.0 \t\t66.7%")
#end 