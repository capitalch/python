#Sql anywhere connection. remember to put host in connection if server is running on different machine
import sqlanydb
try:
    conn = sqlanydb.connect(uid='dba', pwd='sql', eng='server', dbn='capi2019', host='kushserver')
except (Exception, sqlanydb.Error) as error :
    print ("Error while connecting to Sql Anywhere", error)