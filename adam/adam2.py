import simplejson as json
import pandas as pd
import numpy as np

jDataString = '''[
{
    "country": "India",
    "capital":"New Delhi",
    "population":"130CR"
},
{
    "country": "Usa",
    "capital":"Wash",
    "population":"50CR"
}]
    
    '''
df = pd.read_excel('sales-funnel.xlsx')
df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(
    ["won", "pending", "presented", "declined"], inplace=True)
df1 = pd.pivot_table(df, index=["Manager", "Rep"], values=[
                     "Price", "Quantity"], aggfunc=np.sum, columns="Product")
# print(df)
# print(df1)
d1 = [
    {
        "accName": "Conveyance",
        "amount": 100,
        "dc": "d",
        "remarks": "shop to office"
    },
    {
        "accName": "Cash A/c",
        "amount": 700,
        "dc": "c",
        "remarks": "shop to office"
    },
    {
        "accName": "Showroom Exp",
        "amount": 500,
        "dc": "d",
        "remarks": "Repairs of items"
    },
    {
        "accName": "Office exp",
        "amount": 100,
        "dc": "d",
        "remarks": "Furniture repairs"
    },
    {
        "accName": "Office exp",
        "amount": 200,
        "dc": "d",
        "remarks": "Mix repairs"
    },
    {
        "accName": "Cash A/c",
        "amount": 200,
        "dc": "c",
        "remarks": "paid"
    }
]
df = pd.DataFrame(d1)
pivot = pd.pivot_table(df,index=["accName"],columns="dc", 
                       values = "amount", aggfunc=np.sum, fill_value=0)
pivot.rename(
  columns={
    'c' : 'Credit',
    'd' : 'Debit'
  },
  inplace=True
)
json = pivot.to_json(orient='table')
print(pivot)
print(json)
