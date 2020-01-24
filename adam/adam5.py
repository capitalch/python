import simplejson as json
import pandas as pd
import numpy as np
import psycopg2
from itertools import repeat
from psycopg2.extras import RealDictCursor, DictCursor

sql1 = ''' select "id", "accCode", "accName" from "AccM" where "accLeaf" = 'Y' '''
sql2 = ''' select "id", "accId", "amount" from "TranD" '''
sqlList = [sql1, sql2]
sqlTuple = [('sql1',sql1),('sql2',sql2)]

try:
    connection = None
    with open('config.json') as f:
        cfg = json.load(f)
    connection = psycopg2.connect(
        user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    out = {}
    for item in sqlTuple:
        cursor.execute(item[1])
        out[item[0]] = cursor.fetchall()
        # out.append(cursor.fetchall())
    
    print(out)
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