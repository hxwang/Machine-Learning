#code for book Machine learning in action

from numpy import *
import operator
import boost

def loadSimpData():
    datMat = matrix([[ 1. ,  2.1],
        [ 2. ,  1.1],
        [ 1.3,  1. ],
        [ 1. ,  1. ],
        [ 2. ,  1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels



def adaBoostTrainDS(dataArr, classLabels, numIt = 40):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m,1))/m)
    aggClassEst = mat(zeros((m,1)))
    for i in range(numIt):
        bestStump, error, classEst = boost.buildStump(dataArr, classLabels, D)
        print "D:", D.T
        alpha = float(0.5*log((1.0-error)/max(error,1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print "classEst:", classEst.T
        #compute D for next teration
        #D is the weight of all samples
        expon = multiply(-1*alpha*mat(classLabels).T,classEst)
        D = multiply(D,exp(expon))
        D = D/D.sum()

        #calculate error
        aggClassEst += alpha*classEst
        print "aggClassEst: ", aggClassEst.T
        aggErros = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m,1)))
        errorRate = aggErros.sum()/m
        print "total error: ", errorRate, "\n"
        if errorRate == 0.0:
            break
    return weakClassArr, aggClassEst


def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m,1)))
    #iterate all classifier, and estimate a value of each classifier using stumpClassify()
    for i in range(len(classifierArr)):
        classEst = boost.stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'],
                                       classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha']*classEst
    return sign(aggClassEst)







def main():
    datMat, classLabels = loadSimpData()

    #build stump
    #D = mat(ones((5,1))/5)
    #bestStump, minError, bestClasEst = boost.buildStump(datMat, classLabels, D)
    #print "bestStump", bestStump
    #print "minError", minError
    #print "bestClasEst", bestClasEst

    classifierArray, aggClassEst = adaBoostTrainDS(datMat, classLabels, 30)
    print "classifierArray", classifierArray
    #print "sign ", adaClassify([0,0], classifierArray)

    print "sign ", adaClassify([[5,5],[0,0]], classifierArray)



if __name__ == '__main__':
    main()