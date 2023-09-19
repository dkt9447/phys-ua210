import numpy as np
def roots1(a,b,c):
    return ((-b+(b**2-4*a*c)**.5)/(2*a),(-b-(b**2-4*a*c)**.5)/(2*a))
def roots2(a,b,c):
    return (2*c/(-b-(b**2-4*a*c)**.5),2*c/(-b+(b**2-4*a*c)**.5))
def roots(a,b,c):
    if np.abs((-b+(b**2-4*a*c)**.5)>np.abs(2*a)):
        return roots2(a,b,c)
    return roots1(a,b,c)