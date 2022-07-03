import numpy as np

X=np.loadtxt("../5.1/X.dat")
X_cap=np.loadtxt("../5.3/X_cap.dat")
N=10**6

#a=np.size(np.nonzero(X == 1 and X_cap == -1))
a=0
b=np.size(np.nonzero(X == 1))

for i in range(0,N):
	if X[i] == 1:
		if X_cap[i] == -1:
			a=a+1

P0 = a/b
print("P0 is equal to {}" .format(P0))
