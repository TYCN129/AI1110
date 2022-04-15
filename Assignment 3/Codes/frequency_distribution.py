import numpy as np

raw_data = np.array([
    [95, 67, 28, 32, 65, 65, 69, 33, 98, 96],
    [76, 42, 32, 38, 42, 40, 40, 69, 95, 92],
    [75, 83, 76, 83, 85, 62, 37, 65, 63, 42],
    [89, 65, 73, 81, 49, 52, 64, 76, 83, 92],
    [93, 68, 52, 79, 81, 83, 59, 82, 75, 82],
    [86, 90, 44, 62, 31, 36, 38, 42, 39, 83],
    [87, 56, 58, 23, 35, 76, 83, 85, 30, 68],
    [69, 83, 86, 43, 45, 39, 83, 75, 66, 83],
    [92, 75, 89, 66, 91, 27, 88, 89, 93, 42],
    [53, 69, 90, 55, 66, 49, 52, 83, 34, 36]
])
class_frequency = np.array([0,0,0,0,0,0,0,0])

def class_index(f):
    if f >= 20 and f < 30:
        return 0
    elif f >= 30 and f < 40:
        return 1
    elif f >= 40 and f < 50:
        return 2
    elif f >= 50 and f < 60:
        return 3
    elif f >= 60 and f < 70:
        return 4
    elif f >= 70 and f < 80:
        return 5
    elif f >= 80 and f < 90:
        return 6
    elif f >= 90 and f < 100:
        return 7

for i in range(10):
    for j in range(10):
        class_frequency[class_index(raw_data[i][j])] += 1;

print(class_frequency)