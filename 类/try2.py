from my_program import *

p1=Pro1("你好")
p1.shu_chu()
p1.jiao_hu()

p2=Pro2("你好，世界","hello world")
p2.shu_chu()
p2.jiao_hu()

p3=Pro3("你好","hello")
#用的新的def
p3.shu_chu()
#用的父类Pro1的def
p3.jiao_hu()
