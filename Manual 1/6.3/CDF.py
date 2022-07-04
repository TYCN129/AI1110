import numpy as np
import matplotlib.pyplot as plt

pts=40
N=10**6
A=np.loadtxt("a.dat")
x=np.linspace(-6,6,pts)

F=[]
for i in range(0,pts):
        F.append(np.size(np.nonzero(A < x[i]))/N)

@np.vectorize
def CDF(x):
        if x >= 0:
                return (1 - np.exp(-x**2/2))
        else:
                return 0.0

#vec_cdf=np.vectorize(CDF)

plt.plot(x.T,CDF(x),label="Theoretical",color="orange")
plt.scatter(x.T,F,label="Numerical")
plt.grid()
plt.legend()
plt.show()
