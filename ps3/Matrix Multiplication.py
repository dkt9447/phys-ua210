import numpy as np
N=1000
S=0
A=np.random.rand(N,N)
B=np.random.rand(N,N)
C=np.empty([N,N])
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j]+=A[i,k]*B[k,j]
            S+=1
