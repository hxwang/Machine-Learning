# Code for book: Machine Learning in action
# Chap02: K nearest neighbours(KNN)

from  numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

#TODO: convert classifier type from string to int

#create dataset
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

#KNN
def classify0(inX, dataSet, labels, k):
    #calculate distances
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    #select k nearest neighbours
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel,0) + 1

    #select types among knn with highest frequency
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

#data process
#input file has 1000 samples, each line contains one sample which has 3 features
def file2matrix(filename):

    #get lines in files
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)

    #build return NumPy matrix
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0

    #process each sample
    for line in arrayOLines:
        #remove  'enter' from each line
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        #get last element in each line
        #TODO: convert classify label from string to int
        classLabelVector.append((listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

#plot figure
def plotFigure(datingDataMat,datingLabels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #TODO: plot figure with colors
    #ax.scatter(datingDataMat[:,1], datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    plt.show()

#normalize data
def autoNorm(dataSet):
    #min value of each column
    minVals = dataSet.min(0);
    maxVals = dataSet.max(0);
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges,minVals

#test precision of classifier
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        #print "the classifier came back with: %s, the real answer is %s" %(classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]) : errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))

#UI: classify person
def classifyPerson():
    #resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input('percentage of time spent in playing video games?'))
    ffMiles = float(raw_input('frequent flier miles earned per year'))
    iceCreame = float(raw_input('liters of ice cream consumed per year?'))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCreame])
    classsifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    #TODO: print the verbal classify result
    print "You will probably like this person:", classsifierResult

#convert 32*32 bit images to 1*1024 vector
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect


#handwriting classifier
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' %fileNameStr)

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' %fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        #print "the classfier came back with %d, the real answer is : %d" %(classifierResult, classNumStr)
        if(classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of error is: %d" %errorCount
    print "\nthe total error rate is: %f" %(errorCount/float(mTest))

if __name__ == '__main__':

    #Example 1: given an instance([0,0]), classify its type(A or B)
    #
    #create dataset
    group, labels = createDataSet()
    #KNN classify
    result = classify0([0,0],group,labels,3)
    print 'Classify Type:' + result

    #Example 2: given an instance(a man with several features)
    #           classify its type('not at all', 'in small doses', 'in large doses')
    # 1.create dataset
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    # 2.plot figure
    #plotFigure(datingDataMat,datingLabels)
    # 3.normalize data
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 4.test classifier precision
    datingClassTest()
    # 5.UI: classify person
    #classifyPerson()

    #Example3: classify digits
    #convert image informatin to vector
    testVector = img2vector('testDigits/0_13.txt')
    #classify and test precision of classifer
    handwritingClassTest()
