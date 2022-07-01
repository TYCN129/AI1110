import numpy as np
import matplotlib.pyplot as plt

N=10**6
pts=60
U = np.loadtxt("../1.1/uni.dat")
x=np.linspace(-2,2,pts)

F=[]
for i in range(0,pts):
	F.append(np.size(np.nonzero(U < x[i]))/N)

plt.plot(x,F,label="CDF")
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.legend()
plt.grid()
plt.show()
