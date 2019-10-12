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

import json
with open('config.json') as json_file:
    cfg = json.load(json_file)
print(cfg['trackTest']['schema'])