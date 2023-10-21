import numpy as np
import matplotlib.pyplot as plt
def I(x,a):
    return np.exp(-x+(a-1)*np.log(np.abs(x)))
xs=np.linspace(0.1,5,100)
for alpha in [2,3,4]:
    plt.plot(xs,I(xs,alpha))
plt.legend(["a=2",'a=3','a=4'])
def isint(n):
    return round(n)==n
def gamma(a):   
    if  a<0:
        if (isint(a)):
            raise Exception("Gamma function is undefined for all negative integeres")
        #Gauss reflection formula for negative non integer value analytic continuation
        else:
            return np.pi/(np.sin(np.pi*a)*gamma(1-a))
    xi,wi=np.polynomial.legendre.leggauss(50)
    xi=(xi+1)/2
    wi=wi/2     
    z=xi
    if a<1:
        c=gamma(a+1)
    #if a<1, the supposed peak of the integrand would be negative which would be undefined
    #next best is to center it around the mean which would be integral(x*e^-x*x^(a-1))=gamma(a+1)
    else:
        c=a-1
    dz=c/(z-1)**2
    return np.sum(I(z*c/(1-z),a)*dz*wi)

for i in [-3/2,-1/2,1/2,3,6,10]:
    print(gamma(i))
