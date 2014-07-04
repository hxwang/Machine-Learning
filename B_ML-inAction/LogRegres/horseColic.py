#code for book Machine learning in action

import logRegres as lr
from numpy import  *

#classify: given weights, classify the type of input using sigmoid function
def classifyVector(inX, weights):
    prob = lr.sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1
    else:
        return 0

def colicTest():
    #create training data
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currentLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currentLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currentLine[21]))

    #training
    trainWeights = lr.stocGradAscent1(array(trainingSet), trainingLabels, 500)

    #test
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = float(errorCount)/numTestVec
    print "the error rate of this set is: %f " %errorRate
    return errorRate

#conduct multiple test to calculate error rates
def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" %(numTests, errorSum/float(numTests))


if __name__ == '__main__':
    multiTest()


