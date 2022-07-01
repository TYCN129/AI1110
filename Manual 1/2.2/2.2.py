import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

N=10**6
pts=60
U = np.loadtxt("../2.1/gau.dat")
x=np.linspace(-6,6,pts)

F=[]
for i in range(0,pts):
	F.append(np.size(np.nonzero(U < x[i]))/N)

plt.plot(,label="CDF")
plt.xlabel("x")
plt.ylabel("F_X(x)")
plt.legend()
plt.grid()
plt.show()
