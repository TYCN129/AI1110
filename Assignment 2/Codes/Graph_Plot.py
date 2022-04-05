import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})
x1 = np.linspace(-3,3,1000)
x2 = np.linspace(-3,3,1000)
#lx, ly = [-2,-2], [4,0]
#rx, ry = [1,1], [1,0]
plt.plot(x1,x1**2)
plt.plot(x2,2 - x2)
# plt.plot(lx,ly)
# plt.plot(rx,ry)
plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")
plt.grid()
plt.plot([-2],[4],marker="o",markersize = 10,markerfacecolor = "blue")
plt.plot([1],[1],marker="o",markersize = 10,markerfacecolor = "blue")
plt.text(-2.25,4.35,"(-2,4)")
plt.text(1.25,1.35,"(1,1)")
plt.savefig("../Figures/Graph_Plot.png")