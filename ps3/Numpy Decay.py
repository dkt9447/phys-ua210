import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

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

#Numpy implementation 
for i in range(int(tmax/t)-1):
    BiDecay=chance(BiAtoms,PrBi)
    #Determines number of Bi Atoms that decayed
    BiAtoms-=BiDecay
    #Removes the number of Bi decayed atoms
    PbNotTi=chance(BiDecay,.9791)
    #Number of Atoms of Bi that decayed into Pb
    PbAtoms+=PbNotTi
    #Increases number of Pb atom by that amount 
    TiAtoms+=(BiDecay-PbNotTi)
    #Increases number of Ti atoms by the remaining Bi decay atoms
    TiDecay=chance(TiAtoms,PrTi)
    #Number of Ti atoms that decayed into Pb
    TiAtoms-=TiDecay
    PbAtoms+=TiDecay
    #Adjusts Ti atom and Pb atom count accordingly
    PbDecay=chance(PbAtoms,PrPb)
    #Determines number of Pb Atoms that decayed
    PbAtoms-=PbDecay
    Bi209Atoms+=PbDecay
    Bi213Count=np.append(Bi213Count,BiAtoms)
    PbCount=np.append(PbCount,PbAtoms)
    TiCount=np.append(TiCount,TiAtoms)
    Bi209Count=np.append(Bi209Count,Bi209Atoms)
    #Records current count of atoms in each array 

plt.plot(time,Bi213Count)
plt.plot(time,Bi209Count)
plt.plot(time,PbCount)
plt.plot(time,TiCount)

plt.xlabel("Time (s)")
plt.ylabel("Atoms")
plt.title('Numpy Implementation ')
plt.legend(['Bi203','Bi209','Pb','Ti'])