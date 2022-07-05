import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import os

A=np.linspace(0.1,1.0,10)
x=np.linspace(0,3,50)

def P_e(val):
        X=np.loadtxt("../5.1/X.dat")
        X_cap=np.loadtxt("x_cap.dat")
        a=np.count_nonzero((X_cap == val) * (X == -val))
        b=np.count_nonzero(X == -val)

        return a/b

def plot_numerical(x):
        os.system("./run "+str(x))
        a=P_e(-1)
        b=P_e(1)

        return (a+b)/2

def Q(x):
        return mp.erfc(x/np.sqrt(2))/2

vec_numerical=np.vectorize(plot_numerical)
vec_theoretical=np.vectorize(Q)

plt.scatter(A,vec_numerical(A),label="Numerical")
plt.plot(x,vec_theoretical(x),label="Theoretical",color="orange")
plt.grid()
plt.legend()
plt.show()
