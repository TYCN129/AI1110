#Finding the area between y = x^2 and y = 0

import numpy as np

def func_value(x):
    return x*x

def integral():
    area = 0
    for x in np.arange(-2,1,0.001):
        area += func_value(x)*0.001
    
    return area

print("The area bound by the two curves is {} sq.units" .format(integral()))