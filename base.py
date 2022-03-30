import matplotlib
from matplotlib import pyplot as plt, patches
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111)
circle = matplotlib.patches.Circle((0, 0), radius=21, linewidth=3)
x1, y1 = [0,21],[0,0]
plt.plot(x1,y1,color = "black")
ax.add_patch(circle)
plt.text(-5,2.5, "Radius = 21cm")
plt.title("Base")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axis('equal')
plt.savefig("Base.png")
plt.show()