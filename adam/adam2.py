# database connections
import psycopg2
import simplejson as json
from adam5 import headerSql, headerValuestuple
try:
    with open('config.json') as f:
        cfg = json.load(f)
    # connection = psycopg2.connect(user='webadmin', password='AMGnbm23767', host='node15792-chisel.cloudjiffy.net', port='11035', database='trace')
    connection = psycopg2.connect(user=cfg["user"], password=cfg["password"], host=cfg["host"], port=cfg["port"], database=cfg["database"])
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")
    # cursor.execute("SELECT count(*) from adam1;")
    cursor.execute(headerSql,headerValuestuple)
    record = cursor.fetchone()
    connection.commit()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    connection.rollback()
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")