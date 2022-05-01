import numpy as np
from numpy import random as RN 

# total number of people
N = 10
# total number of men
n_0 = 4
# total number of women
n_1 = 6

# So , The Theoretical probabilities
pr_0 = n_0/N
pr_1 = n_1/N


# Let x take any value from 1 to 100 inclusive over the size N ,
x = RN.randint(0, 10, size = N)
# if x <= 4, then we shall take the Selected council member to be a man
# and if x >  4, then we shall take the Selected council member to be a woman

#Finding the number of integers which are greater than 4.
x_0 = np.count_nonzero(x > 4)

#So ,number of integers such that x <= 14 are
x_1 = N - x_0

print("Theoretical Probabilities:", pr_0, pr_1)
print("Practical Probabilities:", x_0/N, x_1/N)
