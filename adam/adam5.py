
import pandas as pd
import numpy as np

list = [1,2,3,4,5]
df = pd.DataFrame(list)
df.rename()
js = df.to_json(orient='table')
print(df)
print(js)
