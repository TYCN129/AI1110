import numpy as np
import matplotlib.pyplot as plt

pts=50
N=10**6
A=np.loadtxt("a.dat")
x=np.linspace(-6,6,pts)

F=[]
for i in range(0,pts):
        F.append(np.size(np.nonzero(A < x[i]))/N)

p=[]
for i in range(0,pts-1):
        p.append((F[i+1]-F[i])/(x[i+1]-x[i]))

@np.vectorize
def PDF(x):
        if x >= 0:
                return x*np.exp(-x**2/2)
        else:
                return 0.0

#vec_cdf=np.vectorize(CDF)

plt.plot(x.T,PDF(x),label="Theoretical",color="orange")
plt.scatter(x.T[0:pts-1],p,label="Numerical")
plt.grid()
plt.legend()
plt.show()
