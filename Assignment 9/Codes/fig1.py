import matplotlib.pyplot as plt
import numpy as np

plt.grid()
plt.axhline(y = 0, color = "black")
plt.axvline(x = 0, color = "black")
plt.plot([900,1100],[1,1],color="blue")
plt.plot([900,900],[0,1],color="blue")
plt.plot([1100,1100],[0,1],color="blue")

plt.xlabel("$r$")
plt.ylabel("$f_r(r)$")

plt.show()