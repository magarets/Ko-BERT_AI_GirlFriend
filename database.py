import pymysql
import pandas as pd

DB = 'Customer'

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    db=DB,
    charset='utf8'
)
cur = conn.cursor()
#sql = 'select * from Customer'
sql = ''
while(sql != 'stop'):
    sql = input("SQL : ")
    cur.execute(sql)
    res = cur.fetchall()

    if(res):
        for DBdata in res:
            print(DBdata)
        print('')
    else:
        print("ERROR")
