import numpy as np
import matplotlib.pyplot as plt

V=np.loadtxt("v.dat")
pts=50
x=np.linspace(-5,13,pts)

N=10**6
F=[]

for i in range(0,pts):
        F.append(np.size(np.nonzero(V < x[i]))/N)

p=[]
for i in range(0,pts-1):
        p.append((F[i+1]-F[i])/(x[i+1]-x[i]))

def PDF(x):
        if x >= 0:
                return (np.exp(-x/2))/2
        else:
                return 0.0

vec_pdf=np.vectorize(PDF)

plt.scatter(x.T[0:pts-1],p,label="Numerical")
plt.plot(x.T,vec_pdf(x),label="Theoretical",color="orange")
plt.grid()
plt.legend()
plt.show()
