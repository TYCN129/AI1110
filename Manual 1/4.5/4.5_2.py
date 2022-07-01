import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,6,100)

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

for i in range(0,100):
        c.append(pdf(x[i]))

plt.plot(x,c,label="Theoritical")
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.legend()
plt.show()
