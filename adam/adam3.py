from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import Spacer

def coord(x, y, unit=1):
    x, y = x*unit, y*unit
    return x, y

def draw_text_objects(c):
    textObj1 = c.beginText(*coord(10,10,mm))
    textObj1.textLine('Welcome1')

    textObj2 = c.beginText(*coord(10,20, mm))
    textObj2.textLine("Welcome2")

    textObj3 = c.beginText(*coord(100,10, mm))
    textObj3.textLine("Welcome3")
    c.drawText(textObj1)
    c.drawText(textObj2)
    c.drawText(textObj3)

def draw_template():
    story = [Spacer()]

c = canvas.Canvas('invoice1.pdf', bottomup=0)
draw_text_objects(c)
# c.drawString(*coord(10, 10, mm), 'Welcome to pdf canvas')



c.showPage()
c.save()


# import simplejson as json
# import psycopg2
# from itertools import repeat


# def getSql(data, tableName, fkeyName, fkeyValue):
#     fieldsList = list(data.keys())
#     if fkeyName and fkeyValue:
#         fieldsList.append(fkeyName)

#     fieldsCount = len(fieldsList)
#     fieldsString = '"{0}"'.format('", "'.join(
#         fieldsList))  # surround fields with ""
#     placeholdersForValues = ', '.join(list(repeat('%s', fieldsCount)))

#     valuesList = list(data.values())
#     if fkeyName and fkeyValue:
#         valuesList.append(fkeyValue)
#     valuesTuple = tuple(valuesList)
#     sql = f'''insert into public."{tableName}"
#     ({fieldsString}) values({placeholdersForValues}) returning id
#     '''
#     return(sql, valuesTuple)


# def processData(data, tableName, fkeyName, fkeyValue, cursor):
#     details = None
#     if 'details' in data:
#         # removes details from data, to create sql out of that
#         details = data.pop('details')

#     sql, tup = getSql(data, tableName, fkeyName, fkeyValue)
#     # execute sql here. You got id, say it is 101
#     cursor.execute(sql, tup)
#     record = cursor.fetchone()
#     id = record[0]

#     if details:
#         if type(details) is list:
#             for det in details:
#                 execSqlObject(det, cursor, id)
#         else:
#             execSqlObject(details, cursor, id)


# def execSqlObject(sqlObject, cursor, fkeyValue=None):
#     tableName = sqlObject["tableName"]
#     fkeyName = None
#     if 'fkeyName' in sqlObject:
#         fkeyName = sqlObject["fkeyName"]
#     data = sqlObject["data"]
#     if data:
#         if type(data) is list:
#             for dt in data:
#                 processData(dt, tableName, fkeyName, fkeyValue, cursor)
#         else:
#             processData(data, tableName, fkeyName, fkeyValue, cursor)

# return(sql, tup)


# sqlObject = {
#     "tableName": "SampleH",
#     "data": {
#         "refNo": "ref1",
#         "remarks": "This remarks1",
#         "details": [{
#             "tableName": "SampleD",
#             "fkeyName": "sampleHeaderId",
#             "data": [
#                 {
#                     "lineRefNo": "Line ref no 1",
#                     "lineRemarks": "This is line remarks 1",
#                     "details": {
#                         "tableName": "SampleDExt",
#                         "fkeyName": "sampleDetailsId",
#                         "data": {
#                             "instrNo": "ch-44434556"
#                         }
#                     }
#                 },
#                 {
#                     "lineRefNo": "Line ref no 2",
#                     "lineRemarks": "This is line remarks 2",
#                     "details": {
#                         "tableName": "SampleDExt",
#                         "fkeyName": "sampleDetailsId",
#                         "data": {
#                             "instrNo": "ch-7778554"
#                         }
#                     }
#                 }]
#         }]
#     }
# }

# try:
#     connection = None
#     with open('config.json') as f:
#         cfg = json.load(f)
#     connection = psycopg2.connect(
#         user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
#     cursor = connection.cursor()
#     execSqlObject(sqlObject, cursor)
#     connection.commit()
#     print("Data saved")
# except (Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL", error)
#     if connection:
#         connection.rollback()
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")


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
