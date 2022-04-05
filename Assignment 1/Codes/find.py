import numpy as np

base_circumference = 132
height = 25

'''using pi = np.pi'''
radius = base_circumference/(2*np.pi)
volume = np.pi*(radius**2)*height

print("Radius and volume of the cylindrical vessel are %d and %d respectively" %(radius,volume))