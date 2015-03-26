#code for book Machine learning in action

from numpy import *

#create some dateset manually
#each sample is labeled insulted or non-insulted (supervised learning)
def loadDataSet():
    postingList = [['my','dog','has','flea','problems','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]

    #1 indicates insult words, 0 indicates normal words
    classVec = [0, 1, 0, 1, 0, 1]

    return postingList, classVec


#create word set from dataSet
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        #combine two sets
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# return whether each word in the inputSet appears in vocabulary
# 1 indicates appear, 0 indicates not
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" %word
    return returnVec

#improve of setOfWords2Vec
#setOfWords2Vec only count whether a word appears or not
#bagOfWord2VecMN also count for the appear times
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


#calculate probability
#TODO: review again
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)

    #initialize
    #since when want the product p(w0|ci)*p(w1|ci)*...*p(wn|ci), to avoid the case any time of p(wj|ci)==0
    #we have the following initialization
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    #use log to avoid overflow(downside)
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive


#classify
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify*p1Vec) + log(pClass1)
    p0 = sum(vec2Classify*p0Vec) + log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

#testing classifier
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postingDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postingDoc))
    p0V,p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classfied as: ', classifyNB(thisDoc, p0V, p1V, pAb)


if __name__ == '__main__':
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    print myVocabList
    print  setOfWords2Vec(myVocabList,listOPosts[0])
    print  setOfWords2Vec(myVocabList,listOPosts[4])

    #create trainMat
    trainMat = []
    for postingDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postingDoc))

    #calculate probability
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    print 'p0V', p0V
    print 'p1V', p1V
    print 'pAb', pAb

    #tesing precision
    testingNB()









