
import sqlanydb
connection = None

sql = '''
truncate table tally_details;
truncate table tally;
truncate table part;
CALL sa_reset_identity( 'part', 'DBA', 0 );
'''

sql1 = '''
truncate table order_cancellation_details;
truncate table order_cancellation_all;
truncate table order_old;
truncate table order_current;
truncate table order_main;
truncate table order_groupa;
truncate table order_all;'''

sql2 = '''
truncate table inv_use_details;
CALL sa_reset_identity( 'inv_use_details', 'DBA', 0 );
truncate table inv_bill_details;
truncate table inv_sale_bill;
truncate table inv_invoice_details;
CALL sa_reset_identity( 'inv_invoice_details', 'DBA', 0 );
truncate table inv_purchase_invoice;
CALL sa_reset_identity( 'inv_purchase_invoice', 'DBA', 0 );'''

sql3='''
truncate table inv_physical_stock_hist_details;
truncate table inv_physical_stock_hist;
truncate table inv_physical_stock;
truncate table inv_other_charges;
CALL sa_reset_identity( 'inv_other_charges', 'DBA', 0 );
truncate table inv_loan_details;
CALL sa_reset_identity( 'inv_loan_details', 'DBA', 0 );
truncate table inv_loan_tran;
CALL sa_reset_identity( 'inv_loan_tran', 'DBA', 0 );'''

sql4='''
truncate table inv_direct_adjust;
CALL sa_reset_identity( 'inv_direct_adjust', 'DBA', 0 );
truncate table book_main;
truncate table book_cancellation_details;
truncate table book_cancellation_all;
truncate table book_all_details;
truncate table book_all;
truncate table adjustment;
CALL sa_reset_identity( 'adjustment', 'DBA', 0 );'''

sql5='''
truncate table inv_main;
CALL sa_reset_identity( 'inv_main', 'DBA', 0 );
'''
sql6 = '''
alter table inv_master alter part_code char(11)
'''

try:
    connection = sqlanydb.connect(uid='dba', pwd='sql', eng='server', dbn='sony', host='kushserver' )
    cur = connection.cursor()
    cur.execute(sql)
    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    cur.execute(sql4)
    cur.execute(sql5)
    cur.execute(sql6)
    connection.commit()
except(Exception) as error:
    print('Error', error)
    if connection:
        connection.rollback()
finally:
    if connection:
        cur.close()
        connection.close()
        print('Completed and connection closed')


