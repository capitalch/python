import simplejson as json
# from nested_lookup import nested_lookup
import re
from dateutil.parser import parse

dt = parse('2020-02-14T00:00:00.000Z').date()
print(dt)

myDict = {
    "debit": 2000,
    "debits":[
        {"debit":100},
        {"debit":200}
    ]
}

# print(nested_lookup('debit', myDict))

def extractAmount(s):
    amtList = re.findall('\d*\.?\d+',s)
    return "".join(amtList)  
# creditAmount':'%u20B9 12,000.20
credits = {"accountName": "", "creditAmount": "%u20B9 1,002.32"}
remList = [',','%u20B9', ' ']
amount = credits["creditAmount"]
for i in remList:
    amount = amount.replace(i,'')
# amt = amount.encode('ascii', 'ignore')
# amount = extractAmount(credits["creditAmount"])
print(amount)
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

sql = '''
set search_path to test; 
with RECURSIVE cte 
    as ( select m."id", m."accCode", m."parentId", t."amount" from "AccTran" t 
        join "AccM" m on t."accCode" = m."accCode" 
    union select a.id,a."accCode", a."parentId"
        , ( cte."amount") as "amount" from "AccM" a join cte on cte."parentId" = a.id ) 
select id, "accCode", "parentId", sum(amount) as amount
    from cte 
        group by id, "accCode", "parentId" order by cte.id
'''

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

a = '"name":"Susha"nt", "address":"12 J.l", "phone":12112'
def escapeDoubleQuotes(match):
    match = match.group()
    s1 = match[1:-1] # gives the string excluding first and last char
    s2 = s1.replace('"','\\"') # replace all " with \". Need to give \\ instead of \
    s3 = match[0]+s2+match[-1] # put back the first and last char in the replaced string
    return s3
tokens = a.split(',')

def processToken(token):
    keyValue = token.split(':')
    value = keyValue[1]
    value = re.sub(r'^("| *")[\s\S]*"[\s\S]*"$', escapeDoubleQuotes, value)
    # ^             :start with
    # ("| *")       :" or zero or more space followed by a"
    # [\s\S]*        : Any character including newLine occurs zero or many times. A dot in the place will not work because dot does not include newline
    # "             : In between there is a "
    # [\s\S]*        : Zero or more chars
    # "$            : end is a "
    keyValue[1] = value
    token = ':'.join(keyValue)
    return token

newTokens = map(processToken, tokens)

a = ",".join(newTokens)
print(a)
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
m = '''{
    "a":"ab"c",
     "b":"cef" 
    }'''
# import ast
# res = json.loads(json.dumps(m))
# print(json.dumps(res))
import re
phone = "2004-959-559 # This is 1 Phone Number"
num = re.sub(r'\w', "X", phone)
print("Phone Num : ", num)
