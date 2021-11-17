from fpdf import FPDF
txt = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32'
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica','', 10)
pdf.multi_cell(0,10,txt)
pdf.output('tut1.pdf')

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
