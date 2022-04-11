import numpy as np

def func_value(x):
    return x*x

def integral():
    area = 0
    for x in np.arange(-2,1,0.001):
        area += func_value(x)*0.001
    
    return area

A_trapezium = ((4 + 1)*3)/2
A_x_2 = integral()
Area = A_trapezium - A_x_2
print("The area bound by the two curves is %.2f sq.units" %(Area))