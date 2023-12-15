import numpy as np
import scipy
import matplotlib.pyplot as plt

N=1000

hbar=6.582119569*10**-16
c=3*10**8

#.0015 1/eV ~ s
L=10**-8/(hbar*c)
#.05 eV^-1  ~1/m

m_e=.511*(10^6)
#eV ~m

sigma=10**-10/(hbar*c)
# 0.0005 eV^-1 ~m
k=(hbar*c)/(.2*10**-10)
#9873 eV ~1/m

a=L/N
h=a**2/2

a1=1+h*1j/(2*m_e*a**2)
a2=-h*1j/(4*m_e*a**2)
b1=1-h*1j/(2*m_e*a**2)
b2=h*1j/(4*m_e*a**2)

A1_diag=np.full(N,a1)
A2_diag=np.full(N-1,a2)
A=np.diag(A2_diag,1)+np.diag(A2_diag,-1)+np.diag(A1_diag)

B1_diag=np.full(N,b1)
B2_diag=np.full(N-1,b2)
B=np.diag(B2_diag,1)+np.diag(B2_diag,-1)+np.diag(B1_diag)

U=np.linalg.inv(A)@B
B=np.diag(np.full(N,1))

B[0][0]=B[-1][-1]=0
U=B@U

np.save("ps9/time_evolve matrix",U)

print(a1,a2,b1,b2)