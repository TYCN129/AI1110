import numpy as np
import matplotlib.pyplot as plt

N = 10**6
pts = 100

X = np.loadtxt("../2.1/gau.dat",dtype='double')
x = np.linspace(-6,6,pts)

cdf = []
pdf = []

def gauss_pdf(x):
	return(1/np.sqrt(2*np.pi))*np.exp(-(x**2/2))

for i in range(0,pts):
	cdf.append(np.size(np.nonzero(X < x[i]))/N)

for i in range(0,pts-1):
	pdf.append((cdf[i+1] - cdf[i])/(x[i+1] - x[i]))

plt.plot(x,gauss_pdf(x))
#plt.scatter(x[0:pts-1],pdf,label="Numerical")
plt.grid()
plt.legend()
plt.show()
