import numpy as np
import matplotlib.pyplot as plt
N=20
m=1
x,w=np.polynomial.legendre.leggauss(N)

def f(x,a):
    return 1/(a**4-x**4)**.5
    
def I(a):
    xi=a/2*x+a/2
    wi=a/2*w
    return np.sqrt(8*m)*np.sum(f(xi,a)*wi)
A=np.linspace(0,2,100)
ia=np.zeros(100)
for i in range(0,100):
    ia[i]=I(A[i])

plt.plot(A,ia)
plt.xlabel("amplitude (m)")
plt.ylabel ("period (s)")