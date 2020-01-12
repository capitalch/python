import simplejson as json
from itertools import repeat

def getSql(data, tableName, fkeyName, fkeyValue):
    fieldsList = list(data.keys())
    if fkeyName and fkeyValue:
        fieldsList.append(fkeyName)
        
    fieldsCount = len(fieldsList)
    fieldsString = '"{0}"'.format('", "'.join(
        fieldsList))  # surround fields with ""
    placeholdersForValues = ', '.join(list(repeat('%s', fieldsCount)))

    valuesList = list(data.values())
    if fkeyName and fkeyValue:
        valuesList.append(fkeyValue)
    valuesTuple = tuple(valuesList)
    sql = f'''insert into public."{tableName}"
    ({fieldsString}) values({placeholdersForValues}) returning id
    '''
    return(sql, valuesTuple)

def execData(data, tableName, fkeyName, fkeyValue):
    details = None
    if 'details' in data:
        details = data.pop('details')

    sql, tup = getSql(data, tableName, fkeyName, fkeyValue)   
    # execute sql here. You got id, say it is 101
    id = 101
    
    if details:
        if type(details) is list:
            for det in details:
                execSqlObject(det, id)
        else:
            execSqlObject(details, id)

def execSqlObject(sqlObject, fkeyValue=None):
    tableName = sqlObject["tableName"]
    
    fkeyName = None
    if 'fkeyName' in sqlObject:
        fkeyName = sqlObject["fkeyName"]
    data = sqlObject["data"]
    if data:
        if type(data) is list:
            for dt in data:
                execData(dt, tableName, fkeyName, fkeyValue)
        else:
            execData(data, tableName, fkeyName, fkeyValue)
    
    # return(sql, tup)

sqlObject = {
    "tableName": "cust",
    "data": {
        "custName": "abc",
        "custPhone": "22234",
        "details": [{
            "tableName": "addresses",
            "fkeyName": "custId",
            "data": [{
                    "address1": "12 J.L",
                    "pin": "111234"
            }]
        }]
    }
}

execSqlObject(sqlObject)
# print(sql)


# {
# 	"tableName":"cust",
# 	"fkeyName": "",
# 	"data": {
# 		"custName": "abc",
# 		"custPhone":"22234",
# 		"details": [{
# 			tableName: "addresses",
# 			fkeyName: "",
# 			data: [{
# 				address1: "12 J.L"
# 				pin: "111234"
# 			}]
# 		}]
# 	}
	
# }
