import jax.numpy as jnp
import jax
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from mpl_toolkits import mplot3d
filename = r"ps7/survey.csv"
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields=next(csvreader)
    width=len(fields)
    length=0
    for row in csvreader:
        length=length+1
    data=np.empty([length,width])
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields=next(csvreader)
    i=0
    for row in csvreader:
        data[i]=row
        i=i+1
age=data[:,0]
yn=data[:,1]
def model(x,params):
    b0=params[0]
    b1=params[1]
    return 1/(1+jnp.exp(-(b0+b1*x)))
def like(params):
    probs=1-yn+model(age,params)*(2*yn-1)

    #1-p if a=0, p if a=1
    probs+=10**-1
    #prevent inf
    return jnp.sum(-jnp.log(probs))

likegrad=jax.grad(like)
plt.scatter(age,yn)
xs=np.arange(0,80)
ini=[-10,.5]
r=optimize.minimize(like, ini, jac=likegrad, method='BFGS', tol=1e-6)
print(r.x)
plt.plot(xs,model(xs,r.x))
plt.xlabel("Age (years)")
hessian=jax.hessian(like)
cov=np.linalg.inv(hessian(r.x))
sigma_b0=np.sqrt(cov[0,0])
sigma_b1=np.sqrt(cov[1,1])
print(cov)

