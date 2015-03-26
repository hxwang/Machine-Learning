#code for book Machine learning in action

from numpy import *
import SMO as smo
import plattSMO as psmo

#TODO: restructure code, kernel.py and plattSMO.py only different in three functions
#optStruct, innerL, calcEk

#fill information in K
#kTup[0]: types of kernel function
#kTup[1],lTup[2]: parameters that kernel function will use
def kernelTrans(X, A, kTup):
    m, n = shape(X)
    K = mat(zeros((m,1)))
    if kTup[0] == 'lin': K = X*A.T
    elif kTup[0] == 'rbf':
        #radial basis function
        for j in range(m):
            deltaRow = X[j,:] - A
            K[j] = deltaRow*deltaRow.T
        K = exp(K/(-1*kTup[1]**2))
    else:
        raise NameError("We have a problem--That kernel is not recognized")
    return K

#different from optStruct in plattSMO.y
#we introduce kTup, which contains information of the kernel
class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler, kTup):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))
        self.K = mat(zeros((self.m, self.m)))
        for i in range(self.m):
            self.K[:,i] = kernelTrans(self.X, self.X[i,:], kTup)


def innerL(i, oS):
    Ei = calcEk(oS,i)
    if((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or \
            ( (oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        #improve from simple SMP
        j, Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()

        if(oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])

        if L==H:
            #print "L==H"
            return 0

        #Code different from plattSMO.py
        eta = 2.0*oS.K[i,j] - oS.K[i,i] - oS.K[j,j]

        if eta >= 0:
            #print "eta>=0"
            return 0

        oS.alphas[j] -= oS.labelMat[j]*(Ei - Ej)/eta
        oS.alphas[j] = smo.clipAlpha(oS.alphas[j], H, L)

        updateEk(oS,j)

        if(abs(oS.alphas[j] - alphaJold) < 0.00001):
            #print "j not moving enough"
            return 0

        oS.alphas[i] += oS.labelMat[j]*oS.labelMat[i]*(alphaJold - oS.alphas[j])
        updateEk(oS,i)

        #update constant b
        b1 = oS.b - Ei- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,i] - oS.labelMat[j]*(oS.alphas[j]-
            alphaJold)*oS.K[i,j]
        b2 = oS.b - Ej- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,j] - oS.labelMat[j]*(oS.alphas[j]-
            alphaJold)*oS.K[j,j]

        if(0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]): oS.b = b2
        else: oS.b = (b1+b2)/2.0
        return 1
    else: return 0

#calculate error
def calcEk(oS, k):
    fXk = float(multiply(oS.alphas, oS.labelMat).T*oS.K[:,k]) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek

def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup = ('lin',0)):
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler,kTup)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while(iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            #Arrpaoch 1: traverse entireset of alpha
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
            print "fullSet, iter: %d i %d, pairs changed %d" %(iter, i, alphaPairsChanged)
            iter += 1
        else:
            #Approach 2: traverse non-bounds alpha
            nonBoundsIs = nonzero((oS.alphas.A > 0)*(oS.alphas.A < C))[0]
            for i in nonBoundsIs:
                alphaPairsChanged += innerL(i, oS)
                print "non-bound, iter: %d i: %d, paris changed %d" %(iter, i, alphaPairsChanged)
            iter += 1

        #using both approach in interchange manner
        if entireSet: entireSet = False
        elif (alphaPairsChanged==0): entireSet = True
        print "iteration number: %d" %iter
    return oS.b, oS.alphas


#select the other alpha for pair
def selectJ(i, oS, Ei):
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    #set corresponding cached value as valid
    oS.eCache[i] = [1,Ei]
    #return the corresponding alpha of non-zero E
    validEcacheList = nonzero(oS.eCache[:,0].A)[0]

    #select the alpha j that maximum abs(Ei - Ek)
    if(len(validEcacheList)) > 1:
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if(deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        return maxK, Ej

    #if there is no such j, random select a j
    else:
        j = smo.selectJrand(i, oS.m)
        Ej = calcEk(oS,j)
    return j, Ej

def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


#test the precision of classifier
def testRbf(k1=1.3):

    #load data
    dataArr, labelArr = smo.loadDataSet('testSetRBF.txt')
    #training
    b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf',k1))
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()

    #build support vector
    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print "there are %d Support Vectors" % shape(sVs)[0]

    #training error rate
    m,n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i,:],('rbf',k1))
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print "the test error rate is: %f" %(float(errorCount)/m)

    #test error rate
    dataArr, labelArr = smo.loadDataSet('testSetRBF2.txt')
    errorCount = 0
    datMat = mat(dataArr)
    labelmat = mat(labelArr).transpose()

    m,n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i,:],('rbf',k1))
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print "the test error rate is: %f" %(float(errorCount)/m)


if __name__ == "__main__":
    testRbf()