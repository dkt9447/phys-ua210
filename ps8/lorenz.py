import jax.numpy as jnp
from jax import grad,jit,vmap
import jax


from scipy import integrate
import matplotlib.pyplot as plt
sigma=10
r=28
b=8/3
def fun(Q):
    return jnp.asarray([sigma*(Q[1]-Q[0]),r*Q[0]-Q[1]-Q[0]*Q[2],Q[0]*Q[1]-b*Q[2]])
def jac(t,Q):
    return jnp.asarray(jax.jacfwd(fun)(Q))
def funt(t,Q):
    return fun(Q)

Q0=[0.,1.,0.]


r=integrate.solve_ivp(funt, [0,50], Q0,method="BDF",jac=jac)
plt.plot(r.y[0],r.y[1])
plt.xlabel('x')
plt.ylabel('y')

plt.show(1)
plt.plot(r.y[0],r.y[2])
plt.xlabel('x')
plt.ylabel('z')
plt.show(2)
plt.plot(r.y[1],r.y[2])
plt.xlabel('y')
plt.ylabel('z')

plt.show(3)
plt.plot(r.t,r.y[1])
plt.xlabel('t')
plt.ylabel('y')
# ax = plt.figure().add_subplot(projection='3d')
# ax.scatter(r.y[0],r.y[1],r.y[2],c=r.t,s=.5,cmap='summer')
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# plt.show()