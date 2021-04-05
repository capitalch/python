import psycopg2
from psycopg2.extras import RealDictCursor, DictCursor

def execSql(cursor):
    out = None
    sqlString = '''
    set search_path to demounit1;
    -- gst-input-all (ExtGstTranD only) based on "isInput"
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
			"isInput" = true and
			"finYearId" = 2021
--             "finYearId" = %(finYearId)s and
--             "branchId" = %(branchId)s and
--             ("tranDate" between %(fromDate)s and %(toDate)s)
        
        order by "tranDate", h."id"),
    
    -- gst-output-all (ExtGstTrand) based on "isInput"
    cte2 as (
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
    
    -- gst-output-net-sales (considering only table SalePurchaseDetails)
    cte3 as (
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
                    "finYearId" = 2021
        --             "finYearId" = %(finYearId)s and
        --             "branchId" = %(branchId)s and
        --             ("tranDate" between %(fromDate)s and %(toDate)s)        
            order by "tranDate", h."id"
    ),

    -- gst-input-net-purchases (considering only table SalePurchaseDetails)
    cte4 as (
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
                    "finYearId" = 2021
        --             "finYearId" = %(finYearId)s and
        --             "branchId" = %(branchId)s and
        --             ("tranDate" between %(fromDate)s and %(toDate)s)
        
        order by "tranDate", h."id"
    ),

    -- gst-input-vouchers
    cte5 as (
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
	select json_build_object(
            'gst-input-all', (SELECT json_agg(row_to_json(a)) from cte1 a),
			'gst-output-all', (SELECT json_agg(row_to_json(b)) from cte2 b),
            'gst-input-net-purchases', (SELECT json_agg(row_to_json(d)) from cte4 d),
            'gst-output-net-sales', (SELECT json_agg(row_to_json(c)) from cte3 c), 
			'gst-input-vouchers', (SELECT json_agg(row_to_json(e)) from cte5 e)
        ) as "jsonResult" '''
    cursor.execute(sqlString)
    out = cursor.fetchone()
    return out