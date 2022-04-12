#Vedant Bhandare - cs21btech11007
#ICSE 12 2019 Q18

#On substituting the line vector in parabola vector equation, we get the
#quadratic equation in lambda as lambda^2 + 3*lambda = 0

import numpy as np

pols = [1,3,0] #quadratic
roots = np.roots(pols)

point_1 = np.array([1,1]) + roots[0]*np.array([1,-1])
point_2 = np.array([1,1]) + roots[1]*np.array([1,-1])

print("The two points of intersection are ({},{}) and ({},{})" .format(point_1[0],point_1[1],point_2[0],point_2[1]))