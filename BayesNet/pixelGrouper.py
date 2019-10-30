"""
Author:     Dylan E. Wheeler
Date:       2019 10 30
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the functions to train and build a 
    Bayesian Map based off of pixel groups as opposed to 
    individual pixels.

"""




#define pixel grouper class
#   this object will have a set height and width in 
#   terms of the number of pixels, and
#   a set containing the pixel group values
#   drawn from training images
class pixelGrouper:
    def __init__(this, fHeight, fWidth):
        this.height = fHeight
        this.width = fWidth
        this.pixelSet = set()
    #end initializer


    #begin at certain coordinates and add one group of
    #   width and height to the set
    def addPixelGroup(this, fImage, fRowStart, fColStart):
        thisGroupTuple = ()
        for i in range(this.height):
            for j in range(this.width):
                tempTuple = (fImage[fRowStart+i][fColStart+j],)
                print(tempTuple)    #debugging
                thisGroupTuple += tempTuple
        this.pixelSet.add(thisGroupTuple)
        thisGroupTuple = ()
    #end add pixel group


    #take in an image and add all its groups to the set

    #end