#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting
import pixelGrouping


print("########## Starting coraline.py ##########") 

#open relevant files for training and testing
trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')


"""
#read in one image
img = imageHandler.readImageFromFile(trainingImages)    #returns a 5 image
#imageHandler.convertAsciiImageToFloatArray(img)
imageHandler.printImage(img)

#test pixel grouping
pixler = pixelGrouping.pixelGrouper(2, 2)

pixler.buildPixelSet(img)

pixler.printPixelGroups()
"""

#generate digit cases
digitCases = [ [], [], [], [], [], [], [], [], [] ,[] ]
for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(digitCases, trainingImages, trainingLabels) 
#


gMap = pixelGrouping.groupCaseToMaps(digitCases, 2, 2, 0.6)


print(pixelGrouping.groupAccuracyRating(testImages, testLabels, gMap))




"""
print(gMap[0].pixelGroups[0][0])

#read in one image
#imageHandler.readImageFromFile(testImages)
imageHandler.readImageFromFile(testImages)
img = imageHandler.readImageFromFile(testImages)    #returns a 2 image
imageHandler.printImage(img)
imgGroup = pixelGrouping.pixelGrouper(2, 2)
imgGroup.buildPixelSet(img)

bestGX = 0.0
c = 0
bestC = 0
for m in gMap:
    imgGX = pixelGrouping.pixelGroupAlliance(imgGroup, m) 
    print(imgGX)
    if imgGX > bestGX:
        bestGX = imgGX
        bestC = c
    c += 1

print("\n\n")
print(bestC)
print(bestGX) 
"""


"""
print(len(gMap))
print(len(gMap[0].pixelGroups))
print(gMap[0].pixelGroups[0][0])

for map in gMap:
    map.printPixelGroups()
    print("\n\n\n\n\n\n\n\n\n")
"""


"""
#build maps from the cases 
maps = bayesTraining.caseToMaps(bayesTraining.digitCases)

for i in maps:
    bayesTraining.printMapAsHeatmap(i)
    pixler = pixelGrouping.pixelGrouper(2, 2)
    pixler.buildPixelSet(i)
    pixler.printPixelGroups()
    print()
#
"""





#exit
input("Press [ENTER] to exit program...")