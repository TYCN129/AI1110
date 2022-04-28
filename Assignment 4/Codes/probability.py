import numpy as np
from numpy import random as RN 

# total number of pens in the lot
N = 144
# total number of good pens
n_0 = 124
# total number of defective pens
n_1 = 20

# So , The Theoretical probabilities
pr_0 = n_0/N
pr_1 = n_1/N


# Let x take any value from 1 to 100 inclusive over the size N ,
x = RN.randint(1, 101, size = N)
# if x <= 14, then we shall take the pen drawn to be defective
# and if x >= 15, then we shall take the pen drawn to be good

#Finding the number of integers which are greater than or equal to 15.
x_0 = np.count_nonzero(x > 14)

#So ,number of integers such that x <= 14 are
x_1 = N - x_0

print("Theoretical Probabilities:", pr_0, pr_1)
print("Practical Probabilities:", x_0/N, x_1/N)