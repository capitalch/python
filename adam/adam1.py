import pandas as pd
import matplotlib.pyplot as plt
import cufflinks as cf
from IPython.display import display,HTML

tup = [1,2,3,4]
for x in tup:
  print(x)

# cf.set_config_file(sharing='public',theme='ggplot',offline=True)
# df_population = pd.read_csv('population_total.csv')
# df_population = df_population.dropna()
# df_population = df_population.pivot(index='year', columns='country',
#                                     values='population')
# df_population = df_population[['United States', 'India', 'China', 
#                                'Indonesia', 'Brazil']]

# df_population.iplot(kind='line',xTitle='Years', yTitle='Population',
#                     title='Population (1955-2020)')

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# df = pd.DataFrame(mydataset)
# json = df.to_json()
# # print(json)
# print(df)
# df = pd.read_csv('data.csv')
# print(df.to_json())
# df.plot()
# plt.show()