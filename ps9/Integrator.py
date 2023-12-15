import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
N=1000

hbar=6.582119569*10**-16
c=3*10**8

#.0015 1/eV ~ s
L=10**-8/(hbar*c)
#.05 eV^-1  ~1/m

m_e=.511*(10^6)
#eV ~m

sigma=10**-10/(hbar*c)
# 0.0005 eV^-1 ~m
k=(hbar*c)/(.2*10**-10)
#9873 eV ~1/m

a=L/N

U=np.load('time_evolve matrix.npy')
U=np.linalg.matrix_power(U,1000)
#faster time evolvution 
def initial(x):
    y= np.exp(-(x-3*L/4)**2/(16*sigma**2))*np.exp(-1j*k*x)/4
    y+= np.exp(-(x-1*L/4)**2/(16*sigma**2))*np.exp(1j*k*x)/4
    y[0]=0
    y[-1]=0
    return y

x=np.linspace(0,L,N)
init_wave=initial(x)


def evolve():
    global P
    P=U@P
P=U@init_wave
# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot initialization
line, = ax.plot(x, np.real(P), np.imag(P), label='Wave Function')

ax.set_xlabel('X (eV^-1)')
ax.set_ylabel('Real')
ax.set_zlabel('Imaginary')
ax.legend()


def init():
    line.set_data(x, np.real(P))
    line.set_3d_properties(np.imag(P))
    return line,


def update(frame):
    evolve()
    line.set_data(x, np.real(P))
    line.set_3d_properties(np.imag(P))
    return line,

ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=False, interval=100)

ani.save('ps9/anim.gif',dpi=100)
