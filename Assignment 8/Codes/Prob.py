import numpy as np
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


th_total = 3**10
th_fav = ncr(10,3)*2**7

th_prob = th_fav/th_total

array = []

sim_total = 0
sim_fav = 0

for i in range(0,100000):
    tuple = [np.random.randint(0,10),np.random.randint(0,10),np.random.randint(0,10)]
    if tuple[0] + tuple[1] + tuple[2] == 10:
        sim_total += 1
        array.append(tuple)

for tuple in array:
    if tuple[0] == 3:
        sim_fav += 1

sim_prob = sim_fav/sim_total

print("The theoritical probabiltiy is {}" .format(th_prob))
print("The simulated probabiltiy is {}" .format(sim_prob))
