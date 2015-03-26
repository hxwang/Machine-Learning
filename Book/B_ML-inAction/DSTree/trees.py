#code for book Machine learning in action

from math import log
import operator
import matplotlib.pyplot as plt
import treePlotter as tp


#calculate Shannon Ent(i.e., information gain)
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

#create dataset
def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

#get sub-dataset
#get the samples whose value at index axis == value
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#find best split
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    #enumerate to find the best feature (i.e., the one with the maximum information gain))
    for i in range(numFeatures):
        #get all possible value for this feature
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# find the classify type with maximum count
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

# create tree
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    #same class
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #TODO: explain
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


#use decision tree for classifying
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featLabels,testVec)
            else: classLabel = secondDict[key]
    return classLabel


#store tree to disk
def storeTree(inputTree, filename):
    #for serialization
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

#grab tree from disk
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)






if __name__ == '__main__':
    #create dataset
    print '-------------- create dataset --------------------'
    myDat, labels = createDataSet()
    print myDat, labels
    #calculate shannonEnt
    print '-------------- calculate shannonEnt --------------------'
    shannonEnt = calcShannonEnt(myDat)
    print shannonEnt
    #split dataset
    print '-------------- split dataset --------------------'
    print splitDataSet(myDat,0,1)
    print splitDataSet(myDat,0,0)
    #get best feature
    print '-------------- best feature --------------------'
    print 'best feature:' ,chooseBestFeatureToSplit(myDat)
    print 'createTree ', createTree(myDat,labels)

    #plot trees
    print '-------------- plot-trees --------------------'
    myTree =  tp.retrieveTree(0)
    print 'myTree ', myTree
    print 'labels', labels
    print 'numLeafs ', tp.getNumLeafs(myTree)
    print 'treeDepth ', tp.getTreeDepth(myTree)
    #tp.createPlot(myTree)

    #update dict and plot again
    #myTree['no surfacing'][3] = 'maybe'
    #tp.createPlot(myTree)

    #classify
    print '-------------- classify --------------------'
    myDat, labels = createDataSet()
    print 'labels', labels
    myTree =  tp.retrieveTree(0)
    print 'myTree ', myTree
    print '[1,0]: ', classify(myTree, labels, [1,0])
    print '[1,1]: ', classify(myTree, labels, [1,1])

    #store and grab tree
    print '-------------- store and grab tree --------------------'
    storeTree(myTree,'classifierStorate.txt')
    newTree = grabTree('classifierStorate.txt')
    print 'grabedTree: ', newTree


    #Example1: choose suitable lens type
    print '-------------- Eg1: choose suitable lens type --------------------'
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astog,atoc', 'tearRate']
    lensesTree = createTree(lenses,lensesLabels)
    print lensesTree
    tp.createPlot(lensesTree)



