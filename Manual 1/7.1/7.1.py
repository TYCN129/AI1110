import matplotlib.pyplot as plt
import numpy as np
import os

ber = np.loadtxt("ber.dat")
gau = np.loadtxt("gau.dat")
uv = np.loadtxt("../1.1/uni.dat")

def p_numerical(g):
        os.system(f"./a.out {g}")
        #rv = np.loadtxt("ral.dat")
        rv = np.sqrt(-g*np.log(1 - uv))
        sig = ber*rv + gau
        a = np.count_nonzero(ber > 0)
        b = np.count_nonzero((sig < 0) & (ber > 0))
        return b/a

def p_theoretical(g):
        return 0.5*(1 - np.sqrt(g/(g + 2)))

P_num = np.vectorize(p_numerical)
P_theo = np.vectorize(p_theoretical)

G = np.linspace(0,10,11)
x = np.linspace(0,10,1000)

plt.plot(x.T,P_theo(x),color="orange",label="Theoretical")
plt.scatter(G,P_num(G),label="Numerical")
plt.grid()
plt.legend()
plt.show()
