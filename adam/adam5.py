import simplejson as json
import pandas as pd
import numpy as np
import psycopg2
from itertools import repeat
from psycopg2.extras import RealDictCursor, DictCursor

sql1 = ''' set search_path to demounit1; select "id", "accCode", "accName" from "AccM" where "accLeaf" = 'Y' '''
sql2 = ''' set search_path to demounit1; select "id", "accId", "amount" from "TranD" '''
sqlList = [sql1, sql2]
sqlTuple = [('sql1', sql1), ('sql2', sql2)]
sql3 = '''
    set search_path to demounit1;
    select "id", "tranDate", "autoRefNo", "finYearId" from "TranH" where "tranDate" between %(startDate)s and %(endDate)s
'''
try:
    connection = None
    with open('config.json') as f:
        cfg = json.load(f)
    connection = psycopg2.connect(
        user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])

    cursor = connection.cursor()
    params = [
        {'name': 'today', 'startDate': '2022-05-29',
            'endDate': '2022-05-29', 'tranTypeId': 4},
        {'name': 'yesterday', 'startDate': '2022-05-28',
            'endDate': '2022-05-28', 'tranTypeId': 4},
        {'name': 'thisMonth', 'startDate': '2022-05-01',
            'endDate': '2022-05-30', 'tranTypeId': 4},
        {'name': 'lastMonth', 'startDate': '2022-04-01',
            'endDate': '2022-04-30', 'tranTypeId': 4},
        {'name': 'ytd', 'startDate': '2022-04-01',
            'endDate': '2022-05-30', 'tranTypeId': 4},
    ]
    out = {}
    for param in params:
        cursor.execute(sql3, param)
        out[param['name']] = cursor.fetchall()
    
    print(out)
    # x = cursor.mogrify(sql3, [data])
    # print(x)
    # cursor.execute(sql3,[data])
    # out = cursor.fetchall()
    # print(out)

    # cursor = connection.cursor(cursor_factory=RealDictCursor)
    # out = {}
    # for item in sqlTuple:
    #     cursor.execute(item[1])
    #     out[item[0]] = cursor.fetchall()

    # print(out)
    connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    if connection:
        connection.rollback()
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
