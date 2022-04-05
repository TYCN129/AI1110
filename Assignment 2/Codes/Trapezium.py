import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})
plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")
x1 = np.linspace(-3,3,1000)
y1 = x1**2
y2 = 2 - x1
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.plot([-2],[4],marker="o",markersize = 10,markerfacecolor = "blue")
plt.plot([1],[1],marker="o",markersize = 10,markerfacecolor = "blue")
plt.grid()
plt.text(-2.2,0,"A")
plt.text(-2.2,4,"B")
plt.text(1.1,1,"C")
plt.text(1.1,0,"D")
plt.xlim(-3,3)
plt.ylim(-2,10)
plt.fill([-2,-2,1,1],[0,4,1,0],alpha = 0.5)
plt.savefig("../Figures/Trapezium.png")