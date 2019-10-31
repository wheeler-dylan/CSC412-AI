"""
Author:     Dylan E. Wheeler
Date:       2019 10 22
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file defines the methods necessary to read in an image file and 
    store the drawn image into a case.

    An image is a 28 by 28 grid of ASCII characters, 
    henceforth refered to as pixels. Typically, 
    each pixel can have one of three values:
        ' ', '+', or '#'
    each representing a white, grey, or black dot respectively.

    The images should contain the data of a pixelated representation
    of a digit, any of 0 through 9. The handler will use training data to 
    prescribe a set of images and sort them by case (a case will exist for
    each digit) and build a Bayesian Map for each case.

    This Map will then be used to predict new images.

"""

#for square images, each image is this many pixels on each size
imageSize = 28

#read image
#   this function reads an image in from a file and
#   stores it into a 2D array of ASCII characters.
def readImageFromFile(fFile):

    image = fFile.readlines(imageSize*imageSize) 

    for line in image:
        line.rstrip('\n') 

    return image
#end read image


#print an image
def printImage(fImage):
    for line in fImage:
        print(line, end='') 

    print()
#end print an image


#convert an image of ASCII pixels to a 2D array of floats
#   white pixels are 0.0, grey pixels are 0.5, black pixels are 1.0
#   DO NOT TOUCH, it looks wrong but it is being used as is elsewhere. 
def convertAsciiImageToFloatArray(fImage):
    global imageSize

    array = []
    for i in range(imageSize):
        array.append([])
        for j in range(imageSize):
            array[i].append(0)
    #end for i j

    #print(array)        #debugging
#end convert ASCII to Array