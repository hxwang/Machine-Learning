#code for book Machine learning in action

from numpy import *
import matplotlib.pyplot as plt

#load dataset from file, process data
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        #x0=1, x1,x2 are values
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        #x3 is labels
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

#sigmoid
def sigmoid(inX):
    return 1.0/(1+exp(-inX))

#gradient ascent to find weights
def gradAscent(dataMatIn, classLabels):
    #convert to NumPy matrix
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    #gradient ascent to change weights
    weights = ones((n,1))
    for k in range(maxCycles):
        #h and error are both values
        h = sigmoid(dataMatrix*weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

#plot regression line
def plotBestFit(wei):
    #TODO: fix error
    #when using function 'gradAscent', it works with: wieghts = wei.getA()
    #when using function 'stocGradAscent', it works with: weights = wei
    weights = wei
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    #divided nodes based on their labels
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    #plot nodes in different colors
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    #let sigmoid =0
    #0 = w0*x0 + w1*x1 + w2*x2, x0=1
    #therefore, we can get y by the following equation
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

#stochastic gradient ascent
#idea: each time random pick a sample to adjust the weights
def stocGradAscent0(dataMatrix, classLabels):
    #m: number of samples
    #n: number of features + 1
    m, n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        #h and error are both vectors
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights


#improvement version of stochastic gradient ascent
def stocGradAscent1(dataMatrix, classLabels, numIters = 150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIters):
        dataIndex = range(m)
        for i in range(m):
            #update alpha every time
            alpha = 4/(1+j+i)+0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            #random choose for update and then delete it
            #advantage: can avoid periodic changing in values of weights
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights





if __name__ == '__main__':

    print '-------------------gradient ascent-------------'
    #dataArr, labelMat = loadDataSet()
    #weights = gradAscent(dataArr, labelMat)
    #plotBestFit(weights)

    print '----------------stochastic gradient ascent---------'
    #dataArr, labelMat = loadDataSet()
    #weights = stocGradAscent0(array(dataArr), labelMat)
    #plotBestFit(weights)

    print '--------------improved stochastic gradient ascent------'
    dataArr, labelMat = loadDataSet()
    weights = stocGradAscent1(array(dataArr), labelMat)
    plotBestFit(weights)