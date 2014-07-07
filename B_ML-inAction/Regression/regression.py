#code for book Machine learning in action

from numpy import *

import plotFig

import matplotlib.pyplot as plt

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))-1
    dataMat = []; labelMat= []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat

    #calculate det
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat)
    #NumPy provide a linear solver, linalg.solve(xTx, xMat.T*yMatT)
    return ws

def main():
    xArr, yArr = loadDataSet('ex0.txt')
    print xArr[0:2]
    ws = standRegres(xArr, yArr)
    print "ws", ws

    xMat = mat(xArr); yMat = mat(yArr)
    yHat = xMat * ws

    #plotFigure
    plotFig.plot(xMat, yMat, ws)

    #coefficient
    #the result will show that the coefficiency between yHat and yMat is 0.98
    print "corrcoef", corrcoef(yHat.T, yMat)

if __name__ == '__main__':
    main()

