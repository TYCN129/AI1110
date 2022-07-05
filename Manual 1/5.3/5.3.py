import matplotlib.pyplot as plt
import numpy as np

N=10**6
Y=np.loadtxt("../5.1/Y.dat",dtype="float")
x=range(N)

plt.scatter(x,Y,alpha=0.5)
plt.grid()
plt.show()
