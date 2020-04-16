import sys,pygame,time
import numpy as np
from pygame.locals import *
pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,640),0,32)
#定义颜色的RGB参数
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
#设置窗口标题
pygame.display.set_caption("散点图")
#字体
text=pygame.font.Font("字体/simsun.ttc",20)
#人物
nor_per=text.render("•",1,WHITE)
dan_per=text.render("•",1,GREEN)
ill_per=text.render("•",1,RED)
#背景
screen.fill(BLACK)
#初始化参数
m=320
n=320
#隔离地坐标
x=640
y=0
#刷新频率
fps=60
#人数
per_num=1000
#活动能力
adl=1
#初始化坐标
area_x=[0.0]*per_num
area_y=[0.0]*per_num
#初始化状态
att=[0]*per_num
#是否隔离
qua=1
#隔离响应时间(天)
qua_time=1
#潜伏期计时
att_inc=[0]*per_num
#初始染病人数
ill_start=10
#感染范围
soi=1
#感染概率
prob=0.50
#潜伏期时间(天)
inc_time=14
#潜伏期是否感染
inc=1
for i in range(ill_start):
    while True:
        if att[np.random.randint(0,1000)]==0:
            att[np.random.randint(0,1000)]=1
            break
#正态分布随机
for i in range(per_num):
    while True:
        area_x[i]=round(np.random.normal(320,120),2)
        area_y[i]=round(np.random.normal(320,120),2)
        if 0<=area_x[i]<=620 and 0<=area_y[i]<=620:
            break

while True:
    screen.fill(BLACK)
    #分割线
    pygame.draw.aaline(screen,RED,(640,0),(640,640),1)
    for i in range(per_num):
        if att[i]==0:
            screen.blit(nor_per,(area_x[i],area_y[i]))
        if att[i]==1:
            screen.blit(dan_per,(area_x[i],area_y[i]))
        if att[i]==2:
            screen.blit(ill_per,(area_x[i],area_y[i]))
        #坐标改变
        if area_x[i]<640:
            if 0<=area_x[i]+(round(np.random.normal(0,1),2)*adl)<=620:
                area_x[i]+=(round(np.random.normal(0,1),2)*adl)
            if 0<=area_y[i]+(round(np.random.normal(0,1),2)*adl)<=620:
                area_y[i]+=(round(np.random.normal(0,1),2)*adl)

        #潜伏期
        if att[i]==1:
            att_inc[i]+=1
            if np.random.randint(0,inc_time*fps)<=att_inc[i]:
                att[i]=2
                att_inc[i]=0
                    
        #感染
        if att[i]==2 or (att[i]==1 and inc==1):
            for j in range(per_num):
                if att[j]==0:
                    if (area_x[i]-area_x[j])**2+(area_y[i]-area_y[j])**2<=soi**2:
                        if np.random.randint(0,100)<=(prob*100):
                            att[j]=1
        #隔离
        if qua==1:
            if att[i]==2:
                att_inc[i]+=1
            if att[i]==2 and att_inc[i]>=(qua_time*fps) and area_x[i]<640:
                area_x[i]=x
                area_y[i]=y
                y+=10
                if y>=640:
                    x+=10
                    y=0
                            
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    clock.tick(fps)
