import pandas as pd
import sqlanydb
from string import Template

mydf1 = pd.read_csv('mydata/test.txt')
sql = '''select item, brand, model, qty, price, "date"
    from bill_memo key join bill_memo_product
        key join inv_main
            key join product
                order by "date" '''
def getconn(db):
    return sqlanydb.connect(uid='dba', pwd='sql', eng='server', dbn=db, host='kushserver' )

def get_amount(row):
    return float(row['qty']) * float(row['price'])

pd.options.display.float_format = '{:,.0f}'.format

conn = sqlanydb.connect(uid='dba', pwd='sql', eng='server', dbn='sony', host='kushserver' )
cur = conn.cursor()
cur.execute('update adjustment set remarks = 'adj1' where adj_id = 3)
cur.commit()

dfa = pd.read_sql_query(sql, getconn('capi2013'))
dfa['month'] = pd.to_datetime(dfa['date']).dt.month
dfa['year'] =  pd.to_datetime(dfa['date']).dt.year
dfa['amount'] =  dfa.apply(get_amount, axis=1)

dfb = pd.read_sql_query(sql, getconn('capi2014'))
dfb['month'] = pd.to_datetime(dfb['date']).dt.month
dfb['year'] =  pd.to_datetime(dfb['date']).dt.year
dfb['amount'] =  dfb.apply(get_amount, axis=1)

dfc = pd.read_sql_query(sql, getconn('capi2015'))
dfc['month'] = pd.to_datetime(dfc['date']).dt.month
dfc['year'] =  pd.to_datetime(dfc['date']).dt.year
dfc['amount'] =  dfc.apply(get_amount, axis=1)

df1 = pd.read_sql_query(sql, getconn('capi2016'))
df1['month'] = pd.to_datetime(df1['date']).dt.month
df1['year'] =  pd.to_datetime(df1['date']).dt.year
df1['amount'] =  df1.apply(get_amount, axis=1)

df2 = pd.read_sql_query(sql, getconn('capi2017'))
df2['month'] = pd.to_datetime(df2['date']).dt.strftime('%Y-%m')
df2['year'] =  pd.to_datetime(df2['date']).dt.year
df2['month'] = pd.to_datetime(df2['date']).dt.month
df2['amount'] =  df2.apply(get_amount, axis=1)

df3 = pd.read_sql_query(sql, getconn('capi2018'))
df3['month'] = pd.to_datetime(df3['date']).dt.strftime('%Y-%m')
df3['year'] =  pd.to_datetime(df3['date']).dt.year
df3['month'] = pd.to_datetime(df3['date']).dt.month
df3['amount'] =  df3.apply(get_amount, axis=1)

df4 = pd.read_sql_query(sql, getconn('capi2019'))
df4['month'] = pd.to_datetime(df4['date']).dt.strftime('%Y-%m')
df4['year'] =  pd.to_datetime(df4['date']).dt.year
df4['month'] = pd.to_datetime(df4['date']).dt.month
df4['amount'] =  df4.apply(get_amount, axis=1)

df = [dfa,dfb,dfc,df1,df2,df3,df4]
df = pd.concat(df)

p = df.pivot_table( index='item', columns='year', values='amount', aggfunc=sum, fill_value=0)
p.to_excel('c:/sales_amount.xlsx')
#p.plot(kind='line', x='item', y='year')
p.head(10000)
