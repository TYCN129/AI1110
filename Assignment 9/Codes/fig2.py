import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1/1100,1/900,step=0.000001)
y = 1/(200*(x**2))
plt.axhline(y = 0, color = "black")
plt.axvline(x = 0, color = "black")

plt.plot(x,y,color = "blue")
plt.plot([0.0012,0.00105],[6000,5000],color = "black")
plt.plot([1/1100,1/1100],[0,1/(200*((1/1100)**2))], color="blue")
plt.plot([1/900,1/900],[0,1/(200*((1/900)**2))], color="blue")
plt.xlabel("$g$")
plt.ylabel("$f_g(g)$")
plt.text(0.00121,6000,"1/(200g^2)")
#plt.arrow(0.0013,6000,-0.0001,-800,head_width=0.0002,width=0.0001)
plt.xlim(0,0.0016)
plt.ylim(0,7000)
plt.grid()
plt.show()