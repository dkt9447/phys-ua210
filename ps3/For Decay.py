import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from random import random
def chance(A,P):
    d=rand.rand(A)
    return(d[d<P].size)
#Takes an integer, A ,and real number, p, returns number of elements in A with size less than p. 

N=1000 #initial number of atoms
t=1 #time step in fractions of seconds
tmax=20000 #max time in seconds
time=np.linspace(0,tmax,int(tmax/t))#initialize a time array 
LBi=46*60 
PrBi=1-2**(-t/LBi)
LTi=2.2*60
PrTi=1-2**(-t/LTi)
LPb=3.3*60
PrPb=1-2**(-t/LPb)
#initialize half-lives and decay probabilities for each species
Bi213Count=np.array(1000)
TiCount=np.array(0)
PbCount=np.array(0)
Bi209Count=np.array(0)
#initialize records of each species to be later plotted
BiAtoms=N
TiAtoms=0
PbAtoms=0
Bi209Atoms=0
#initialize current number of atoms of each species
#For loop implementation
for i in range (int(tmax/t)-1):
    BiDecay=0
    TiDecay=0
    PbDecay=0
    Bi213Count=np.append(Bi213Count,BiAtoms)
    PbCount=np.append(PbCount,PbAtoms)
    TiCount=np.append(TiCount,TiAtoms)
    Bi209Count=np.append(Bi209Count,Bi209Atoms)
    #Same implementation as textbook, looping over current count of each species and subsequently adding or subtracting
    #Accourding to each decay probability
    for j in range(BiAtoms):
        if random()<PrBi:
            BiDecay+=1
    BiAtoms-=BiDecay
    for k in range(BiDecay):
        if random()<.9791:
            PbAtoms+=1
        else:
            TiAtoms+=1
    for l in range(TiAtoms):
        if random()<PrTi:
            TiDecay+=1
    TiAtoms-=TiDecay
    PbAtoms+=TiDecay
    for m in range(PbAtoms):
        if random()<PrPb:
            PbDecay+=1
    PbAtoms-=PbDecay
    Bi209Atoms+=PbDecay

plt.plot(time,Bi213Count)
plt.plot(time,Bi209Count)
plt.plot(time,PbCount)
plt.plot(time,TiCount)

plt.xlabel("Time (s)")
plt.ylabel("Atoms")
plt.title('For Loop Implementation ')
plt.legend(['Bi203','Bi209','Pb','Ti']) 

