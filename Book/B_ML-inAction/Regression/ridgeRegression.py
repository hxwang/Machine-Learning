#code for book Machine learning in action

from numpy import *
import regression as reg
import matplotlib.pyplot as plt
import ridgeRegression as ridgeReg


#introduce lambda to punish large w
#ridge come from the name of eye matrix
def ridgeRegress(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1])*lam
    if linalg.det(denom) == 0.0:
        print "This matrix is singlular, cannot do inverse"
        return
    ws = denom.I*(xMat.T * yMat)
    return ws

def ridgeTest(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T

    #normalized data
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMeans = mean(yMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegress(xMat, yMat, exp(i-10))
        wMat[i,:] = ws.T
    return wMat

def plotFigure(ridgeWeights):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()

def main():
    abX, abY = reg.loadDataSet('abalone.txt')
    ridgeWeights = ridgeTest(abX, abY)
    plotFigure(ridgeWeights)

if __name__ == "__main__":
    main()






