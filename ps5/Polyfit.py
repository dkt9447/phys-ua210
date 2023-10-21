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
plt.figure(0)
plt.scatter(t,sig)
plt.xlabel('Dimensionless Time')
plt.ylabel('Signal')
def poly_SVD(ivar,dvar,n):
    A=np.vander(ivar,n,increasing=True)
    (U, w, VT) = np.linalg.svd(A)
    Winv=np.zeros((len(VT),(len(U))))
    Winv[:len(w),:len(w)]=np.diag(1/w)
    ainv=VT.transpose().dot(Winv).dot(U.transpose())
    return ainv.dot(dvar)
def poly_fit(x,c,n):
    return np.vander(x,n,increasing=True).dot(c)
def cond_number(ivar,dvar,n):
    A=np.vander(ivar,n,increasing=True)
    (U, w, VT) = np.linalg.svd(A)
    return (max(w)/min(w))

sigFit4=poly_fit(tIn,poly_SVD(t,sig,4),4)

plt.plot(tIn,sigFit4,color='purple')

plt.figure(1)

res4=(sigFit4-sig)
print(np.std(res4))
res=plt.hist(res4,bins=21)
plt.xlabel("Residuals")
a=[]
N=20
for i in range(1,N):
    a.append(cond_number(t, sig, i))
a=np.abs(a)

r=np.where(a[a<10**12]==max(a[a<10**12]))[0][0]

print("Highest order polynomial within machine precision is at order " + str(r-1)+ " with condition number " +  str(a[r]) )

sigFitReasonable=poly_fit(tIn,poly_SVD(t,sig,r),r)
plt.figure(0)
plt.plot(tIn,sigFitReasonable,color='orange')
plt.legend(["signal","third order","reasonable order"])
