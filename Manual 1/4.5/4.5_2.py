import matplotlib.pyplot as plt
import numpy as np

T=np.loadtxt("../4.1/tri.dat")
x=np.linspace(-6,6,100)
N=10**6

def pdf(x):
        if x <= 0:
                return 0
        elif x > 0 and x <= 1:
                return x**2/2
        elif x > 1 and x < 2:
                return 2*x - (x**2/2) - 1
        else:
                return 1

c=[]
F=[]
for i in range(0,100):
        c.append(pdf(x[i]))

for i in range(0,100):
        F.append(np.size(np.nonzero(T <  x[i]))/N)

plt.scatter(x,c,label="Theoritical")
plt.plot(x,F,label="Numerical",color="orange")
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.legend()
plt.show()
