import numpy as np
import pandas as pd

read = pd.read_excel(r'ExcelFiles/raw_data.xlsx')
raw_data = np.array(read)

#automatically generating bins and class intervals
bin = [10*(i + 2) for i in range(9)] 
class_intervals = ["{}-{}".format(bin[i],bin[i+1] - 1) for i in range(8)]

#using inbuilt function for frequencies / class indices
hist = np.histogram(raw_data,bins=bin)

#using inbuilt function for tracking frequency count
cumulative = np.cumsum(hist[0])

school_count = cumulative[7] - cumulative[2]
print("Total number of schools with greater than 50 plants left is {}" .format(school_count))

write = pd.DataFrame({"Class intervals":class_intervals,"Frequency":hist[0]})
write.to_excel('ExcelFiles/frequency_distribution.xlsx',index=False)
