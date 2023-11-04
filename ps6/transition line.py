import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt

hdu_list =fits.open('ps6/specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

def spec(n,m):
    L=3-np.log10(1/n**2-1/m**2)-np.log10(1.09677)
    plt.plot([L,L],[0,100],linestyle = 'dotted',lw=4,color='r')
plt.plot(logwave,flux[3])
spec(2,3)


