import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})
plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")
x1 = np.linspace(-3,3,1000)
y1 = x1**2
y2 = 2 - x1
plt.plot(x1,y1,label = "$y = x^2$")
plt.plot(x1,y2,label = "$y = 2 - x$")
plt.plot([-2],[4],marker="o",markersize = 10,markerfacecolor = "blue")
plt.plot([1],[1],marker="o",markersize = 10,markerfacecolor = "blue")
plt.text(-2.1,4.25,"(-2,4)")
plt.text(1.1,1,"(1,1)")
plt.xlim(-5,5)
plt.ylim(-2,10)
plt.fill_between(x1,y1,y2,where = (x1 >= -2) & (x1 <= 1),color = 'blue',alpha = 0.6)
plt.legend(loc = 1)
plt.savefig("../Figures/Shaded.png")