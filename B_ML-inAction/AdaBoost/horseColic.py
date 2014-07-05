# Code for book: Machine Learning in action

from numpy import *
import adaboost as ab
import boost

def loadDataSet(fileName):
    #automatic get number of features by examing files
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

def main():
    print '---------------------training--------------------'
    datArr, labelArr = loadDataSet('horseColicTraining2.txt')
    #the last input is the number of classifier
    classifierArray, aggClassEst= ab.adaBoostTrainDS(datArr, labelArr, 50)

    print '---------------------testing---------------------'
    testArr, testLabelArr = loadDataSet('horseColicTest2.txt')
    prediction10 = ab.adaClassify(testArr, classifierArray)

    errArr = mat(ones((67,1)))
    print 'error rate:', errArr[prediction10 != mat(testLabelArr).T].sum()/67




if __name__ == '__main__':
    main()
