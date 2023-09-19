import numpy as np
import timeit
L=100

b=np.moveaxis(np.mgrid[-L:L,-L:L,-L:L], 0, -1)

sb=np.power(np.sum(np.power(b,2),axis=3),-1/2) *((-1)**abs(np.sum(b,axis=3)))
sb[L][L][L]=0
print(np.sum(sb))


##For Loop
S=0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if(i**2+j**2+k**2!=0):
                S+=(-1)**(abs(i+j+k))*(i**2+j**2+k**2)**-.5
print(S)

