#code for book Machine learning in action

from numpy import *
import SMO as smo

#using class in order for storage values as structure
#note here using class is not for OOP
class optStruct:
    #init members
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m,1)))
        self.b = 0
        #cache for erros
        #the first column is using for indication(1 means valid, 0 means invalid)
        #valid means the calculation is done
        self.eCache = mat(zeros((self.m,2)))

#calculate error
def calcEk(oS, k):
    fXk = float(multiply(oS.alphas, oS.labelMat).T *(oS.X*oS.X[k,:].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek

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

        eta = 2.0*oS.X[i,:]*oS.X[j,:].T - oS.X[i,:]*oS.X[i,:].T - oS.X[j,:]*oS.X[j,:].T
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
        b1 = oS.b - Ei- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[i,:].T - oS.labelMat[j]*(oS.alphas[j]-
            alphaJold)*oS.X[i,:]*oS.X[j,:].T
        b2 = oS.b - Ej- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.X[i,:]*oS.X[j,:].T - oS.labelMat[j]*(oS.alphas[j]-
            alphaJold)*oS.X[j,:]*oS.X[j,:].T

        if(0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]): oS.b = b2
        else: oS.b = (b1+b2)/2.0
        return 1
    else: return 0


def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup = ('lin',0)):
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler)
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

def calcWs(alphas, dataArr, classLables):
    X = mat(dataArr)
    labelMat = mat(classLables).transpose()
    m,n = shape(X)
    w = zeros((n,1))
    for i in range(m):
        w += multiply(alphas[i]*labelMat[i], X[i,:].T)
    return w


def main():
    print '-----------------------load data and training-----------'
    dataArr, labelArr = smo.loadDataSet('testSet.txt')
    b, alphas = smoP(dataArr, labelArr, 0.6, 0.001, 40)
    print "b", b
    print "alphas > 0", alphas[alphas > 0]

    #calculate weights
    print '-----------------------calculate weights----------------'
    ws = calcWs(alphas, dataArr, labelArr)
    print "ws", ws

    print '-----------------------test classify result----------------'
    #process first node
    datMat = mat(dataArr)
    print "first node classify to: ", datMat[0]*mat(ws) + b
    print "first node true label:", labelArr[0]

    #process third node
    print "third node classify to: ", datMat[2]*mat(ws) + b
    print "third node true label: ", labelArr[2]

if __name__ == "__main__":
    main()

