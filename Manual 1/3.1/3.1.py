import matplotlib.pyplot as plt
import numpy as np

V = np.loadtxt("v.dat")

N=10**6
pts=60
x = np.linspace(-6,10,pts)

F=[]
for i in range(0,pts):
        F.append(np.size(np.nonzero(V < x[i]))/N)

plt.plot(x,F,label="CDF")
plt.grid()
plt.xlabel("x")
plt.ylabel("F_V(x)")
plt.legend()
plt.show()
