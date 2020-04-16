import pymysql
conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
cur.execute("drop table if exists program1")
sql = """create table if not exists program1 (
         num int,
         id varchar(255),
         p1034 varchar(2047),
         p1059 varchar(2047),
         p1069 varchar(2047),
         p1147 varchar(2047),
         p1114 varchar(2047),
         p1158 varchar(2047));"""
#cur.execute(sql)
conn.close()
