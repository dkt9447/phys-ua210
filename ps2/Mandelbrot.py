import numpy as np
import matplotlib.pyplot as plt
N=100
X,Y=np.meshgrid(np.linspace(-2,.5,N),np.linspace(-1.25,1.25,N))
C=X+1j*Y
I=100
Z=np.zeros(C.shape)
S=np.empty(C.shape)
for i in range(I):
    Z=Z**2+C
    S+=np.abs(Z)>2
plt.imshow(S,cmap='gray')
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
np.min(S)