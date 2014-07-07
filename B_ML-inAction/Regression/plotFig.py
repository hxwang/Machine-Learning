#code for book Machine learning in action

import matplotlib.pyplot as plt

def plot(xMat, yMat,ws):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #create orginal data in the plot
    ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])

    #create regression curve
    xCopy = xMat.copy()
    #sort xCopy
    xCopy.sort(0)
    yHat = xCopy*ws

    #TODO: have problem with this plot, bugs
    #ax.plot(xCopy[:,1], yHat)
    plt.show()


