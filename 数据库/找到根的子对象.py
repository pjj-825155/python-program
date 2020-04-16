import pymysql
import queue
q=queue.Queue()
conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
sql1="select distinct from_user from pysql where from_user not in (select to_user from pysql)"
cur.execute(sql1)
root=cur.fetchone()
root=list(root)
q.put(root[0])
root=q.get()
sql2="select to_user from pysql where from_user='"+root+"'"
cur.execute(sql2)
res=cur.fetchall()
for son in res:
    son=list(son)
    q.put(son[0])
    print(q.get())
