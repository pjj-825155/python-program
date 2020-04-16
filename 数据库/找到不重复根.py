import pymysql
import queue
q=queue.Queue()
conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
sql="select distinct from_user from pysql where from_user not in (select to_user from pysql)"
cur.execute(sql)
root=cur.fetchone()
root=list(root)
print(type(root))
#进队列
q.put(root[0])
#出队列
print(q.get())
conn.close()
