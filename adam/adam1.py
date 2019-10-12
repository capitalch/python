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
import simplejson as json
with open('config.json') as json_file:
    cfg = json.load(json_file)

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

import psycopg2
from psycopg2.extras import RealDictCursor
try:
    connection = psycopg2.connect(user=cfg['trackTest']['user'], password=cfg['trackTest']['password'], host=cfg['trackTest']['host'], port=cfg['trackTest']['port'], database=cfg['trackTest']['database'])
    cursor = connection.cursor(cursor_factory=RealDictCursor)
   
    cursor.execute(sql)
    rows = cursor.fetchall()
    j = json.dumps(rows, indent=2)
    list = json.loads(j)
    print(list)
    # print(json.dumps(rows, indent=2))
    # print(rows)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")