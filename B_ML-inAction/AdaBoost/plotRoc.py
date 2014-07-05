#code for book Machine learning in action

import matplotlib.pyplot as plt
from numpy import *

import horseColic as hc
import adaboost as ab

def plotRoc(predStrengths, classLabels):
    #plot from (1.0,1.0) to (0,0)
    cur = (1.0, 1.0)
    ySum = 0.0
    numPosClas = sum(array(classLabels)==1.0)
    yStep = 1/float(numPosClas)
    xStep = 1/float(len(classLabels)-numPosClas)
    #get sorted indices
    sortedIndices = predStrengths.argsort()
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndices.tolist()[0]:
        if classLabels[index] == 1.0:
            delX =0;  delY = yStep
        else:
            delX = xStep; delY = 0
            #ySum: use to calculate value of AUC
            ySum += cur[1]
        ax.plot([cur[0], cur[0]-delX], [cur[1],cur[1]-delY], c ='b')
        cur = (cur[0]-delX, cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0,1,0,1])
    plt.show()
    print "the Area under the Curve is: ", ySum * xStep


def main():
    datArr, labelArr = hc.loadDataSet('horseColicTraining2.txt')
    classiferArray, aggClassEst = ab.adaBoostTrainDS(datArr, labelArr, 10)
    plotRoc(aggClassEst.T, labelArr)

if __name__ == '__main__':
    main()