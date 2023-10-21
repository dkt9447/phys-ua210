import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###converting dat file to np array##
signal = pd.read_csv('ps5/signal.dat',sep="|",usecols=[1,2])
signal=signal.to_numpy()
###scaling t so theres no operations of order 10^8
t=np.transpose(signal)[0]
t=t-np.mean(t)
t=t/np.sqrt(np.sum(t**2))
sig=np.transpose(signal)[1]
tIn=np.linspace(min(t),max(t),1000)
plt.scatter(t,sig)

def cos_SVD(ivar,dvar,n):
    k=4*np.pi/(max(ivar)-min(ivar))
    A=np.real(np.vander(np.exp(1j*ivar*k),n,increasing=True))
    (U, w, VT) = np.linalg.svd(A)
    indx = np.where(w > 1.e-15)[0]
    w[indx] = 1. / w[indx]
    Winv=np.zeros((len(VT),(len(U))))
    Winv[:len(w),:len(w)]=np.diag(w)
    ainv=np.conjugate(VT.transpose()).dot(Winv).dot(U.transpose())
    return ainv.dot(dvar)
def cos_fit(x,c,n):
    k=4*np.pi/((max(x)-min(x)))
    f=np.real(np.vander(np.exp(1j*x*k),n,increasing=True).dot(c))
    return(f)


def sin_SVD(ivar,dvar,n):
    k=4*np.pi/(max(ivar)-min(ivar))
    A=np.imag(np.vander(np.exp(1j*ivar*k),n,increasing=True))
    (U, w, VT) = np.linalg.svd(A)
    indx = np.where(w > 1.e-15)[0]
    w[indx] = 1. / w[indx]
    Winv=np.zeros((len(VT),(len(U))))
    Winv[:len(w),:len(w)]=np.diag(w)
    ainv=np.conjugate(VT.transpose()).dot(Winv).dot(U.transpose())
    return ainv.dot(dvar)
def sin_fit(x,c,n):
    k=4*np.pi/((max(x)-min(x)))
    f=np.imag(np.vander(np.exp(1j*x*k),n,increasing=True).dot(c))
    return(f)

s=[]
c=[]
for i in range(18):
    Scoef=sin_SVD(t,sig,i)
    Sfit=sin_fit(tIn,Scoef,i)
    Ccoef=cos_SVD(t,sig,i)
    Cfit=cos_fit(tIn,Ccoef,i)
    s.append(np.sum(sig-Sfit)**2)
    c.append(np.sum(sig-Cfit)**2)
#smallest residuals  
Sbest=np.where(s==min(s))[0][0]
Cbest=np.where(c==min(c))[0][0]

Ccoef=cos_SVD(t,sig,Cbest)
Cfit=cos_fit(tIn,Ccoef,Cbest)
plt.plot(tIn,Cfit,color="orange")
domCosFreqy=np.where(np.abs(Ccoef)==max(np.abs(Ccoef)))[0][0]
Scoef=sin_SVD(t,sig,Sbest)
Sfit=sin_fit(tIn,Scoef,Sbest)
plt.plot(tIn,Sfit,color="purple")
domSinFreq=np.where(np.abs(Scoef)==max(np.abs(Scoef)))[0][0]
print(domCosFreqy,domSinFreq)