# Photon-Counting
The file to use is main.py, which has three output functions. The rest of the files are auxiliary functions used in this main archives.

The functions in main are:
signal() -> draws a square signal, not actually used, just to show the shape
main() -> draws W and the model. Again, this is just to show the behaviour, it is not used in the experimental part
exp() -> experiental part. Given the measurements of T and n(2) it does the adjustment and plots the comparison graph. To change the parameters, the variables are T and
        n2_exp, which are the direct measurements: prec, which is the precission wanted in the sweep minimizing chi square, and the limits M and P, which are considered 
        for the experiment particular signal

