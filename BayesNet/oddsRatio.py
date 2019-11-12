"""
Author:     Dylan E. Wheeler
Date:       2019 11 11
Course:     CSC 412 - Introduction to AI
Prof.:      Dr. Bo Li

This file contains functions and methods to display 
    the odds ratio of two heatmaps, as well as to
    find the most commonly confused numbers within a 
    confusion matrix.

"""

import bayesTraining
from imageHandler import imageSize 
import math


#build an odds ratio of two numbers
def buildOddsRatio(fMap1, fMap2):
    oddsMap = bayesTraining.buildTempMap()
    for i in range(imageSize):
        for j in range(imageSize):
            #oddsMap[i][j] += fMap1[i][j]
            #oddsMap[i][j] -= fMap2[i][j]
            oddsMap[i][j] = fMap1[i][j] / fMap2[i][j]
            oddsMap[i][j] = math.log(oddsMap[i][j])
    return oddsMap
#end build odds ratio


#find most confused numbers in matrix
#   will compile a list of number pairs fPairs long
def findMostConfusedNumbers(fMatrix, fPairs):
    #find highest misclasified pairs
    wrongNumbers = []
    w = 0
    for i in range(len(fMatrix)):
        for j in range(len(fMatrix[i])): 
            if (i != j):
                if (fMatrix[i][j] != 0):
                    wrongNumbers.append([])
                    wrongNumbers[w].append(fMatrix[i][j]) 
                    wrongNumbers[w].append(i) 
                    wrongNumbers[w].append(j)
                    w+=1

    wrongNumbers.sort(reverse=True)

    #store top 'fPairs' mislasified coordinates
    pairs = []
    w = 0
    for p in range(fPairs):
        pairs.append([])
        pairs[p].append(wrongNumbers[w][1])
        pairs[p].append(wrongNumbers[w][2])
        pairs[p].append(wrongNumbers[w][0])
        w+=1

    return pairs
#end


#print a UNICODE character heatmap of an odds ratio
def printOddsAsHeatmap(fMap):
    for j in range(imageSize):
        for k in range(imageSize):
            if fMap[j][k] < -5:
                print('# ',end='')  #
            elif (fMap[j][k]) < -4:
                print('@ ',end='')  #
            elif (fMap[j][k]) < -2:
                print('% ',end='')  #
            elif (fMap[j][k]) < -.9:
                print('= ',end='')  #
            elif (fMap[j][k]) < -.7:
                print('~ ',end='')  #
            elif (fMap[j][k]) < -.5:
                print('- ',end='')  #
            elif (fMap[j][k]) < -.3:
                print('. ',end='')  #
            elif (fMap[j][k]) < -.1:
                print('_ ',end='')  #
            elif (fMap[j][k]) < .1:
                print('  ',end='')  #
            elif (fMap[j][k]) < .3:
                print('+ ',end='')  #
            elif (fMap[j][k]) < .5:
                print('^ ',end='')  #
            elif (fMap[j][k]) < .7:
                print('° ',end='')  #
            elif (fMap[j][k]) < .9:
                print('¥ ',end='')  #
            elif (fMap[j][k]) < 2:
                print('¶ ',end='')  #
            elif (fMap[j][k]) < 4:
                print('¤ ',end='')  #
            elif (fMap[j][k]) < 5:
                print('ø ',end='')  #
            else:
                print('© ',end='')  #
        print()
#end print heatmap






















"""
#print a UNICODE character heatmap of an odds ratio
def printOddsAsHeatmap(fMap):
    for j in range(imageSize):
        for k in range(imageSize):
            if fMap[j][k] < -5:
                print('@ ',end='')  #
            elif (fMap[j][k]) < -4:
                print('% ',end='')  #
            #elif (fMap[j][k]) < -3:
            #    print('. ',end='')  #
            elif (fMap[j][k]) < -2:
                print('+ ',end='')  #
            #elif (fMap[j][k]) < -1:
            #    print('. ',end='')  #
            elif (fMap[j][k]) < -.9:
                print('= ',end='')  #
            #elif (fMap[j][k]) < -.8:
            #    print('▇ ',end='')  #Lower seven eighths block
            elif (fMap[j][k]) < -.7:
                print('~ ',end='')  #Lower three quarters block
            #elif (fMap[j][k]) < -.6:
            #    print('▅ ',end='')  #Lower five eighths block
            elif (fMap[j][k]) < -.5:
                print('- ',end='')  #Lower half block
            #elif (fMap[j][k]) < -.4:
            #    print('▃ ',end='')   #Lower three eighths block
            elif (fMap[j][k]) < -.3:
                print('. ',end='')  #Lower one quarter block
            #elif (fMap[j][k]) < -.2:
            #    print('▁ ',end='')  #Lower one eighth block
            elif (fMap[j][k]) < -.1:
                print('_ ',end='')  #
            elif (fMap[j][k]) < .1:
                print('  ',end='')  #
            #elif (fMap[j][k]) < .2:
            #    print('+ ',end='')  #
            elif (fMap[j][k]) < .3:
                print('▎ ',end='')  #Left one eighth block
            #elif (fMap[j][k]) < .4:
            #    print('▎ ',end='')  #Left one quarter block
            elif (fMap[j][k]) < .5:
                print('▎ ',end='')  #Left one quarter block
            #elif (fMap[j][k]) < .6:
            #    print('▌ ',end='')  #Left half block
            elif (fMap[j][k]) < .7:
                print('▌ ',end='')  #Left three eighths block
            #elif (fMap[j][k]) < .8:
            #    print('▊ ',end='')  #Left three quarters block
            elif (fMap[j][k]) < .9:
                print('▌ ',end='')  #Left half block
            #elif (fMap[j][k]) < 1:
            #    print('█ ',end='')  #Full block
            elif (fMap[j][k]) < 2:
                print('▊ ',end='')  #Left five eighths block
            #elif (fMap[j][k]) < 3:
            #    print('  ',end='')  #
            elif (fMap[j][k]) < 4:
                print('▊ ',end='')  #Left three quarters block
            elif (fMap[j][k]) < 5:
                print('█ ',end='')  #Left seven eighths block
            else:
                print('█ ',end='')  #Full block
        print()
#end print heatmap
"""
