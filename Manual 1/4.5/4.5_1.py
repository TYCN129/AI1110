import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,6,100)
T=np.loadtxt("../4.1/tri.dat")
N=10**6

def pdf(x):
        if x <= 0:
                return 0.0
        elif x > 0 and x <= 1:
                return x
        elif x > 1 and x < 2:
                return 2 - x
        else:
                return 0.0

vec_gauss=np.vectorize(pdf)

F=[]
pdf=[]
for i in range(0,100):
        F.append(np.size(np.nonzero(T <  x[i]))/N)
for i in range(0,99):
        pdf.append((F[i+1]-F[i])/(x[i+1]-x[i]))

plt.scatter(x[0:99],pdf,label="Theoritical")
plt.plot(x,vec_gauss(x),label="Numerical",color="orange")
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.legend()
plt.show()
