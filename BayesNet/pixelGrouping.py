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
imageSize = imageHandler.imageSize 

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
#   parameters: case list, map list
def