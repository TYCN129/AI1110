import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50
n = 10**6
U = pd.read_csv("../1.1/uni.dat")

x = np.linspace(-2,2,pts)
F = []

for i in range(0,pts):
        F_n = np.count_nonzero(U < x[i]) #checking probability condition
        F.append(F_n/n) #storing the probability values in a list

F_theory = []
for i in range(0,pts):
        if(x[i]<0):
                F_theory.append(0)
        elif(x[i]>1):
                F_theory.append(1)
        else:
                F_theory.append(x[i])

plt.scatter(x.T, F, color="blue" )#plotting the CDF
plt.plot(x.T, F_theory, color="orange" )#plotting the CDF
plt.grid()
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.show()
