import simplejson as json
import pandas as pd
import numpy as np
import psycopg2
from itertools import repeat
from psycopg2.extras import RealDictCursor, DictCursor

def execSql(cursor):
    out = None
    sqlString = '''
    set search_path to demounit1;
    -- GstInputAll (ExtGstTranD only), GstOutputAll (ExtGstTrand) based on "isInput"
    with cte1 as (
	select  "tranDate", "autoRefNo", "userRefNo", "tranType", "gstin", d."amount" - "cgst" - "sgst" - "igst" as "aggregate", "cgst", "sgst", "igst", d."amount",
            "accName",h."remarks", "dc", "lineRefNo", d."remarks" as "lineRemarks"
        from "TranH" h
            join "TranD" d
                on h."id" = d."tranHeaderId"
            join "ExtGstTranD" e
                on d."id" = e."tranDetailsId"
            join "AccM" a
                on a."id" = d."accId"
			join "TranTypeM" t
				on t."id" = h."tranTypeId"
        where
            ("cgst" <> 0 or
            "sgst" <> 0 or
            "igst" <> 0) and
			"isInput" = false and
			"finYearId" = 2021
--             "finYearId" = %(finYearId)s and
--             "branchId" = %(branchId)s and
--             ("tranDate" between %(fromDate)s and %(toDate)s)
        
        order by "tranDate", h."id"),
    
    -- GstNetSales (considering only table SalePurchaseDetails)
    cte2 as (
        select  "tranDate", "autoRefNo", "userRefNo", "tranType", 
        (select "gstin" from "ExtGstTranD" where "tranDetailsId" = d."id") as "gstin",
        "gstRate",
        CASE WHEN "tranTypeId" = 4 THEN (s."amount" - "cgst" - "sgst" - "igst") ELSE -(s."amount" - "cgst" - "sgst" - "igst") END as "aggregate",
        CASE WHEN "tranTypeId" = 4 THEN "cgst" ELSE -"cgst" END as "cgst",
        CASE WHEN "tranTypeId" = 4 THEN "sgst" ELSE -"sgst" END as "sgst",
        CASE WHEN "tranTypeId" = 4 THEN "igst" ELSE -"igst" END as "igst",
        CASE WHEN "tranTypeId" = 4 THEN s."amount" ELSE -s."amount" END as "amount",
        "accName", h."remarks", "dc", "lineRefNo", d."remarks" as "lineRemarks"
                from "TranH" h
                    join "TranD" d
                        on h."id" = d."tranHeaderId"
        --             join "ExtGstTranD" e
        --                 on d."id" = e."tranDetailsId"
                    join "AccM" a
                        on a."id" = d."accId"
                    join "TranTypeM" t
                        on t."id" = h."tranTypeId"
                    join "SalePurchaseDetails" s
                        on d."id" = s."tranDetailsId"
                where
                    ("cgst" <> 0 or
                    "sgst" <> 0 or
                    "igst" <> 0) and
                    "tranTypeId" in (4,9) and
        --			"isInput" = false and
                    "finYearId" = 2021
        --             "finYearId" = %(finYearId)s and
        --             "branchId" = %(branchId)s and
        --             ("tranDate" between %(fromDate)s and %(toDate)s)        
            order by "tranDate", h."id"
    ),

    -- GstNetPurchases (considering only table SalePurchaseDetails)
    cte3 as (
        select  "tranDate", "autoRefNo", "userRefNo", "tranType", 
        (select "gstin" from "ExtGstTranD" where "tranDetailsId" = d."id") as "gstin",
        "gstRate",
        CASE WHEN "tranTypeId" = 5 THEN (s."amount" - "cgst" - "sgst" - "igst") ELSE -(s."amount" - "cgst" - "sgst" - "igst") END as "aggregate",
        CASE WHEN "tranTypeId" = 5 THEN "cgst" ELSE -"cgst" END as "cgst",
        CASE WHEN "tranTypeId" = 5 THEN "sgst" ELSE -"sgst" END as "sgst",
        CASE WHEN "tranTypeId" = 5 THEN "igst" ELSE -"igst" END as "igst",
        CASE WHEN "tranTypeId" = 5 THEN s."amount" ELSE -s."amount" END as "amount",
        "accName", h."remarks", "dc", "lineRefNo", d."remarks" as "lineRemarks"
                from "TranH" h
                    join "TranD" d
                        on h."id" = d."tranHeaderId"
        --             join "ExtGstTranD" e
        --                 on d."id" = e."tranDetailsId"
                    join "AccM" a
                        on a."id" = d."accId"
                    join "TranTypeM" t
                        on t."id" = h."tranTypeId"
                    join "SalePurchaseDetails" s
                        on d."id" = s."tranDetailsId"
                where
                    ("cgst" <> 0 or
                    "sgst" <> 0 or
                    "igst" <> 0) and
                    "tranTypeId" in (5,10) and
        --			"isInput" = false and
                    "finYearId" = 2021
        --             "finYearId" = %(finYearId)s and
        --             "branchId" = %(branchId)s and
        --             ("tranDate" between %(fromDate)s and %(toDate)s)
        
        order by "tranDate", h."id"
    )
    cte4 as (
        select  "tranDate", "autoRefNo", "userRefNo", "tranType", 
        "gstin", "rate",
        d."amount" - "cgst" - "sgst" - "igst" as "aggregate", "cgst", "sgst", "igst", d."amount",
        "accName", h."remarks", "dc", "lineRefNo", d."remarks" as "lineRemarks"
                from "TranH" h
                    join "TranD" d
                        on h."id" = d."tranHeaderId"
                    join "ExtGstTranD" e
                        on d."id" = e."tranDetailsId"
                    join "AccM" a
                        on a."id" = d."accId"
                    join "TranTypeM" t
                        on t."id" = h."tranTypeId"
        --			join "SalePurchaseDetails" s
        --				on d."id" = s."tranDetailsId"
                where
                    ("cgst" <> 0 or
                    "sgst" <> 0 or
                    "igst" <> 0) and
                    "rate" is not null and -- When it is not a sale / purchase i.e voucher, then "gstRate" value exists in "ExtGstTranD" table otherwise not
                    "isInput" = true and -- Only applicable for GST through vouchers
                    "finYearId" = 2021
        --             "finYearId" = %(finYearId)s and
        --             "branchId" = %(branchId)s and
        --             ("tranDate" between %(fromDate)s and %(toDate)s)
                
        order by "tranDate", h."id"
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
    with open('adam/config.json') as f:
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
