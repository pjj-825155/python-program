import pymysql
file=open("重复率.txt","w")
conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
for x in range(1,202):
    for y in range(x+1,202):
        cur.execute("select id,p1034,p1059,p1069,p1147,p1114,p1158 from program1 where num="+str(x))
        a=cur.fetchone()
        cur.execute("select id,p1034,p1059,p1069,p1147,p1114,p1158 from program1 where num="+str(y))
        b=cur.fetchone()
        num=0
        if a[1]==b[1] and a[1]:
            num+=1
        if a[2]==b[2] and a[2]:
            num+=1
        if a[3]==b[3] and a[3]:
            num+=1
        if a[4]==b[4] and a[4]:
            num+=1
        if a[5]==b[5] and a[5]:
            num+=1
        if a[6]==b[6] and a[6]:
            num+=1
        if num>=5:
            file.write("id为"+a[0]+"和"+b[0]+"的重复程度为:%d"%num)
            file.write("\n")
            print("id为"+a[0]+"和"+b[0]+"的重复程度为:%d"%num)
file.close()
