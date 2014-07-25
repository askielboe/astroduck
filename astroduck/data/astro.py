import numpy as np
from .core import XYData, XYZData

class Lightcurve(XYData):
    def __init__(self, time, flux, ferr = None):
        XYData.__init__(self, time, flux, ferr, xname='Time', yname='Flux')

    @property
    def time(self):
        return self._x

    @property
    def flux(self):
        return self._y

    @property
    def ferr(self):
        return self._e

class Spectrum():
    def __init__(self, wave, flux, ferr = None):
        XYData.__init__(self, wave, flux, ferr, xname='Wavelength', yname='Flux')

    @property
    def wave(self):
        return self._x

    @property
    def flux(self):
        return self._y

    @property
    def ferr(self):
        return self._e

class Rainbow():
    def __init__(self, spectra):
        self.spectra = np.array(spectra)
        self.wavelengths = np.array(spectra[0].wavelengths)

        # Check that all spectra have the same wavelengths
        for spectrum in self.spectra:
            if False in self.wavelengths == spectrum.wavelengths:
                raise ValueError("Error: All spectra need to have the same wavelengths!")
