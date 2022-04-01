# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:26:37 2022

@author: Sergio
"""
from imports import *

def W(t, A1, A2, P, T):
    """
    Integral of the intensity measured, done for a square signal with 
    intensities A1 and A2. The units must be the same for all the problem. 

    Parameters
    ----------
    t : array
        times, start at 0, last one greater than period
    A1 : float
        Bigger intensity
    A2 : float
        Lower intensity
    P : float
        Period of the signal
    T : float
        Sample time

    """
    
    #Constant correction so that T<P
    #If T>P, a constant is added to the integral ((A1+A2)*P/2)
    cte = T//P
    T -= P*(cte)
    #Initialize W
    W = []
    #Identify case, depending on the difference between P and T
    
    #Low T
    if T<=P/2:
        
        #Loop over times in one period
        for i, j in enumerate(t):
            #Section 1
            if j < P/2-T:
                W.append(A1*T)
            #Section 2
            elif j < P/2:
                W.append((A1-A2)*(-j+P/2) + A2*T)
            #Section 3
            elif j < P-T:
                W.append(A2*T)
            #Section 4
            elif j < P:
                W.append((A1-A2)*(j-P)+A1*T)
            #Period completed, exit the loop
            else:
                break
    #Big T    
    else:
        #Loop over times in one period
        for i, j in enumerate(t):
            #Section 1
            if j < P-T:
                W.append((A1-A2)*(-j+P/2)+A2*T)
            #Section 2
            elif j < P/2:
                W.append(-(A1-A2)*P/2 + A1*T)
            #Section 3
            elif j < 3*P/2-T:
                W.append((A1-A2)*(j-P)+A1*T)
            #Section 4
            elif j < P:
                W.append((A1-A2)*P/2+A2*T)
            #Period completed, exit the loop
            else:
                break
        
    #Add last value to complete period    
    W.append(W[0])
    return t[:i+1], np.array(W)+cte
       
        


    

    