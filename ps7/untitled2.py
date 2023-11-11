import numpy as np
import scipy.optimize as opt
def brents(f, a, b,):

    fa,fb = f(a),f(b)

    if fa*fb > 0:
        raise Exception("Initial bracketing must different signs.")

    if np.abs(fa) < np.abs(fb):
        a,b = b,a
        fa,fb = fb,fa

    c,fc = a,fa
    d,e = b-a,b-a

    for iter in range(1000):
        #quadratic interp or secant
        if fa!=fc and fb!=fc and fa!=fb:
            s=a*fb*fc /((fa-fb)*(fa-fc))+b*fa*fc/((fb-fa)*(fb-fc))+c*fa*fb/((fc-fa)*(fc-fb))
        if fa!=fb:
            s = b-fb*(b-a)/(fb-fa)
        #bisection
        bisect = (s < (3 * a + b) / 4 or s > b) or (e and abs(s - b) >= abs(d) / 2)
        if bisect:
            s= (a+b)/2

        fs = f(s)
        d, e = e, d

        if np.abs(fs) < 10**-15:
            return s, fs, iter + 1

        if fs*fb< 0:
            a, b, c = b, s, a
            fa, fb, fc = fb, fs, fa
        else:
            c,a = a,s
            fc,fa = fs,fb

        if np.abs(fa) < np.abs(fb):
            a, b = b, a
            fa, fb = fb, fa

def f(x):
    return (x-.3)**2 * np.exp(x)

brents(f, .3, 1)

opt.brent(f,brack=(0,1))