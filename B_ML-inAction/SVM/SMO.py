#code for book Machine learning in action

from numpy import *

#load and process data from file
def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

#select random index of alpha
def selectJrand(i,m):
    j = i
    while(j==i):
        j = int(random.uniform(0,m))
    return j

#adjust aj if it larger than H or smaller than L
def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


#simple version of smo
#it traverse all alpha, for each alpha, it random select the other one to pair with it
#the selected pair alpha will be optimize together

#toler is the tolerate rate of error
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    #m is number of sample
    #n is number of features
    b =0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    iter = 0
    while(iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            #predict label of i
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            #error between prediction and true label
            Ei = fXi - float(labelMat[i])

            #alpha can be optimized
            #elimiated two cases: 1)alpha already be tuned to be 0 or C
            if((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                #random select second alpha to pair
                j = selectJrand(i,m)
                #calcualte error
                fXj = float(multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()

                #ensure 0 <= alpha <= C
                if(labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j]-alphas[i])
                    H = min(C, C+alphas[j]-alphas[i])
                else:
                    L = max(0, alphas[j]+alphas[i]-C)
                    H = min(C, alphas[j] + alphas[i])

                if L==H:
                    #print "L==H"
                    continue

                #change of alpha j
                eta = 2.0 * dataMatrix[i,:] * dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T  - dataMatrix[j,:]*dataMatrix[j,:].T
                #TODO: here we simplified by igore the case eta==0
                if eta >= 0:
                    print "eta>=0"; continue

                #adjust i by delta, and adjust j by -delta
                alphas[j] -= labelMat[j] * (Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j], H, L)

                if(abs(alphas[j] - alphaJold) < 0.00001):
                    #print "j not moving enough"
                    continue

                #set constant item b
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - labelMat[i] * (alphas[i]-alphaIold) * dataMatrix[i,:] * dataMatrix[i,:].T - \
                    labelMat[j] * (alphas[j]-alphaJold) * dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej - labelMat[i] * (alphas[i]-alphaIold) - dataMatrix[i,:] * dataMatrix[j,:].T - \
                    labelMat[j]*(alphas[j]-alphaJold) * dataMatrix[j,:] * dataMatrix[j,:].T
                if(0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1+b2)/2.0
                alphaPairsChanged += 1
                print "iter: %d i: %d, pairs changed %d" %(iter, i, alphaPairsChanged)

        #check if alpha is updated
        #only when alpha is no longer updated for maxInter time, the program will stop
        if(alphaPairsChanged == 0): iter += 1
        else: iter = 0
        print "iteration number: %d" % iter
    return b, alphas





if __name__ == '__main__':
    dataArr, labelArr = loadDataSet('testSet.txt')
    print dataArr
    print labelArr
    b, alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
    print 'b', b
    #print 'alpha', alphas
    print 'alphas>0', alphas[alphas>0]