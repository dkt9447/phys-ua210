# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:09:17 2023

@author: donov
"""

import numpy as np
import matplotlib.pyplot as plt
xs=np.linspace(-10, 10,1000)
ys=1/(3*np.sqrt(2*np.pi))*np.exp(-xs**2/9)
plt.plot(xs,ys)
plt.savefig('gaussian')