import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt


hdu_list =fits.open('ps6/specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
flux=flux[:500,:1000]
logwave =logwave[:1000]
def spec(n,m):
    L=3-np.log10(1/n**2-1/m**2)-np.log10(1.09677)
    plt.plot([L,L],[0,100],linestyle = 'dotted',lw=4,color='r')

norm=np.sum(flux,axis=1)
flux/=norm[:,np.newaxis]
mean=np.mean(flux,axis=1)
flux-=mean[:,np.newaxis]
S=np.cov(flux)
val,vec=np.linalg.eig(S)
vec=vec[:, np.argsort(val)[::-1] ]

u,w,v=np.linalg.svd(S)
v[0,:]*=-1*v[0,:]
print(
np.sum(np.abs(v-vec)/vec)/1000**2,
np.max(flux)/np.min(flux),
np.max(S)/np.min(S),

)
