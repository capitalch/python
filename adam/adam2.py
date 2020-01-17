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
        "dc": "D",
        "remarks": "shop to office"
    },
    {
        "accName": "Cash A/c",
        "amount": 700,
        "dc": "C",
        "remarks": "shop to office"
    },
    {
        "accName": "Showroom Exp",
        "amount": 500,
        "dc": "D",
        "remarks": "Repairs of items"
    },
    {
        "accName": "Office exp",
        "amount": 100,
        "dc": "C",
        "remarks": "Furniture repairs"
    },
    {
        "accName": "Office exp",
        "amount": 200,
        "dc": "D",
        "remarks": "Mix repairs"
    },
    {
        "accName": "Cash A/c",
        "amount": 200,
        "dc": "C",
        "remarks": "paid"
    },
    {
        "accName": "Cash A/c",
        "amount": -1200.23,
        "dc": "O",
        "remarks": "paid"
    }
]
df = pd.DataFrame(d1)
pivot = pd.pivot_table(df, index=["accName"], columns="dc",
                       values="amount", aggfunc=np.sum, fill_value=0).reindex(columns=['O', 'D', 'C'])
pivot.rename(
    columns={
        'D': 'Debit',
        'C': 'Credit',
        'O': 'Opening'
    },
    inplace=True
)

pivot['Closing'] = pivot['Opening'] + pivot['Debit'] - pivot['Credit']



pivot.loc['total'] = pivot.select_dtypes(pd.np.number).sum() # for summary
pivot['op_dc'] = pivot['Opening'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
pivot['clos_dc'] = pivot['Closing'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
pivot = pivot.reindex(
    columns=['Opening','op_dc', 'Debit', 'Credit','Closing', 'clos_dc']
)
pivot['Opening'] = pivot['Opening'].apply(lambda x: x if x>=0 else -x)
pivot['Closing'] = pivot['Closing'].apply(lambda x: x if x>=0 else -x)

json = pivot.to_json(orient='table')
print(pivot)
print(json)
