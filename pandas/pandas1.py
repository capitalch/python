import pandas as pd
import numpy as np
s = pd.Series()
#print(s)
data = np.array(['a','b','c','d'])
s = pd.Series(data)
#print(s)
url = "https://community.watsonanalytics.com/wp-content/uploads/2015/04/WA_Fn-UseC_-Sales-Win-Loss.csv"
sales_data = pd.read_csv(url)
print(sales_data)