# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:34:55 2022

@author: Sergio
"""
from imports import *
from mom2 import mom2_arr

def chi2(mom_exp, T, M, P):
    m = mom2_arr(T, M, P)
    res = 1/len(T)*np.sum(mom_exp-mom2_arr(T, M, P))**2
    return res
