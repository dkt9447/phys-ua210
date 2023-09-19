import numpy as np
import matplotlib.pyplot as plt
N=1000
X,Y=np.meshgrid(np.linspace(-2,2,N),np.linspace(-2,2,N))
C=X+1j*Y
I=1000
Z=np.zeros(C.shape)
S=np.empty(C.shape)
for i in range(I):
    Z=Z**2+C
    S+=np.abs(Z)>2
plt.imshow(S,cmap='gray')
plt.imshow(S,cmap='jet')
plt.imshow(S,cmap='hot')
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()