#code for book Machine learning in action

from numpy import *
from os import listdir

import kernel as kn


#convert 32*32 bit images to 1*1024 vector
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

#only 0 and 9 digits are included in the file
def loadImages(dirName):
    hwLabels = []
    trainingFileList = listdir(dirName)
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        if classNumStr == 9:
            hwLabels.append(-1)
        else:
            hwLabels.append(1)
        trainingMat[i,:] = img2vector('%s/%s' %(dirName, fileNameStr))
    return trainingMat, hwLabels

def testDigits(kTup=('rbf',10)):
    dataArr, labelArr = loadImages('digits/trainingDigits')
    b, alphas = kn.smoP(dataArr, labelArr, 200, 0.0001, 10000, kTup)
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()

    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print "there are %d Support Vectors" %shape(sVs)[0]

    #error rate of training data
    m,n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kn.kernelTrans(sVs, datMat[i,:],kTup)
        predict = kernelEval.T*multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print "the training error rate is: %f" %(float(errorCount)/m)

    #error rate of test data
    dataArr, labelArr = loadImages('digits/testDigits')
    errorCount = 0
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    m,n = shape(datMat)
    for i in range(m):
        kernelEval = kn.kernelTrans(sVs, datMat[i,:], kTup)
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print "the test error rate is: %f" %(float(errorCount)/m)


if __name__ == '__main__':
    #TODO: test correctness
    testDigits(('rbf',10))



