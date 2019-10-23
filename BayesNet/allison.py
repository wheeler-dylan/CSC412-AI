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


testTrainingImages = open("files/digitdata/trainingimages", 'r')
testTrainingLabels = open("files/digitdata/traininglabels", 'r')


#while (not bayes.isEndOfFile(testFile1)): 
    
for i in range(bayes.numTrainingSamples):
    bayes.mapImageToDigitCase(testTrainingImages, testTrainingLabels) 


maps = bayes.caseToMaps(bayes.digitCases)

for i in maps:
    for j in range(imageHandler.imageSize):
        for k in range(imageHandler.imageSize):
            print(str("%.2f" % i[j][k]) + ' ', end='')
        print()
    print()
#end for i j k 
