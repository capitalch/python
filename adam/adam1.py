from fpdf import FPDF, HTMLMixin
from datetime import datetime, date
from invoice import invoice

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("helvetica", "B", 16)
# pdf.cell(30, 10, "Hello World!",0,2)
# pdf.cell(30,10,"Next line", ln=1)
# pdf.alias_nb_pages()
# pdf.output("tuto1.pdf")

class FPDF(FPDF, HTMLMixin):
    pass

def generate_invoice():
    def draw_company_info(p, x, y, companyInfo):
        p.set_font('Helvetica', size=14, style='B')
        p.set_xy(x, y)
        p.cell(0, 6, companyInfo['name'], align='L', ln=1)
        # p.set_font_size(10)
        p.set_font(style='', size=10)
        p.multi_cell(
            140, 5, f"{companyInfo['address1']} {companyInfo['address2']}", ln=1)
        # p.cell(0, 5, companyInfo['address1'], ln=1)
        # p.cell(0, 5, companyInfo['address2'], ln=1)
        p.multi_cell(
            140, 5, f"**Pin:** {companyInfo['pin']} **Phone:** {companyInfo['phone']} **Email:**{companyInfo['email']} **Web:** {companyInfo['web']} **GSTIN: {companyInfo['gstin']}** PAN: {companyInfo['pan']}", ln=1, align='L', markdown=True)
        x1 = p.get_x()
        y1 = p.get_y() + 2
        x2 = 200
        y2 = y1
        p.line(x1, y1, x2, y2)

    def draw_tax_invoice(p, x, y, info):
        p.set_font('Helvetica', size=16, style='B')
        p.set_xy(x, y)
        p.multi_cell(0, 5, 'Tax invoice', align='L', ln=1)
        p.set_font(size=10, style='B')
        p.set_x(x)
        p.multi_cell(0, 5, f"Inv no: {info['refNo']}", ln=1)
        p.set_x(x)
        p.multi_cell(0, 5, f"Date: {info['tranDate']}", ln=1)

    def draw_items_table(p, x, y, table_header, products, ):
        # products.insert(0, table_header)
        p.set_font("Arial", size=9)
        p.set_xy(x, y)
        col_width = 20
        row_height = 6
        for colName in table_header:
            p.cell(col_width,row_height,colName)
        p.ln(8)
        p.line(p.get_x(), p.get_y(), p.get_x() + 190, p.get_y())
        p.ln(1)
        for row in products:
            for it in row:
                p.cell(col_width, row_height, it)
            p.ln(row_height)

    companyInfo = invoice['companyInfo']
    pdf = FPDF(unit='mm')
    pdf.add_page()
    pdf.set_margin(10)
    draw_company_info(pdf, 10, 10, companyInfo)
    draw_tax_invoice(pdf, 160, 10, invoice)
    table_header = ['#', 'Product', 'Price', 'Qty',
                    'Gst(%)', 'Cgst', 'Sgst', 'Igst', 'Amount']
    products = [['1', 'ABCD', '200', '1', '18', '12', '12', '0', '220'],
                ['2', 'FBCD', '300', '2', '12', '12', '12', '0', '230']]
    draw_items_table(pdf, 10, 45, table_header, products)
    pdf.write_html('<b>Some html</b>')
    pdf.output('invoice.pdf')


def generate_receipt(date, amount):
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.cell(0, 80, "Purchase Receipt", 0, 1, "C")
    pdf.set_font("Times", "B", 14)
    pdf.cell(100, 25, "Payment Date:")
    pdf.set_font("Times", "", 12)
    pdf.cell(0, 25, "{}".format(date), 0, 1)
    pdf.cell(0, 5, "", 0, 1)
    pdf.set_font("Times", "B", 14)
    pdf.cell(100, 25, "Payment Total:")
    pdf.set_font("Times", "", 12)
    pdf.cell(0, 25, "${}".format(amount), 0, 1)
    return pdf.output('receipt.pdf')


generate_invoice()
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
