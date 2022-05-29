# import dtale
import dtale
import plotly.express as px
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as p

# Define Data

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot

plt.plot(x, y)

# Display

plt.show()




# df = pd.DataFrame(np.random.rand(10, 4), 
#                   columns=('col_1', 'col_2', 'col_3', 'col_4'))
# df.plot()

# df = sns.load_dataset('planets')
# df = px.data.tips()
# df.head()
# df = pd.DataFrame([1,2,3,4,5])
# dtale.show(df,)
# dtale.show(open_browser=True)
# d = dtale.show(df, ignore_duplicate=True)
# d.open_browser()

print('abcd')

# def encrypt(text,s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if(char == ' '):
#             result += '*'
#         elif (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#     return result
# def encrypt(plain_text, s):
#     encrypted_text = ''
#     for i in range(len(plain_text)):
#         if plain_text[i] == ' ':
#             encrypted_text = encrypted_text + plain_text[i]
#         elif plain_text[i].isupper():
#             encrypted_text = encrypted_text + chr((ord(plain_text[i])+s-65)%26+65)
#         else:
#             encrypted_text = encrypted_text + chr((ord(plain_text[i])+s-97)%26+97)
#     return encrypted_text


# def decrypt(encrypt_text, s):
#     decrypted_text = ''
#     for i in range(len(encrypt_text)):
#         if encrypt_text[i] == ' ':
#             decrypted_text = decrypted_text + encrypt_text[i]
#         elif encrypt_text[i].isupper():
#             decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-s-65)%26+65)
#         else:
#             decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-s-97)%26+97)
#     return decrypted_text

# encoded = encrypt('This is a test string', 13)
# print(encoded)

# id = str(9969)
# encoded = base64.b64encode(id.encode('ascii')).decode('ascii')
# decoded = base64.b64decode(encoded).decode('ascii')
# print(str(decoded))

# id = str(9969)
# encoded = base64.a85encode(id.encode('ascii')).decode('ascii')
# decoded = base64.a85decode(encoded).decode('ascii')
# print(str(decoded))

# id = str(9969)
# encoded = base64.b32encode(id.encode('ascii')).decode('ascii')
# decoded = base64.b32decode(encoded).decode('ascii')
# print(str(decoded))

# json = {
#     'dbName': 'demo_accounts',
#     'buCode': 'demounit1',
#     'id': 9969
# }
# jsonString = djson.encode(json)
# mystr = 'dbName:demo_accounts,buCode:demounit1,id:9969'
# encoded = base64.urlsafe_b64encode(mystr.encode()).decode()
# decoded = base64.urlsafe_b64decode(encoded.encode()).decode()
# encrypted = encrypt(mystr,4)
# decrypted = decrypt(encrypted,4)
# ret = zlib.compress(jsonString.encode('ascii')).decode('ascii')

# print(encoded)
# key = Fernet.generate_key()
# fernet = Fernet(key)
# encMessage = fernet.encrypt(jsonString.encode()).decode()

# encoded = base64.b32encode(jsonString.encode('utf-8')).decode('utf-8')

# print(encMessage)

# data:application/pdf;base64,
# str = '''
# JVBERi0xLjMKJf////8KOCAwIG9iago8PAovVHlwZSAvRXh0R1N0YXRlCi9jYSAxCj4+CmVuZG9iago3IDAgb2JqCjw8Ci9UeXBlIC9QYWdlCi9QYXJlbnQgMSAwIFIKL01lZGlhQm94IFswIDAgNTk1LjI4MDAyOSA4NDEuODkwMDE1XQovQ29udGVudHMgNSAwIFIKL1Jlc291cmNlcyA2IDAgUgo+PgplbmRvYmoKNiAwIG9iago8PAovUHJvY1NldCBbL1BERiAvVGV4dCAvSW1hZ2VCIC9JbWFnZUMgL0ltYWdlSV0KL0V4dEdTdGF0ZSA8PAovR3MxIDggMCBSCj4+Ci9Gb250IDw8Ci9GMSA5IDAgUgo+Pgo+PgplbmRvYmoKMTEgMCBvYmoKKHJlYWN0LXBkZikKZW5kb2JqCjEyIDAgb2JqCihyZWFjdC1wZGYpCmVuZG9iagoxMyAwIG9iagooRDoyMDIyMDEwODE4MjU0MlopCmVuZG9iagoxMCAwIG9iago8PAovUHJvZHVjZXIgMTEgMCBSCi9DcmVhdG9yIDEyIDAgUgovQ3JlYXRpb25EYXRlIDEzIDAgUgo+PgplbmRvYmoKOSAwIG9iago8PAovVHlwZSAvRm9udAovQmFzZUZvbnQgL0hlbHZldGljYQovU3VidHlwZSAvVHlwZTEKL0VuY29kaW5nIC9XaW5BbnNpRW5jb2RpbmcKPj4KZW5kb2JqCjMgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1BhZ2VzIDEgMCBSCi9OYW1lcyAyIDAgUgovVmlld2VyUHJlZmVyZW5jZXMgNCAwIFIKPj4KZW5kb2JqCjEgMCBvYmoKPDwKL1R5cGUgL1BhZ2VzCi9Db3VudCAxCi9LaWRzIFs3IDAgUl0KPj4KZW5kb2JqCjIgMCBvYmoKPDwKL0Rlc3RzIDw8CiAgL05hbWVzIFsKXQo+Pgo+PgplbmRvYmoKNCAwIG9iago8PAovRGlzcGxheURvY1RpdGxlIHRydWUKPj4KZW5kb2JqCjUgMCBvYmoKPDwKL0xlbmd0aCAyODU1Ci9GaWx0ZXIgL0ZsYXRlRGVjb2RlCj4+CnN0cmVhbQp4nO1c2Y4ctxV976/oHxDNfQGEebCTGMhDAEUD5MHwg6amOzYwY0AQkPx+ziXZtZK19Giq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
# '''
# str1 = 'a29kZXJwbGFjZQ=='
# ret = base64.b64decode(str)
# print(ret)
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("helvetica", "B", 16)
# pdf.cell(30, 10, "Hello World!",0,2)
# pdf.cell(30,10,"Next line", ln=1)
# pdf.alias_nb_pages()
# pdf.output("tuto1.pdf")


# class FPDF(FPDF, HTMLMixin):
#     def header(self):
#         # self.set_font('Helvetica', size=20, style='B')
#         # self.cell(0,0, 'This is a header')
#         # print('ok')
#         self.draw_company_info(10, 10, invoice['companyInfo'])
#         self.draw_tax_invoice(160, 10, invoice)
#         self.set_xy(10, 50)

#     def draw_company_info(self, x, y, companyInfo):
#         p = self
#         p.set_font('Helvetica', size=14, style='B')
#         p.set_xy(x, y)
#         p.cell(0, 6, companyInfo['name'], align='L', ln=1)
#         # p.set_font_size(10)
#         p.set_font(style='', size=10)
#         p.multi_cell(
#             140, 5, f"{companyInfo['address1']} {companyInfo['address2']}", ln=1)
#         # p.cell(0, 5, companyInfo['address1'], ln=1)
#         # p.cell(0, 5, companyInfo['address2'], ln=1)
#         p.multi_cell(
#             140, 5, f"**Pin:** {companyInfo['pin']} **Phone:** {companyInfo['phone']} **Email:**{companyInfo['email']} **Web:** {companyInfo['web']} **GSTIN: {companyInfo['gstin']}** PAN: {companyInfo['pan']}", ln=1, align='L', markdown=True)
#         x1 = p.get_x()
#         y1 = p.get_y() + 2
#         x2 = 200
#         y2 = y1
#         p.line(x1, y1, x2, y2)

#     def draw_tax_invoice(self, x, y, info):
#         p = self
#         p.set_font('Helvetica', size=16, style='B')
#         p.set_xy(x, y)
#         p.multi_cell(0, 5, 'Tax invoice', align='L', ln=1)
#         p.set_font(size=10, style='B')
#         p.set_x(x)
#         p.multi_cell(0, 5, f"Inv no: {info['refNo']}", ln=1)
#         p.set_x(x)
#         p.multi_cell(0, 5, f"Date: {info['tranDate']}", ln=1)


# def generate_invoice():
    # def draw_company_info(p, x, y, companyInfo):
    #     p.set_font('Helvetica', size=14, style='B')
    #     p.set_xy(x, y)
    #     p.cell(0, 6, companyInfo['name'], align='L', ln=1)
    #     # p.set_font_size(10)
    #     p.set_font(style='', size=10)
    #     p.multi_cell(
    #         140, 5, f"{companyInfo['address1']} {companyInfo['address2']}", ln=1)
    #     # p.cell(0, 5, companyInfo['address1'], ln=1)
    #     # p.cell(0, 5, companyInfo['address2'], ln=1)
    #     p.multi_cell(
    #         140, 5, f"**Pin:** {companyInfo['pin']} **Phone:** {companyInfo['phone']} **Email:**{companyInfo['email']} **Web:** {companyInfo['web']} **GSTIN: {companyInfo['gstin']}** PAN: {companyInfo['pan']}", ln=1, align='L', markdown=True)
    #     x1 = p.get_x()
    #     y1 = p.get_y() + 2
    #     x2 = 200
    #     y2 = y1
    #     p.line(x1, y1, x2, y2)

    # def draw_tax_invoice(p, x, y, info):
    #     p.set_font('Helvetica', size=16, style='B')
    #     p.set_xy(x, y)
    #     p.multi_cell(0, 5, 'Tax invoice', align='L', ln=1)
    #     p.set_font(size=10, style='B')
    #     p.set_x(x)
    #     p.multi_cell(0, 5, f"Inv no: {info['refNo']}", ln=1)
    #     p.set_x(x)
    #     p.multi_cell(0, 5, f"Date: {info['tranDate']}", ln=1)

#     def draw_items_table(p, x, y, table_header, products, ):
#         # products.insert(0, table_header)
#         p.set_font("Arial", size=9)
#         p.set_xy(x, y)
#         col_width = 20
#         row_height = 6
#         for colName in table_header:
#             p.cell(col_width, row_height, colName)
#         p.ln(8)
#         p.line(p.get_x(), p.get_y(), p.get_x() + 190, p.get_y())
#         p.ln(1)
#         for row in products:
#             for it in row:
#                 p.cell(col_width, row_height, it)
#             p.ln(row_height)

#     def get_long_html():
#         ht = []
#         for i in range(2000):
#             ht.append(
#                 f'''<div style="color:red"><b>This is a test line {i}</b></div><br/>''')
#         return(''.join(ht))

#     companyInfo = invoice['companyInfo']
#     pdf = FPDF(unit='mm')
#     pdf.add_page()
#     pdf.set_margin(10)
#     # draw_company_info(pdf, 10, 10, companyInfo)
#     # draw_tax_invoice(pdf, 160, 10, invoice)
#     table_header = ['#', 'Product', 'Price', 'Qty',
#                     'Gst(%)', 'Cgst', 'Sgst', 'Igst', 'Amount']
#     products = [['1', 'ABCD', '200', '1', '18', '12', '12', '0', '220'],
#                 ['2', 'FBCD', '300', '2', '12', '12', '12', '0', '230']]
#     # draw_items_table(pdf, 10, 45, table_header, products)
#     pdf.write_html(get_long_html())
#     pdf.output('invoice.pdf')


# def generate_receipt(date, amount):
#     pdf = FPDF(orientation='P', unit='pt', format='A4')
#     pdf.add_page()
#     pdf.set_font("Times", "B", 24)
#     pdf.cell(0, 80, "Purchase Receipt", 0, 1, "C")
#     pdf.set_font("Times", "B", 14)
#     pdf.cell(100, 25, "Payment Date:")
#     pdf.set_font("Times", "", 12)
#     pdf.cell(0, 25, "{}".format(date), 0, 1)
#     pdf.cell(0, 5, "", 0, 1)
#     pdf.set_font("Times", "B", 14)
#     pdf.cell(100, 25, "Payment Total:")
#     pdf.set_font("Times", "", 12)
#     pdf.cell(0, 25, "${}".format(amount), 0, 1)
#     return pdf.output('receipt.pdf')


# generate_invoice()
# generate_receipt('22-02-02', 10000)

# import fpdf
# import socketio
# import requests


# def initSocket(socUrl=None, pointId=None, token=None):
#     url = socUrl if socUrl is not None else 'http://localhost:5000'

#     sio = socketio.Client(reconnection=True)

#     @sio.on('connect')
#     def on_connect():
#         print('connected')

#     pid = pointId if pointId is not None else sio.sid
#     sio.connect(url, headers={'pointId': pid},  transports=('websocket'))
#     return(sio)


# def ibukiEmit(socket, message, data):
#     socket.emit('cs-socket-emit', (message, data))


# def ibukiFilterOn(socket, message, f):
#     socket.emit('cs-socket-filter-on', message)

#     @socket.on(message)
#     def on_message(data):
#         f(data)


# def joinRoom(socket, room):
#     socket.emit('cs-join-room', room)


# def onReceiveData(socket, f):
#     @socket.on('sc-send')
#     def on_receive(message, data):
#         f(message, data)


# def onReceiveDataFromPoint(socket, f):
#     @socket.on('sc-send-to-point')
#     def on_sc_send_to_point(message, data, sourcePointId):
#         f(message, data, sourcePointId)


# sio = initSocket(pointId='pythonClient1')


# ibukiEmit(sio, 'PYTHON-MESSAGE1', {'foo': 'ABCD'})
# ibukiFilterOn(sio, 'REACT-APP1-MESSAGE', lambda data: print(data))
# joinRoom(sio, 'room1')
# onReceiveData(sio, lambda message, data:
#               print((message, data)))
# onReceiveDataFromPoint(sio, lambda message, data, sourcePointId:
#                        print((message, data, sourcePointId)))

# sio.wait()

# sio = socketio.Client()
# sio.connect('http://localhost:5000')
# sio.emit('cs-socket-emit', 'REACT-APP-MESSAGE1', {
#     'source': 'Python script'
# })
# sio.emit('cs-socket-emit', data=('REACT-APP-MESSAGE1', {
#     'source': 'Python script'
# }))
# import datetime
# firstTime = datetime.datetime.now()
# print('some time')
# laterTime = datetime.datetime.now()
# difference = laterTime - firstTime
# print(difference.total_seconds()/60)
# arr = [1,2,3,4]
# def calc(a):
#     return(a+1)

# ret = map(calc,arr)
# print(list(ret))

# def num2words(num):
#     under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
#     tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
#     above_100 = {100: 'Hundred',1000:'Thousand', 100000:'Lakhs', 10000000:'Crores'}

#     if num < 20:
#          return under_20[(int)(num)]

#     if num < 100:
#         return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[(int)(num%10)])

#     # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
#     pivot = max([key for key in above_100.keys() if key <= num])

#     return num2words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + num2words(num%pivot))

# num="51222124.12"
# print(num2words(int(num.split(".")[0])))
# print(num2words(int(num.split(".")[1])))

# from datetime import date
# import datetime
# from babel.numbers import format_currency
# from num2words import num2words
# d = 100111212.29
# d1 = format_currency(d,'INR', locale='en_IN')
# print(d1)
# print(num2words(d,'en_IN', to='cardinal'))
# num2words import num2words
# d = 23333322.1
# d1 = f'{d:,.2f}'
# print(d1)
# from copy import copy, deepcopy
# x = datetime.datetime.strptime('2021-04-16','%Y-%m-%d')
# y = x.strftime('%d/%m/%Y')
# dict = {'a': 1}
# cp = deepcopy(dict)

# newDate = myDate.strftime('%d/%m/%Y')
# print(y)

# import pandas as pd
# import io
# from xlsxwriter.workbook import Workbook
# from decimal import *
# from reportlab.pdfgen import canvas
# import os
# c = canvas.Canvas("hello.pdf")
# c.drawString(100,700, 'First time using reportlab')
# c.save()
# os.startfile('hello.pdf')
# items = ['ddd', 'eee', 'fff']
# valueDict = {}
# sql = '''
#         select "id", "hsn", "info", "label"
#         from "ProductM"
#         where "label" ILIKE ANY(array[someArgs])
# '''                                                     # 'ddd', 'eee', 'fff'
# some = ''
# for index, item in enumerate(items):
#         some = some + f" '%%' || '{item}' || '%%' ,"
# # some = some.replace(',','',-1)
# some = some.rstrip(",")
# sql = sql.replace('someArgs', some)
# print(some)
# sql = '''
# select "id", "hsn", "info", "label", "productCode", "upcCode", "gstRate"
# 		    from "ProductM"
#         where "label" ILIKE '%%' || %(arg)s || '%%'
# '''
# temp = ''

# for index, item in enumerate(items):
#         sqlX = sql.replace('arg', f'arg{str(index)}' )
#         # temp = temp +' union ' + sqlX
#         temp = f'{temp} union {sqlX}'
#         valueDict['arg'+str(index)] = item
# temp = temp.replace(' union ','', 1)
# print(temp, valueDict)

# cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#         'Price': [ Decimal('32000'),Decimal('35000'),Decimal('37000'),Decimal('45000')]
#         }

# df = pd.DataFrame(cars, columns = ['Brand', 'Price'])
# df.to_excel ('test.xlsx', index = False, header=True)

# writer = pd.ExcelWriter('demo1.xlsx', engine='xlsxwriter')
# writer.save()

# writer = pd.ExcelWriter(output,  engine='xlsxwriter')
# contents = output.getvalue()
# output.close()


# import simplejson as json
# import demjson as demjson
# import bcrypt
# import re

# regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
# email = 'ss#ss.vo'

# if(re.search(regex,email)):
#     ret = True
# else:
#     ret = False

# print(ret)

# import codecs
# s = codecs.encode('hjj6AZ@745', 'rot13')
# l = codecs.decode(s,'rot13')
# print(s)


# import jwt
# import random
# import string

# def random_string_generator(str_size, allowed_chars):
#     return ''.join(random.choice(allowed_chars) for x in range(str_size))

# chars = string.ascii_letters + string.punctuation + string.digits
# size = 8
# print(chars)

# print(random_string_generator(size, chars))

# val = ''
# valueDict = demjson.decode(val)
# print(valueDict)

# JWT_SECRET = 'secret'
# JWT_ALGORITHM = 'HS256'
# JWT_EXP_DELTA_SECONDS = 20

# payload = {
#     'user_id': 'abcd',
#     'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
# }
# jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

# payload1 = jwt.decode(jwt_token, JWT_SECRET,
#                       algorithms=[JWT_ALGORITHM])

# print(jwt_token)

# import bcrypt
# import base64
# credentials = 'c3NzOiQyYSQxMCR5ZW9aSVdKLzBSUkkwQ3JBclEuYmwuUDMvSWRud1VudExHaEU0eldiQXZjZm4zaWFKcHBsbQ=='
# uidPwd =base64.b64decode(credentials).decode('utf-8')
# uidPwdArr = uidPwd.split(':')
# uid = uidPwdArr[0]
# password = uidPwdArr[1]

# pwd = 's'.encode('utf-8')
# salt = bcrypt.gensalt(rounds=12)
# pwdHash = bcrypt.hashpw(pwd,salt).decode('utf-8')
# b'$2b$12$nAXGJ.Ji5v0vXl5NAScIQuSdbjIPehLGjGGcatY7NHZK4Nnxf0i7a'
# print(pwdHash)
# hashed = '$2b$12$MlC4/PqV2OoD8.Csg2ode.jBjVvi6fkeNO5GF9hdq8yzVxZHmVBJ6'
# if bcrypt.checkpw('superAdmin'.encode('utf-8'), hashed.encode('utf-8')):
#     print("match")
# else:
#     print("does not match")


# logic['N']['Y']()
# tableName = 'TranD'
# sqlObject = {"deletedIds": [1,2]}
# deletedIdList = sqlObject["deletedIds"]
# ret='('
# for x in deletedIdList:
#     ret = ret + str(x) + ','
# ret = ret.rstrip(',')+')'
# tup = tuple(deletedIdList)
# st = str(tup)
# sql =  f''' delete from {tableName} where id in{st}'''
# sql1 = sql
# data = {
#     'tranDate': '2020-12-12',
#     'amount': 2223,
#     'refNo': 'abc',
#     'remarks': 'def',
#     'id': 356
# }
# tableName = 'TranH'

# def getUpdateKeyValues(data):
#     str = ''
#     for it in data:
#         str = str + f''' "{it}" = '{data[it]}', '''
#     str = (str.strip())[:-1]
#     return('set ' + str)

# sql = f''' update "{tableName}"
#     {getUpdateKeyValues(data)}
#     where "id" = {data['id']}
# '''


# myDict = {
#     "debit": 2000,
#     "debits":[
#         {"debit":100},
#         {"debit":200}
#     ]
# }

# print(nested_lookup('debit', myDict))

# def extractAmount(s):
#     amtList = re.findall('\d*\.?\d+', s)
#     return "".join(amtList)


# # creditAmount':'%u20B9 12,000.20
# credits = {"accountName": "", "creditAmount": "%u20B9 1,002.32"}
# remList = [',', '%u20B9', ' ']
# amount = credits["creditAmount"]
# for i in remList:
#     amount = amount.replace(i, '')
# # amt = amount.encode('ascii', 'ignore')
# # amount = extractAmount(credits["creditAmount"])
# print(amount)
# myDict = {
#     "tableName": "cust",
#     "data": {
#         "name": 'sushant',
#         "address": '12 J.l',
#         "details1": {
#             "name": "else"
#         }
#     }
# }
# data = myDict["data"]
# details = None
# if 'details' in data:
#     details = data.pop("details")

# if details:
#     print('details there')
# else:
#     print ('Details not exists')

# print('a')

# print('Hello world')
# myList = ['a','b','c']
# print (myList)

# # if elif
# i= 500
# if i==0:
#     print('i is zero')
# elif i==1:
#     print('i is one')
# else:
#     print('i is' + str(i))

# # iteration in list
# myList = ['a', 'bsdd','cdd']
# for x in myList:
#     print(x,len(x))

# for y in range(5, 15):
#     print(y)

# # functions
# def myFunc(a, L= []):
#     L.append(a)
#     print(L)

# myFunc(100)
# myFunc(200)
# myFunc(300)

# # tuple and dictionary arguments in function
# def tupDict(x, *tup, **dict):
#     print(x)
#     print(tup)
#     print(dict)

# tupDict('Sush', 'a', 'b', 'c', 'd', m= 1, y= 2, z= 3)

# # list
# L = [1,2,3,4]
# L.remove(4)
# print(L)

# # tuple
# tup = (1, 2, 3)
# tup1 = 1, 2, 3
# print(tup)

# # string format
# import math
# print(f'Value of pi is {math.pi:.3f}')

# # json
# import json
# print(json.dumps({'a':1, 'b':2}))

# # os
# import os
# print(os.getcwd())

# # statistics
# import statistics
# L=[1.2,3.4,4.6,4.6]
# print(statistics.mean(L))

# template string
# from string import Template

# t = Template('$name is the $job of $company')
# s = t.substitute(name='Tim Cook', job='CEO', company='Apple Inc.')
# print(s)

# import json
# import simplejson as json
# with open('config.json') as json_file:
#     cfg = json.load(json_file)

# sql = '''
# set search_path to test;
# with RECURSIVE cte
#     as ( select m."id", m."accCode", m."parentId", t."amount" from "AccTran" t
#         join "AccM" m on t."accCode" = m."accCode"
#     union select a.id,a."accCode", a."parentId"
#         , ( cte."amount") as "amount" from "AccM" a join cte on cte."parentId" = a.id )
# select id, "accCode", "parentId", sum(amount) as amount
#     from cte
#         group by id, "accCode", "parentId" order by cte.id
# '''

# import psycopg2
# from psycopg2.extras import RealDictCursor
# try:
#     connection = psycopg2.connect(user=cfg['trackTest']['user'], password=cfg['trackTest']['password'], host=cfg['trackTest']['host'], port=cfg['trackTest']['port'], database=cfg['trackTest']['database'])
#     cursor = connection.cursor(cursor_factory=RealDictCursor)

#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     j = json.dumps(rows, indent=2)
#     list = json.loads(j)
#     print(list)
# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

# sql = "insert into adam1(sample) values('ABC') returning id"
# try:
#     connection = psycopg2.connect(user='webadmin', password='AMGnbm23767', host='node15792-chisel.cloudjiffy.net', port='11035', database='trace')
#     cursor = connection.cursor(cursor_factory=RealDictCursor)
#     cursor.execute(sql)
#     id = cursor.fetchone()
#     connection.commit()

# except (Exception, psycopg2.Error) as error:
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")


# def escapeDoubleQuotes(match):
#     match = match.group()
#     s1 = match[1:-1] # gives the string excluding first and last char
#     s2 = s1.replace('"','\\"') # replace all " with \". Need to give \\ instead of \
#     s3 = match[0]+s2+match[-1] # put back the first and last char in the replaced string
#     return s3
# a = '"I am ae"""klkkl"""" "boy"'
# b = re.sub(r'^("| *")[\s\S]*"[\s\S]*"$', escapeDoubleQuotes, a)
# print(b)

# a = '"name":"Susha"nt", "address":"12 J.l", "phone":12112'


# def escapeDoubleQuotes(match):
#     match = match.group()
#     s1 = match[1:-1]  # gives the string excluding first and last char
#     s2 = s1.replace(
#         '"', '\\"')  # replace all " with \". Need to give \\ instead of \
#     s3 = match[0]+s2 + \
#         match[-1]  # put back the first and last char in the replaced string
#     return s3


# tokens = a.split(',')


# def processToken(token):
#     keyValue = token.split(':')
#     value = keyValue[1]
#     value = re.sub(r'^("| *")[\s\S]*"[\s\S]*"$', escapeDoubleQuotes, value)
#     # ^             :start with
#     # ("| *")       :" or zero or more space followed by a"
#     # [\s\S]*        : Any character including newLine occurs zero or many times. A dot in the place will not work because dot does not include newline
#     # "             : In between there is a "
#     # [\s\S]*        : Zero or more chars
#     # "$            : end is a "
#     keyValue[1] = value
#     token = ':'.join(keyValue)
#     return token


# newTokens = map(processToken, tokens)

# a = ",".join(newTokens)
# print(a)
# dict = {
#     "a": '''1''',
#     "b": '''2'''
# }

# s = json.dumps(dict)
# print(s)
# import re
# n = 'R ₹  123,998.00'
# list = re.findall('\d*\.?\d+',n)
# out = "".join(list)
# print(out)
# m = '''{
#     "a":"ab"c",
#      "b":"cef"
#     }'''
# import ast
# res = json.loads(json.dumps(m))
# print(json.dumps(res))
# phone = "2004-959-559 # This is 1 Phone Number"
# num = re.sub(r'\w', "X", phone)
# print("Phone Num : ", num)
