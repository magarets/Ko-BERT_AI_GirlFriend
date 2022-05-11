import pymysql
import pandas as pd

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    db='alswn_db',
    charset='utf8'
)
cur = conn.cursor()
sql = 'select * from alswn'
cur.execute(sql)
res = cur.fetchall()
print(res)