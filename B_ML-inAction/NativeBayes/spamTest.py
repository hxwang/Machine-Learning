
import bayes
from numpy import *

#convert email to a set of words
def textParse(bigString):
    import  re
    #note need to be capitle W, W means any non-word chars
    listOfTokens = re.split(r'\W*', bigString)
    #tok.lower(): convert all text to lowe case
    #len(tok)>2: filter out '', 'py', 'en' since when split URL such text could be created
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

#test spam
def spamTest():
    docList = []
    classList = []
    fullText = []

    # parse text from email
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' %i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        #parse text
        wordList = textParse(open('email/ham/%d.txt' %i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = bayes.createVocabList(docList)

    #build training set and test set
    trainingSet = range(50);
    testSet =[]
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        #select testset and remove the testset from all dataset
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bayes.setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = bayes.trainNB0(array(trainMat), array(trainClasses))

    #classify and test precision
    errorCount = 0
    for docIndex in testSet:
        wordVector = bayes.setOfWords2Vec(vocabList, docList[docIndex])
        if bayes.classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount)/len(testSet)


if __name__=='__main__':
    spamTest()
