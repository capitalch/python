# database connections
import psycopg2
try:
    connection = psycopg2.connect(user='webadmin', password='AMGnbm23767', host='node15792-chisel.cloudjiffy.net', port='11035', database='postgres')
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")
    cursor.execute("SELECT count(*) from comments;")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")