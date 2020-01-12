import simplejson as json
from itertools import repeat

toInsertSqlAndArgs(tableName, dataDict):
'''converts a dict to sql statement with placeholders %s for arguments. 
Output is sql string along with arguments tuple consumable 
from a psycopg2 sql execute'''
    fieldsList = list(dataDict.keys)
    fieldsString = '"{0}"'.format('", "'.join(fieldsList))
    fieldsCount = len(fieldsList)
    placeHoldersString = ', '.join(list(repeat('%s',fieldsCount))) # get %s, %s
    valuesList= list(dataDict.values())
    valuesTuple = tuple(valuesList)
    sql = f'''insert into public."{tableName}" 
        ({fieldsString}) values(placeHoldersString}) returning id;''' #parameterised sql
    
jInput = '''
{
    "header":{
        "name":"SampleH",
        "value":{
            "refNo":"abc101",
            "remarks":"XYZ 123"
        }
    },
    "details":{
        "name":"SampleD",
        "fkey":"sampleHeaderId",
        "values":[
            {
                "lineRefNo":"DEF 100021",
                "lineRemarks":"DEF 100021"
            },
            {
                "lineRefNo":"DEF 100022",
                "lineRemarks":"MNO 100021"
            }
        ]
    }
}
'''
jObj = json.loads(jInput)
header = jObj["header"]
headerTableName = header["name"]
headerTableDict = header["value"]
headerFieldsList = list(headerTableDataDict.keys())
# headerFields = list(map(lambda x: 'x', headerFieldsList))
headerFields ='"{0}"'.format('", "'.join(headerFieldsList)) # surround fields with ""
headerFieldsCount = len(headerFieldsList)
s = ', '.join(list(repeat('%s',headerFieldsCount))) # get %s, %s

headerValuesList = list(headerTableDataDict.values())
headerValuestuple = tuple(headerValuesList)
headerSql = f'''insert into public."{headerTableName}" 
({headerFields}) values({s}) returning id;''' #parameterised sql

details = jObj["details"]
detailsTableName = details["name"]
detailsTableDataDictList = details["values"]
detailsFieldsList = list(detailsTableDataDictList[0].keys())
# headerFields = list(map(lambda x: 'x', headerFieldsList))
detailsFields ='"{0}"'.format('", "'.join(detailsFieldsList)) # surround fields with ""
detailsFieldsCount = len(detailsFieldsList)
s = ', '.join(list(repeat('%s',detailsFieldsCount))) # get %s, %s

# headerValuesList = list(headerTableDataDict.values())
# headerValuestuple = tuple(headerValuesList)
# headerSql = f'''insert into public."{headerTableName}" 
# ({headerFields}) values({s}) returning id;''' #parameterised sql
