import simplejson as json
import pandas as pd
import numpy as np
import psycopg2
from itertools import repeat
from psycopg2.extras import RealDictCursor, DictCursor

def execSql(cursor):
    out = None
    sqlString = '''
        select "accCode", "accName", "accType", sum("amount") as amount, "dc" from
	        "TranD" t join "AccM" a on t."accId" = a."id"
		        where a."accLeaf" in('Y', 'L')
			        group by "accCode", "accName", "accType", "dc"
				        order by "accType" '''
    cursor.execute(sqlString)
    out = cursor.fetchall()
    return out

def trialBalance(data):
    df = pd.DataFrame(data)
    pivot = pd.pivot_table(df, index=["accCode"], columns=["dc"],
                       values="amount", aggfunc=np.sum, fill_value=0)
    pivot.rename(
        columns={
            'D': 'Debit',
            'C': 'Credit'
        },
        inplace=True
    )
    pivot['Closing'] =  + pivot['Debit'] - pivot['Credit']
    # pivot.loc['total'] = pivot.select_dtypes(pd.np.number).sum() # for summary
    # pivot.loc['Total',:]= df.sum(axis=1)
    # pivot.loc['total'] = pivot["Closing"].sum() # for summary

    pivot.loc['Total', 'Closing'] = pivot['Closing'].sum()
    pivot.loc['Total', 'Debit'] = pivot['Debit'].sum()
    pivot.loc['Total', 'Credit'] = pivot['Credit'].sum()

    pivot['clos_dc'] = pivot['Closing'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
    pivot['Closing'] = pivot['Closing'].apply(lambda x: x if x>=0 else -x) # remove minus sign
    
    print(pivot)
    j = pivot.to_json(orient='table')
    jsonObj = json.loads(j)
    dt = jsonObj["data"]
    return dt
try:
    connection = None
    with open('config.json') as f:
        cfg = json.load(f)
    connection = psycopg2.connect(
        user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    data = execSql(cursor)
    d = trialBalance(data)
    # print(d)
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
