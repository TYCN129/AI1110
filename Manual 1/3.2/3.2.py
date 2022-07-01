import matplotlib.pyplot as plt
import numpy as np

V = np.loadtxt("v.dat")
U = np.loadtxt("../1.1/uni.dat")

N=10**6
pts=30
x = np.linspace(-2,10,pts)

F_sim=[]
for i in range(0,pts):
        F_sim.append(np.size(np.nonzero(V < x[i]))/N)

F_theory=[]
for i in range(0,pts):
        if x[i] <= 0:
                F_theory.append(0)
        else:
                F_theory.append(1 - np.exp(-x[i]/2))

plt.plot(x[0:],F_sim,'o',label="Empirical",color="blue")
plt.plot(x[0:],F_theory,label="Theoritical",color="orange")
plt.grid()
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.legend()
plt.show()
