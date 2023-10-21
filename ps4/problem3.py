import matplotlib.pyplot as plt
import numpy as np
import math

NL=50
NH=4
def H(n,x):
    if n==0:
        return 1
    if n==1:
        return 2*x
    return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)



def Rpsi(n,x):
    return H(n,x)*1/np.sqrt(2**n*math.factorial(n)*np.sqrt(math.pi))
#defining a reduced wave function without exp(-x^2/2) term such that when squared to find observables
#the integral is of the form exp(-x^2) thus use gaussian hermite quadrature
def psi(n,x):
    return Rpsi(n,x)*np.exp(-x**2/2)
#actual psi


A=np.linspace(-10,10,1000)
B=np.linspace(-4,4,250)
plt.plot(B,psi(0,B))
plt.plot(B,psi(1,B))
plt.plot(B,psi(2,B))
plt.plot(B,psi(3,B))
plt.legend(['n=0','n=1','n=2','n=3'])
plt.xlabel('Distance (dimentionless) ')
plt.ylabel('Amplitude (dimentionless) ')
plt.show()
plt.plot(A,psi(10,A))
plt.xlabel('Distance (dimentionless) ')
plt.ylabel('Amplitude (dimentionless) ')
x,w=np.polynomial.hermite.hermgauss(15)
np.sqrt(np.sum(x**2*Rpsi(5,x)**2*w))



def rmsX(n):
    x,w=np.polynomial.hermite.hermgauss(2*n)
    #weights for 2n polynomial that one should expect for
    np.sqrt(np.sum(x**2*Rpsi(5,x)**2*w))
    return np.sqrt(np.sum(x**2*Rpsi(n,x)**2*w))
def rmsXL(n):
    xl,wl=np.polynomial.legendre.leggauss(NL)
    z=xl/(1-xl**2)
    #coord transform
    dz=(1+xl**2)/(1-xl**2)**2
    #jacobian
    return np.sqrt(np.sum(z**2*psi(5,z)**2*wl*dz))

rmsXL(5)