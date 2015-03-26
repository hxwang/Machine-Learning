#code for book Machine learning in action

from numpy import *
import regression as reg
import predictAge as pa
import operator

def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat,0)   #calc mean then subtract it off
    inVar = var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat

#eps: step size
def stageWise(xArr, yArr, eps=0.01, numIt=100):

    #normalize data
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMat = regularize(xMat)

    m,n = shape(xMat)
    returnMat = zeros((numIt,n))
    ws = zeros((n,1))
    wsTest = ws.copy()
    wsMat = ws.copy()

    for i in range(numIt):
        #print ws.T
        lowerError = inf

        #for each feature, increase, or decrease
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                #change weight to get new value
                wsTest[j] += eps*sign
                yTest = xMat * wsTest
                rssE = pa.rssErr(yMat.A, yTest.A)
                #update lowerError
                if rssE < lowerError:
                    lowerError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:] = ws.T
    return returnMat



def main():
    xArr, yArr = reg.loadDataSet('abalone.txt')
    rntMat =  stageWise(xArr, yArr,0.01,200)
    print rntMat
    

if __name__ == "__main__":
    main()