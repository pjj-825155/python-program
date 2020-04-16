import pymysql

conn=pymysql.connect("localhost","root","","1")
cur=conn.cursor()
filename=open("logs-1007.txt","r",encoding="UTF-8")
#清空
cur.execute("truncate table program1")
id_list=[]
num=1
log=filename.readline()
while log:
    log=log.replace("\n","")
    #输出正确的
    if log[-1]!="确":
        log=filename.readline()
        while log[0]!="-":
            log=filename.readline()
        log=filename.readline()
        continue
    id_name=log[:11]
    if id_name not in id_list:
        id_list.append(id_name)
        #添加id
        cur.execute("insert into program1 values('"+str(num)+"','"+str(id_name)+"','','','','','','')")
        num+=1
    #print(id_name)
    pro=log[19:23]
    #print(pro)
    log=filename.readline()
    code=""
    while log[0]!="-":
        #去掉tab,换行,空格
        log=log.replace("\t","")
        log=log.replace("\n","")
        log=log.replace(" ","")
        #单引号转双引号
        log=log.replace("\'","\"")
        code=code+log
        log=filename.readline()
    #print(code)
    if len(code)>=2000:
        code=code[:2000]
    cur.execute("update program1 set p"+str(pro)+"='"+code+"' where id='"+str(id_name)+"'")
    
    log=filename.readline()
