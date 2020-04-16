import pymysql
conn=pymysql.connect("localhost","root","","1")
cursor=conn.cursor()
cursor.execute("select * from pysql")
one_data = cursor.fetchone()
print(one_data)
conn.close()
