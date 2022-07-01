import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,6,100)

def pdf(x):
        if x <= 0:
                return 0
        elif x > 0 and x <= 1:
                return x
        elif x > 1 and x < 2:
                return 2 - x
        else:
                return 0

p=[]

for i in range(0,100):
        p.append(pdf(x[i]))

plt.plot(x,p,label="Theoritical")
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.legend()
plt.show()
