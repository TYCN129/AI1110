import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 60

n = 10**6
X = np.loadtxt("../2.1/gau.dat")

x = np.linspace(-6,6,pts)
F = [] 
for i in range(0,pts):
	Fcount = np.size(np.nonzero(X < x[i]))
	F.append(Fcount/n) 

p = []
for i in range(0,pts-1):
	p.append( (F[i+1] - F[i])/ (x[i+1]-x[i]))
	
plt.plot(x.T[0:(pts-1)], p, color="blue" )
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_X(x)$")
plt.title("Emperical PDF of X")
plt.show()
