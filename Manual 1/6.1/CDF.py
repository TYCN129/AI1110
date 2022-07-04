import numpy as np
import matplotlib.pyplot as plt

V=np.loadtxt("v.dat")
pts=40
x=np.linspace(-5,13,pts)

N=10**6
F=[]

def CDF(x):
        if x >= 0:
                return (1 - np.exp(-x/2))
        else:
                return 0.0

for i in range(0,pts):
        F.append(np.size(np.nonzero(V < x[i]))/N)

vec_cdf=np.vectorize(CDF)
plt.scatter(x.T,F,label="Numerical")
plt.plot(x.T,vec_cdf(x),label="Theoretical",color="orange")
plt.grid()
plt.legend()
plt.show()
