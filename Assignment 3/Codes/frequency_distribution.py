import numpy as np
import pandas as pd

read = pd.read_excel(r'ExcelFiles/raw_data.xlsx')
raw_data = np.array(read)

bin = [10*(i + 2) for i in range(9)] 
class_intervals = ["{}-{}".format(bin[i],bin[i+1] - 1) for i in range(8)]

#using inbuilt function for frequencies / class indices
hist = np.histogram(raw_data,bins=bin)
print(hist[0])

write = pd.DataFrame({"Class intervals":class_intervals,"Frequency":hist[0]})
write.to_excel('ExcelFiles/frequency_distribution.xlsx',index=False)
