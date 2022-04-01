# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:34:15 2022

@author: Sergio
"""
from imports import *


def mom2(M, P, num05):
    """
    Second order factorial moment for a square signal with M=(A1-A2)/(A1+A2)
    and period P, measured in a sample time T and evaluated in num points
    between 0 and 1 with intervals dTP

    Parameters
    ----------
   
    M : float, adimensional
        Relation between intensities A1 (big) and A2 (low), defined as 
        (A1-A2)/(A1+A2). It goes from 0 (A1=A2, constant signal) to 1
        (A2=0)
        
    P: float
        Period of the signal
    
    num05 : int
        half the number of points in which evaluate the function, as it has to
        be evaluated separatedly before and after T=P/2. Final result will have
        2*num05+1 elements, as 0 isn't conted

    Returns
    -------
    Arrays with T (uits of P) and second order factorial moment for the given M

    """
    #Get the step, easier computing
    step = 0.5*nv(P)/num05
    
    #Define sample times arrays
    #First part, from 0 to 0.5P
    T1 = np.arange(0, 0.5*nv(P)+step, step)
    #second part, from 0.5P to P
    T2 = np.arange(0.5*nv(P)+step, nv(P)+step, step)
    
    #M sqaure
    M2 = M**2
    
    #Get second order factorial moment
    #From T=0 to P/2
    n1 = 1 + M2 * (1 - (4*T1)/(3*P))
    #From T=P/2 to P
    n2 = 1 + M2 * (2*P/T2 + 4/3*T2/P - 1/3*P**2/T2**2 - 3)
    
    #return T, n
    return np.concatenate([T1, T2]), np.concatenate([n1, n2])

def mom2_arr(T, M, P):
    m = []
    M2 = M**2
    for i in T:
        i-=i//P
        if i<P/2:
            m.append(1 + M2 * (1 - (4*i)/(3*P)))
        else:
            m.append(1 + M2 * (2*P/i + 4/3*i/P - 1/3*P**2/i**2 - 3))
    return np.array(m)


def mom2_single(T, M, P):
    #T correction so that T<P
    T -= T//P
    M2 = M**2
    #Low sample time
    if T<P/2:
        return 1 + M2 * (1 - (4*T)/(3*P))
    else:
        return 1 + M2 * (2*P/T + 4/3*T/P - 1/3*P**2/T**2 - 3)