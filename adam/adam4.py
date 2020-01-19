import simplejson as json
import pandas as pd
import numpy as np
import psycopg2
from itertools import repeat
from psycopg2.extras import RealDictCursor, DictCursor

def execSql(cursor):
    out = None
    sqlString = '''
    with cte1 as (
	select a."id" as id1, b."id" as id2, a."accCode", a."accName", a."accType", a."accLeaf"
		from "AccM" a join "AccM" b on a."id" = b."parentId"
			where a."accLeaf" in ('L')
		union all
	select "id" as id1,"id" as id2, "accCode", "accName", "accType", "accLeaf"
		from "AccM" where "accLeaf" = 'Y'),
    cte2 as (
        select "accId", "dc", "amount"
            from "TranD"
                union all
            select "accId", 'O' as dc, CASE WHEN "dc" = 'D' THEN "amount" else -"amount" END as amount
                from "AccOpBal"
    )

    select  a."id1" as id, a."accCode", a."accName", a."accType", a."accLeaf", "dc", sum(amount) as amount
        from cte1 a join cte2 b
            on a."id2" = b."accId"
                group by "id", a."accCode", a."accName", a."accType", a."accLeaf", b."dc"
                    order by a."accType", a."accCode", a."accName", b."dc" '''
    cursor.execute(sqlString)
    out = cursor.fetchall()
    return out

def trialBalance(data):
    df = pd.DataFrame(data)
    pivot = pd.pivot_table(df, index=["accCode", "accName", "accType"], columns=["dc"],
                       values="amount", aggfunc=np.sum, fill_value=0)
    
    pivot.rename(
        columns={
            'O': 'Opening',
            'D': 'Debit',
            'C': 'Credit'
        },
        inplace=True
    )
    pivot['Closing'] = pivot['Opening'] + pivot['Debit'] - pivot['Credit']

    pivot.loc['Total', 'Closing'] = pivot['Closing'].sum()
    pivot.loc['Total', 'Debit'] = pivot['Debit'].sum()
    pivot.loc['Total', 'Credit'] = pivot['Credit'].sum()
    pivot.loc['Total', 'Opening'] = pivot['Opening'].sum()
    
    pivot['Closing_dc'] = pivot['Closing'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
    pivot['Closing'] = pivot['Closing'].apply(lambda x: x if x>=0 else -x) # remove minus sign
    
    pivot['Opening_dc'] = pivot['Opening'].apply(lambda x: 'Dr' if x >= 0 else 'Cr')
    pivot['Opening'] = pivot['Opening'].apply(lambda x: x if x>=0 else -x) # remove minus sign
    
    pivot = pivot.reindex(columns= ['Opening', 'Opening_dc', 'Debit', 'Credit', 'Closing', 'Closing_dc'])
    
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
