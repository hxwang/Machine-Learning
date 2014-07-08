#code for book Machine learning in action

import lwlr
import regression as reg

def rssErr(yArr, yHatArr):
    return ((yArr - yHatArr)**2).sum()


def main():
    abX, abY = reg.loadDataSet('abalone.txt')
    yHat01 = lwlr.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
    error01 = rssErr(abY[0:99], yHat01.T)
    yHat1 = lwlr.lwlrTest(abX[0:99], abX[0:99], abY[0:99],1)
    error1 = rssErr(abY[0:99], yHat1.T)
    yHat10 = lwlr.lwlrTest(abX[0:99], abX[0:99], abY[0:99],10)
    error10 = rssErr(abY[0:99],yHat10.T)
    #the result show smaller kernel
    print "yHat01:", yHat01, "error01:", error01
    print "yHat1", yHat1, "error1:", error1
    print "yHat10",yHat10, "error10", error10

if __name__ == '__main__':
    main()

