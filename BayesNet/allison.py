#THIS IS A TEST FILE, DO NOT INCLUDE IN FINAL IMPLEMENTATION

#SANDBOX

import imageHandler
import bayesTraining
import bayesTesting


print("########## Starting allison.py ##########") 

trainingImages = open("files/digitdata/trainingimages", 'r')
trainingLabels = open("files/digitdata/traininglabels", 'r')
testImages = open("files/digitdata/testimages", 'r')
testLabels = open("files/digitdata/testlabels", 'r')



for i in range(bayesTraining.numTrainingSamples):
    bayesTraining.mapImageToDigitCase(trainingImages, trainingLabels) 
#
maps = bayesTraining.caseToMaps(bayesTraining.digitCases)


"""k smoothing had only negative affect on accuracy when using single pixel units
    Update: no longer true, k smoothing was broken, fixed now, see findBestK.py
    best k value is 0.1
""" 
#k = bayesTraining.findBestK(maps, testImages, testLabels)
#print("Allison says: best k value found: " + str(k)) 
#if k > 0:
#    bayesTraining.smoothMap(i, k)




for i in maps:
    #bayesTraining.printTrueMap(i, True)
    #bayesTraining.printMapAsHeatmap(i)
    #bayesTraining.smoothMap(i, .3)
    #bayesTraining.printTrueMap(i, True)
    bayesTraining.printMapAsHeatmap(i)
    print()
#



print(bayesTesting.reportAccuracy(testImages, testLabels, maps))
