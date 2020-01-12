import simplejson as json
import psycopg2
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

def execData(data, tableName, fkeyName, fkeyValue, cursor):
    details = None
    if 'details' in data:
        details = data.pop('details')

    sql, tup = getSql(data, tableName, fkeyName, fkeyValue)   
    # execute sql here. You got id, say it is 101
    cursor.execute(sql,tup)
    record = cursor.fetchone()
    id = record[0]
    
    if details:
        if type(details) is list:
            for det in details:
                execSqlObject(det, cursor, id)
        else:
            execSqlObject(details, cursor, id)

def execSqlObject(sqlObject, cursor, fkeyValue=None):
    tableName = sqlObject["tableName"]
    
    fkeyName = None
    if 'fkeyName' in sqlObject:
        fkeyName = sqlObject["fkeyName"]
    data = sqlObject["data"]
    if data:
        if type(data) is list:
            for dt in data:
                execData(dt, tableName, fkeyName, fkeyValue, cursor)
        else:
            execData(data, tableName, fkeyName, fkeyValue, cursor)
    
    # return(sql, tup)

sqlObject = {
    "tableName": "SampleH",
    "data": {
        "refNo": "ref1",
        "remarks": "This remarks1",
        "details": [{
            "tableName": "SampleD",
            "fkeyName": "sampleHeaderId",
            "data": [{
                    "lineRefNo": "Line ref no 1",
                    "lineRemarks": "This is line remarks 1"
            }, {
                    "lineRefNo": "Line ref no 2",
                    "lineRemarks": "This is line remarks 2"
            }]
        }]
    }
}

try:
    with open('config.json') as f:
        cfg = json.load(f)
    connection = psycopg2.connect(user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")
    execSqlObject(sqlObject, cursor)
    # cursor.execute(headerSql,headerValuestuple)
    # record = cursor.fetchone()
    connection.commit()
    print("Data saved")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    connection.rollback()
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


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
