import numpy as np
import matplotlib.pyplot as plt
#Define f(x)
def f(x):
    return((x-1)*x)
t=np.linspace(-1,-14,131)
#Powers of 10 to use as delta
d=np.float_power(10,t)
#values of delta
x0=1
#point of derivative
empdir=(f(x0+d)-(f(x0)))/d
#numerical derivative
andir=2*x0-1
#analytical derivative
rerror=(empdir-andir)/andir
plt.plot(-t,abs(rerror))
plt.xlabel("-Log(delta)")
plt.ylabel("Relative error")
print(empdir[10],empdir[30],empdir[50],empdir[70],empdir[90],empdir[110],empdir[130])
#numerical derivative at d=10^(-2,-4,-6,-8,-10,-12,-14)
print(rerror[10],rerror[30],rerror[50],rerror[70],rerror[90],rerror[110],rerror[130])
#relative error at d=10^(-2,-4,-6,-8,-10,-12,-14)