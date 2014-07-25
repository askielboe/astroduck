import numpy as np
from ..visual.plot import xyplot

def check_list_lenghts_are_equal(list_of_lists):
    n = len(list_of_lists[0])
    if not all(len(x) == n for x in list_of_lists if x is not None):
        raise ValueError("Data dimensions must be compatible - not all input arrays are the same length!")

class XYData(object):
    def __init__(self, x, y, e = None, xname = None, yname = None, xunit = None, yunit = None):

        check_list_lenghts_are_equal([x, y, e])

        self._x = np.array(x)
        self._y = np.array(y)
        self._e = np.array(e)

        self.xname = xname
        self.yname = yname

        self.xunit = xunit
        self.yunit = yunit

        self._xlabel = None
        self._ylabel = None

    @property
    def xlabel(self):
        if self.xunit:
            self._xlabel = "{name} [{unit}]".format(name=self.xname, unit=self.xunit)
        else:
            self._xlabel = self.xname
        return self._xlabel

    @property
    def ylabel(self):
        if self.xunit:
            self._ylabel = "{name} [{unit}]".format(name=self.yname, unit=self.yunit)
        else:
            self._ylabel = self.yname
        return self._ylabel

    def plot(self):
        xyplot(self._x, self._y, yerr=self._e, xlabel=self.xlabel, ylabel=self.ylabel)
