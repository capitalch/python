import simplejson as json

jInput = '''
{
    "parent":{
        "name":"TranM",
        "value":{
            "date":"2019-01-01",
            "refNo":"abc101",
            "jData":""
        }
    },
    "child":{
        "name":"TranD",
        "fkey":"tranId",
        "values":[
            {
                "accId":"1",
                "amount":2000.00,
                "tranType": "d",
                "jData":""
            },
            {
                "accId":"2",
                "amount":2025.00,
                "tranType": "d",
                "jData":""
            }
        ]
    }
}
'''
jObj = json.loads(jInput)
parent = jObj['parent']
parentTable = parent['name']; parentDict = parent['value']

parentFieldsList = list(parentDict.keys())
parentValuesList = list(parentDict.values())
parentFields = '"{0}"'.format('", "'.join(parentFieldsList))
parentValues =  "'{0}'".format("', '".join(parentValuesList))
parentSql = f'''
insert into {parentTable}({parentFields}) values({parentValues}) returning id
'''

child = jObj['child']
childTable = child['name']; childDict = child['values']
fkeyName = child['fkey']; fkeyValue = 1
childList = child['values']
firstChildDict = childList[0] # get field names
childFieldsList = list(firstChildDict.keys())
childFields = '"{0}"'.format('", "'.join(childFieldsList)) + f', "{fkeyName}"' # add foreign key at last

items = []
for itemDict in childList:
    itemValuesList = list(itemDict.values())
    itemValues = "'{0}'".format("', '".join(str(x) for x in itemValuesList)) + f", '{fkeyValue}'" # add foreign key at last
    items.append(itemValues)

childValues = ""
for item in items:
    childValues = childValues + f'({item}),'
childValues = childValues[:-1]

childSql = f'''
insert into {childTable}({childFields}) values {childValues}
'''
print (childSql)
