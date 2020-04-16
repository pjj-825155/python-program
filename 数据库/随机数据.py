import pymysql
import random
conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
#清空
cur.execute("truncate table pysql_middle")
#多少条
number=1000

for i in range(1,number):
    cur.execute(f"insert into pysql_middle values('{str(i)}','{str(random.randint(0,(i-1)))}a','{str(i)}a','')")


#建索引
#cur.execute("ALTER TABLE `pysql` ADD INDEX index_name (`from_user`, `to_user`)")
conn.close()
