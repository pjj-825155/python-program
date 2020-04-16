import sys,random,math,pygame,time,os
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((860,720),0,0)

pygame.mixer.music.load(r'背景音乐/上海アリス幻樂団 - 輝く針の小人族 .mp3')
pygame.mixer.music.set_volume(0.2)#设置音量
pygame.mixer.music.play()

text=pygame.font.Font("C:/Windows/Fonts/simsun.ttc",20)
text_df=text.render("得分:",1,(225,225,225))

bg=pygame.image.load("背景图片/背景.jpg").convert()#不透明
bg=pygame.transform.smoothscale(bg,(860,720))

#加载人物
rw1=pygame.image.load("人物图片/灵梦.png").convert_alpha()#透明
rw1=pygame.transform.smoothscale(rw1,(60,80))
rw2=pygame.image.load("人物图片/魔理沙.png").convert_alpha()#透明
rw2=pygame.transform.smoothscale(rw2,(60,80))
rw3=pygame.image.load("人物图片/幽幽子.png").convert_alpha()#透明
rw3=pygame.transform.smoothscale(rw3,(60,80))
rw4=pygame.image.load("人物图片/妖梦.png").convert_alpha()#透明
rw4=pygame.transform.smoothscale(rw4,(60,80))
rw5=pygame.image.load("人物图片/蕾米莉亚.png").convert_alpha()#透明
rw5=pygame.transform.smoothscale(rw5,(60,80))
rw6=pygame.image.load("人物图片/咲夜.png").convert_alpha()#透明
rw6=pygame.transform.smoothscale(rw6,(60,80))
rw7=pygame.image.load("人物图片/八云紫.png").convert_alpha()#透明
rw7=pygame.transform.smoothscale(rw7,(60,80))

pd=pygame.image.load("判定点/判定点.png").convert_alpha()#透明
pd=pygame.transform.smoothscale(pd,(10,10))

#加载子弹
zd1=pygame.image.load("子弹图片/灵梦子弹.png").convert_alpha()#透明
zd1=pygame.transform.smoothscale(zd1,(10,30))
zd2=pygame.image.load("子弹图片/魔理沙子弹.png").convert_alpha()#透明
zd2=pygame.transform.smoothscale(zd2,(10,30))
zd3=pygame.image.load("子弹图片/幽幽子子弹.png").convert_alpha()#透明
zd3=pygame.transform.smoothscale(zd3,(10,30))
zd4=pygame.image.load("子弹图片/妖梦子弹.png").convert_alpha()#透明
zd4=pygame.transform.smoothscale(zd4,(10,30))
zd5=pygame.image.load("子弹图片/蕾米莉亚子弹.png").convert_alpha()#透明
zd5=pygame.transform.smoothscale(zd5,(10,30))
zd6=pygame.image.load("子弹图片/咲夜子弹.png").convert_alpha()#透明
zd6=pygame.transform.smoothscale(zd6,(10,30))
zd7=pygame.image.load("子弹图片/八云紫子弹.png").convert_alpha()#透明
zd7=pygame.transform.smoothscale(zd7,(10,30))

#记录人物坐标
x=320
y=640

#记录子弹
num=1
zi_dan_x=[0]*300
zi_dan_y=[0]*300
ge_shu=4#分为1到4

#记录类型
rw=rw1
zd=zd1

while True:
    if pygame.mixer.music.get_busy()==False:#循环播放歌曲
        pygame.mixer.music.play()

    screen.blit(bg,(0,0))#画背景
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
            pygame.quit()
            sys.exit()

    key_pressed=pygame.key.get_pressed()
    
    #改变人物和子弹
    if key_pressed[K_1]:
            rw=rw1
            zd=zd1
    if key_pressed[K_2]:
            rw=rw2
            zd=zd2
    if key_pressed[K_3]:
            rw=rw3
            zd=zd3
    if key_pressed[K_4]:
            rw=rw4
            zd=zd4
    if key_pressed[K_5]:
            rw=rw5
            zd=zd5
    if key_pressed[K_6]:
            rw=rw6
            zd=zd6
    if key_pressed[K_7]:
            rw=rw7
            zd=zd7

    x,y = pygame.mouse.get_pos()
    x-=25
    y-=55
    if x>=640:
        x=640
    if y>=640:
        y=640
        
    shu_zuo,shu_zhong,shu_you = pygame.mouse.get_pressed()
    if shu_zuo==1 or shu_zhong==1 or shu_you==1:#发射子弹
        if shu_zuo==1:
            ge_shu=1
        if shu_zhong==1:
            ge_shu=2
        if shu_you==1:
            ge_shu=3
        if num>=280:#子弹计数清零
            num=0
        while zi_dan_x[num]!=0:
            num+=1
            
        #一次发射子弹个数
        if ge_shu==1:
            zi_dan_x[num]=x+25#子弹赋坐标
            zi_dan_y[num]=y-15
            num+=1
        if ge_shu==2:
            zi_dan_x[num]=x+15
            zi_dan_y[num]=y-15
            num+=1
            zi_dan_x[num]=x+35
            zi_dan_y[num]=y-15
            num+=1
        if ge_shu==3:
            zi_dan_x[num]=x+25
            zi_dan_y[num]=y-15
            num+=1
            zi_dan_x[num]=x-10
            zi_dan_y[num]=y+30
            num+=1
            zi_dan_x[num]=x+60
            zi_dan_y[num]=y+30
            num+=1
        if ge_shu==4:
            zi_dan_x[num]=x+15
            zi_dan_y[num]=y-15
            num+=1
            zi_dan_x[num]=x+35
            zi_dan_y[num]=y-15
            num+=1
            zi_dan_x[num]=x-10
            zi_dan_y[num]=y+30
            num+=1
            zi_dan_x[num]=x+60
            zi_dan_y[num]=y+30
            num+=1
            
    i=0
    while i<300:
        if zi_dan_y[i]<=0:
            zi_dan_x[i]=0
            zi_dan_y[i]=0
        if zi_dan_y[i]!=0:
            screen.blit(zd,(zi_dan_x[i],zi_dan_y[i]))#子弹前移
            zi_dan_y[i]-=15
        i+=1
            
    screen.blit(rw,(x,y))#画人物
    screen.blit(pd,(x+20,y+50))#画判定点
    screen.blit(text_df,(710,100))#画得分
    pygame.draw.aaline(screen,(0,0,0),(701,0),(701,720),1)#分割线
    pygame.draw.aaline(screen,(0,0,0),(702,0),(702,720),1)
    pygame.display.flip()#刷新绘制线条
    pygame.display.update()
    clock.tick(60)#限制更新频率
