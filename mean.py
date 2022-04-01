# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:51:05 2022

@author: Sergio
"""
from imports import *
def get_mean(x):
    """
    Given array of ufloats, computes the mean with errors
    """
    x_m = 0
    aux = []
    n = len(x)
    for i in x:
        x_m += i/len(x)
        aux.append(nv(i))
    print('From the mean: ',x_m)
    
    err = np.std(aux)
    print('Standard deviation: ', err)
    dx = np.sqrt(sd(x_m)**2+err**2)
    return ufloat(nv(x_m), dx)