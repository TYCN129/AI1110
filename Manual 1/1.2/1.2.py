import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

U = np.array(pd.read_csv("../1.1/uni.dat"))
count,bins = np.histogram(U, bins = 10**6)

pdf = count/sum(count)
cdf = np.cumsum(pdf)

plt.plot(bins[1:],cdf,label="CDF")
plt.legend()
plt.grid()
plt.show()
