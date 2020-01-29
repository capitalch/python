
import sqlanydb

connection = None
sql = '''
update adjustment set remarks = 'adj1' where adj_id = 3
update adjustment set remarks = 'adj2' where adj_id = 3
update adjustment set remarks = 'adj3' where adj_id = 3
update adjustment set remarks = 'adj5' where adj_id = 3
'''
try:
    connection = sqlanydb.connect(uid='dba', pwd='sql', eng='server', dbn='sony', host='kushserver' )
    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()
except(Exception) as error:
    print('Error', error)
    if connection:
        connection.rollback()
finally:
    if connection:
        cur.close()
        connection.close()
        print('Closed')