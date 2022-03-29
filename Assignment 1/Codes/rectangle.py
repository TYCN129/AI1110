import matplotlib
from matplotlib import pyplot as plt, patches
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111)
rectangle = matplotlib.patches.Rectangle((0, 0), height = 42, width = 25)
x1, y1 = [12.5,12.5],[21,42]
plt.plot(x1,y1,color = "black")
ax.add_patch(rectangle)
plt.title("Side Profile")
# plt.xlim([-4, 4])
# plt.ylim([-4, 4])
plt.axis('equal')
plt.savefig("../Figures/Side Profile.png")