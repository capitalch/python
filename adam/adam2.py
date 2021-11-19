
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfgen import canvas


c = canvas.Canvas('hello.pdf')  # creates a file hello.pdf
c.translate(10 * mm, 10 * mm)  # moves the origin as x= 10mm, y = 10 mm
width, height = A4
print('Width:', width, ' height:', height)
c.setFont('Helvetica', 14)
# draws line starting from new origin which is 10mm, 10mm
c.line(0, 0, 0, 1.7*inch)
c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=0)  # draw a rectangle
# at point 10,10 draw string. There are drawRightString, drawCenterString
c.drawString(10, 10, 'Hello world')
c.showPage()  # ends the page and resets font, colors etc.
c.save()

invoice = {
    'companyInfo': {
        'name': 'Capital Chowringhee Pvt Ltd',
        'address1': '12 J.L. Nehru road',
        'address2': '',
        'pin': '700013',
        'phone': '9831052332, 8910322267, 9163055161',
        'email': 'capitalch@gmail.com',
        'web': 'www.capital-chowringhee.com',
        'gstin': '19AACCC5685L1Z3',
        'pan': 'AACCC5685L'
    },
    'refNo': 'cardn/1111/21',
    'tranDate': '2121-11-19',
    'billTo': {
        'name': 'Contrary to popular belief, Lorem',
        'address1': 'It has roots in a piece of classical Latin literature from 45 BC, making',
        'address2': 'it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College',
        'pin': '7000065',
        'phone': '9998744565',
        'email': 'gggg.wait@gmail.com',
        'gstin': '19AACCC5685L1M3'
    },
    'shipTo': {
        'name': 'Contrary to popular belief, Lorem',
        'address1': 'looked up one of the more obscure Latin words, consectetur',
        'address2': 'going through the cites of the word in classical literature, discovered',
        'pin': '7000069',
        'phone': '9998743365',
        'email': 'g22wait@gmail.com'
    },
    'items': [
        {
            'code': '1111',
            'item': 'but the majority have suffered alteration in some',
            'slNo': 'yuuyu66677777',
            'hsn': '44454',
            'qty': 1,
            'price': 12000,
            'gstRate':18,
            'cgst': 1000,
            'sgst': 1000,
            'igst': 0,
            'amount': 14000
        },
        {
            'code': '1112',
            'item': 'but the majority have suffered alteration in some',
            'slNo': 'yuuyu66677777',
            'hsn': '44454',
            'qty': 1,
            'price': 12000,
            'gstRate':18,
            'cgst': 1000,
            'sgst': 1000,
            'igst': 0,
            'amount': 14000
        },
        {
            'code': '1113',
            'item': 'obscure Latin words, consectetur, from a Lorem Ipsum passage, and going',
            'slNo': 'uuuu677654',
            'hsn': '44455',
            'qty': 1,
            'price': 10000,
            'gstRate':18,
            'cgst': 800,
            'sgst': 800,
            'igst': 0,
            'amount': 11600
        },
    ],
    'summary':{
        'cgst':2000,
        'sgst':2000,
        'igst':0,
        'total': 22000,
        'inWords': 'Twenty two thousands only'
    },
    'terms':[
        'ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries',
        '1960s with the release of Letraset sheets containing Lorem Ipsum passages'
        'making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney'
    ],
    'transactions':[
        {
            'account':'cash',
            'amount':11000
        },
        {
            'account':'credit card',
            'amount': 11000
        }
    ],
    'dueAmount': 0
}

# import simplejson as json
# import pandas as pd
# import numpy as np

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
# }]

#     '''
# # df = pd.read_excel('sales-funnel.xlsx')
# # df["Status"] = df["Status"].astype("category")
# # df["Status"].cat.set_categories(
# #     ["won", "pending", "presented", "declined"], inplace=True)
# # df1 = pd.pivot_table(df, index=["Manager", "Rep"], values=[
# #                      "Price", "Quantity"], aggfunc=np.sum, columns="Product")
# # print(df)
# # print(df1)
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
#         "amount": -1200.23,
#         "dc": "O",
#         "remarks": "paid"
#     }
# ]
# df = pd.DataFrame(d1)
# pivot = pd.pivot_table(df, index=["accName"], columns="dc",
#                        values="amount", aggfunc=np.sum, fill_value=0).reindex(columns=['O', 'D', 'C'])
# pivot.rename(
#     columns={
#         'D': 'Debit',
#         'C': 'Credit',
#         'O': 'Opening'
#     },
#     inplace=True
# )

# pivot['Closing'] = pivot['Opening'] + pivot['Debit'] - pivot['Credit']


# pivot.loc['total'] = pivot.select_dtypes(pd.np.number).sum() # for summary
# pivot['op_dc'] = pivot['Opening'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
# pivot['clos_dc'] = pivot['Closing'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
# pivot = pivot.reindex(
#     columns=['Opening','op_dc', 'Debit', 'Credit','Closing', 'clos_dc']
# )
# pivot['Opening'] = pivot['Opening'].apply(lambda x: x if x>=0 else -x)
# pivot['Closing'] = pivot['Closing'].apply(lambda x: x if x>=0 else -x)

# json = pivot.to_json(orient='table')
# print(pivot)
# print(json)
