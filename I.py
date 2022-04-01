# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:32:45 2022

@author: Sergio
"""
from imports import *

def I(t, P, A1, A2):
    for i, j in enumerate(t):
        if j>P/2:
            break
        
    time = np.concatenate([t[:i], t[i-1:2*i-1]])
    signal = np.concatenate([np.full(i, A1), np.full(i, A2)])
    time = np.concatenate([time, time+P, time+2*P])
    signal = np.concatenate([signal, signal, signal])
    plt.plot(time, signal, '-')
    plt.hlines(0, min(time), max(time), 'k')
    plt.xlabel('t')
    plt.ylabel('I')
    plt.grid()
    plt.show()