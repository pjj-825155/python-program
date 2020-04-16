#我的第一个类
class Pro1:
    content=""
    def __init__(self,p):
        self.content=p
    def shu_chu(self):
        print(self.content)
    def jiao_hu(self):
        content=input("请输入：")
        print(content)
#一个新的类
class Pro2:
    con1=""
    con2=""
    def __init__(self,c1,c2):
        self.con1=c1
        self.con2=c2
    def shu_chu(self):
        print(self.con1,self.con2)
    def jiao_hu(self):
        con1,con2=input("数字1："),input("数字2：")
        print(con1,con2)
#继承Pro1的类
class Pro3(Pro1):
    a=""
    def __init__(self,p,a):
        Pro1.__init__(self,p)
        self.a=a
    def shu_chu(self):
        print(self.a)
