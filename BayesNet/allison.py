#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayes

print("########## Starting allison.py ##########") 

fileName = "files/digitdata/trainingimages"

file = open(fileName, 'r')


#for i in range(5):
#    image1 = imageHandler.readImageFromFile(file)
#    imageHandler.printImage(image1) 


testFile1 = open("files/testEOF", 'r')

while (not bayes.isEndOfFile(testFile1)): 
    print(testFile1.readline()) 
    #print("Debugging") 

