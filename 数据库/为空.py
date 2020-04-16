import pymysql

conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
cur.execute("select * from pysql_low where id=2")
root=cur.fetchone()
if root[1]==null:
    print(1)
print(root[1])
