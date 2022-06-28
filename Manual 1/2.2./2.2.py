import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

U = np.array(pd.read_csv("../2.1/gau.dat"))
count,bins = np.histogram(U, bins = 10**6)

p = count/sum(count)
cdf = np.cumsum(p)

plt.plot(bins[1:],cdf,label="CDF")
plt.legend()
plt.grid()
plt.show()
