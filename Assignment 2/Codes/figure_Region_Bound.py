import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})
x1 = np.linspace(-3,3,1000)
y1 = x1**2
y2 = 2 - x1
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")
plt.grid()
plt.plot([-2],[4],marker="o",markersize = 10,markerfacecolor = "blue")
plt.plot([1],[1],marker="o",markersize = 10,markerfacecolor = "blue")
plt.text(-2.25,4.35,"(-2,4)")
plt.text(1.25,1.35,"(1,1)")
plt.fill_between(x1,y1,y2,where = (x1 >= -2) & (x1 <= 1),alpha = 0.5)
plt.savefig("../Figures/Region_Bound.png")
