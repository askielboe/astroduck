import matplotlib.pyplot as plt

def xyplot(x, y, yerr = None, xlabel = None, ylabel = None):

    plt.figure()

    if yerr:
        plt.errorbar(x, y, yerr)
    else:
        plt.plot(x, y)

    if xlabel:
        plt.xlabel(xlabel)

    if ylabel:
        plt.ylabel(ylabel)

    plt.show()
