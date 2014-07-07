#code for book Machine learning in action

from numpy import *
import matplotlib.pyplot as plt

import regression as reg

def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I *(xMat.T*(weights*yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat

def plot(xArr, yArr):
    xMat = mat(xArr)
    srtInd = xMat[:,1].argsort(0)
    xSort = xMat[srtInd][:,0,:]
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #TODO: have problem plot the regression line
    #ax.plot(xSort[:,1],yHat[srtInd])

    ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
    plt.show()

def main():
    xArr, yArr = reg.loadDataSet('ex0.txt')
    print yArr[0]
    print lwlr(xArr[0], xArr, yArr, 1.0)
    print lwlr(xArr[0], xArr, yArr, 0.001)

    yHat = lwlrTest(xArr, xArr, yArr, 0.003)
    print "yHat:", yHat

    plot(xArr, yArr)


if __name__ == '__main__':
    main()

