import simplejson as json
import pandas as pd
import io
import psycopg2
from psycopg2.extras import RealDictCursor, DictCursor
from adam8 import execSql

try:
    connection = None
    with open('adam/config.json') as f:
        cfg = json.load(f)
    connection = psycopg2.connect(
        user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
    # cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor = connection.cursor(cursor_factory=)
    data = execSql(cursor)

    sheets = list(data[0].keys())    
    writer = pd.ExcelWriter(r'c:\gst-all-reports.xlsx', engine='xlsxwriter')

    for sheet in sheets:
        df = pd.DataFrame(data[0].get(sheet))
        print(df)
        df.to_excel(writer, sheet_name=sheet,
                 index=False, header=True)
    writer.save()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    if connection:
        connection.rollback()
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# df=pd.DataFrame(d1)
# df['test']=[1, 'abc', 1, 1, 1, 1, 1]
# df.sum(axis = 0)
# # del df['dc']
# # print(df[0:3])
# # print (df)
# df.to_excel(r'c:\test.xlsx', sheet_name = 'mytest',
#             index = False, header = True)
# output = io.BytesIO()
# writer = pd.ExcelWriter(output, engine='xlsxwriter')
# df.to_excel(writer, index=False, header=True)
# writer.close()
# output.seek(0)
# str = output.read()
# output.close()
# print(str)


# jDataString = '''[
# {
#     "country": "India",
#     "capital":"New Delhi",
#     "population":"130CR"
# },
# {
#     "country": "Usa",
#     "capital":"Wash",
#     "population":"50CR"
# }]'''

# d1 = [
#     {
#         "accName": "Conveyance",
#         "amount": 100,
#         "dc": "D",
#         "remarks": "shop to office"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": 700,
#         "dc": "C",
#         "remarks": "shop to office"
#     },
#     {
#         "accName": "Showroom Exp",
#         "amount": 500,
#         "dc": "D",
#         "remarks": "Repairs of items"
#     },
#     {
#         "accName": "Office exp",
#         "amount": 100,
#         "dc": "C",
#         "remarks": "Furniture repairs"
#     },
#     {
#         "accName": "Office exp",
#         "amount": 200,
#         "dc": "D",
#         "remarks": "Mix repairs"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": 200,
#         "dc": "C",
#         "remarks": "paid"
#     },
#     {
#         "accName": "Cash A/c",
#         "amount": 1200.23,
#         "dc": "D",
#         "remarks": "paid"
#     }
# ]
