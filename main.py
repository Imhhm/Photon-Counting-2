# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:13:45 2022

@author: Sergio
"""
from imports import *
from I import I
from W import W
from mom2 import mom2, mom2_arr
from chi2 import chi2
from mean import get_mean
def plot(x, y, color, M):
    plt.plot(x, y, color=color, label=f'M={M}')

def show(xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()
    
def main():
    A1 = 10
    A2 = 7
    P = 2
    T = 0.25
    t = np.arange(0, 10, 0.05)
    # I(t, P, A1, A2)
    tm, w = W(t, A1, A2, P, T)
    plt.plot(tm, w, 'b')
    # plt.vlines(P/2-T, 0, A1*T, 'k')
    plt.ylabel('W')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    M = [0.1, 0.3, 0.5, 0.75, 1]
    color = ['b', 'g', 'r', 'purple', 'k']
    
    for i in range(len(M)):
        x, y = mom2(M[i], P, 50)
        x/=P
        plot(x, y, color[i], M[i])
    # plt.plot(0, 1.27, 'or')
    show(r'$T/P$', r'$n^{(2)}$')
    
    
def exp():
    #Characterize signal with unknown M, P
    
    #Sample times that were measured
    T = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9.9])
    #Values of n2 measured. For each value of T it was measured 10 times
    #Each row for a value of T, in the order of the previous array
    n2_exp = np.array([[1.26, 1.27, 1.27, 1.26, 1.29, 1.28, 1.28, 1.27, 1.27, 1.27],
                       [1.27, 1.23, 1.24, 1.20, 1.23, 1.22, 1.22, 1.22, 1.22, 1.24],
                       [1.18, 1.20, 1.21, 1.19, 1.19, 1.19, 1.18, 1.19, 1.18, 1.20],
                       [1.15, 1.11, 1.16, 1.14, 1.12, 1.14, 1.14, 1.13, 1.16, 1.14],
                       [1.11, 1.11, 1.11, 1.12, 1.11, 1.11, 1.11, 1.10 ,1.105 ,1.11],
                       [1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07],
                       [1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03],
                       [1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02],
                       [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]])
    #Initialize arrays for mean and standard deviation
    n2 = np.zeros(len(T))
    n2_err = np.copy(n2)
    
    #Compute mean value and error of n2
    for i in range(len(T)):
        n2[i] = np.round(np.mean(n2_exp[i]), 2)
        n2_err[i] = np.std(n2_exp[i])
    
    #Initialize M and P to compute them minimizing chi square 
    prec = 0.01
    #Sets of M and P to evaluate
    M = np.arange(0.45, 0.6, prec)
    P = np.arange(9.9, 10.15, prec)
    
    #Initialize resultant M and P 
    M_exp = []
    P_exp = []
    
    #Loop over all columns in n2 (to perform 10 adjustments)
    for k in range(len(n2_exp)):
        # print(n2_exp[:,i])
        #Initialize chi square as a zeros matrix with dimensions dim(M)*dim(P), 
        #being P the vertical axis and M the horizontal one
        chi = np.zeros((len(P), len(M)))
        #Loop over all values of M and P
        for i in range(len(P)):
            for j in range(len(M)):
                #Evaluate chi square for that pair of values over all the 
                #measurements
                chi[i, j] = chi2(n2_exp[:,k], T, M[j], P[i])
        #Get the position of the minimum value of chi square in the matrix
        index = np.where(chi == np.min(chi))
        #Convert it to the values of M and P
        M_exp.append(ufloat(M[index[1]], prec))
        P_exp.append(ufloat(P[index[0]], prec))
    
    #Convert lists to arrays
    M_exp = np.array(M_exp)
    P_exp = np.array(P_exp)
    
    #Do the means
    M_fin = get_mean(M_exp)
    P_fin = get_mean(P_exp)
    
    
    print(M_fin, P_fin)
    #Get curve for the adjustment done
    
    t_fin, n2_res= mom2(M_fin, P_fin, 50)
    
    n2_fin = []
    n2_fin_err = []
    
    for i in n2_res:
        n2_fin.append(nv(i))
        n2_fin_err.append(sd(i))
    n2_fin = np.array(n2_fin)
    n2_fin_err = np.array(n2_fin_err)
    
    #Plot experimental values (after doing the mean)
    plt.errorbar(T, n2, n2_err, fmt='o', color='b', ecolor='g', 
                 label='Experimental data')
    plt.plot(t_fin, n2_fin+n2_fin_err, 'r-', label='Adjustment')
    plt.plot(t_fin, n2_fin-n2_fin_err, 'r-')
    
    
    
    # print(n2_fin)
    # m_final = mom2_arr(T, M_exp, P_exp)
    # print(m_final)
    # plt.plot(T, m_final, 'ro')
    show(r'$T$', r'$n^{(2)}$$')
  
    
exp()

def signal():
    A1 = 3
    A2 = 1
    t = np.arange(0, 10, 0.1)
    P = 6
    I(t, P, A1, A2)
