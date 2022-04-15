import numpy as np
import pandas as pd

read = pd.read_excel(r'ExcelFiles/raw_data.xlsx')
raw_data = np.array(read)

class_intervals = ["20 - 29","30 - 39","40 - 49","50 - 59","60 - 69","70 - 79","80 - 89","90 - 99"]
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

write = pd.DataFrame({"Class intervals":class_intervals,"Frequency":class_frequency})
write.to_excel('ExcelFiles/frequency_distribution.xlsx',index=False)

print(class_frequency)
