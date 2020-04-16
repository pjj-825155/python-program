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

rw=pygame.image.load("人物图片/灵梦.png").convert_alpha()#透明
rw=pygame.transform.smoothscale(rw,(60,80))
rw= pygame.transform.rotate(rw,0)

pd=pygame.image.load("判定点/判定点.png").convert_alpha()#透明
pd=pygame.transform.smoothscale(pd,(10,10))

#记录人物坐标
x=320
y=640

#记录初始位置
m=-20
n=-50

#记录移动
zong=0
heng=0

#记录方向
fx=0
jd=0

while True:
    if pygame.mixer.music.get_busy()==False:#循环播放歌曲
        pygame.mixer.music.play()

    screen.blit(bg,(0,0))#画背景
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
            pygame.quit()
            sys.exit()
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        m,n = pygame.mouse.get_pos()
        m-=25
        n-=55
        if m>=640:
            m=640
        if n>=640:
            n=640
    if m!=-20 and n!=-50:
        zong=n-y
        heng=m-x
        xie=math.hypot(abs(zong),abs(heng))
        #计算坐标，计算移动方向和速度
        if abs(heng)>1 or abs(zong)>1:
            if abs(heng)>=abs(zong):
                zong=zong/abs(heng)
                heng=heng/abs(heng)
            else:
                heng=heng/abs(zong)
                zong=zong/abs(zong)
                
        #计算旋转角度
        if zong==0 and heng<0:
            fx=90
        elif zong>0 and heng==0:
            fx=180
        elif zong==0 and heng>0:
            fx=270
        elif zong<0 and heng==0:
            fx=0
        else:
            if zong<0 and heng<0:
                fx=math.asin(abs(heng)/xie)*180/math.pi
            elif zong>0 and heng<0:
                fx=180-math.asin(abs(heng)/xie)*180/math.pi
            elif zong>0 and heng>0:
                fx=180+math.asin(abs(heng)/xie)*180/math.pi
            elif zong<0 and heng>0:
                fx=360-math.asin(abs(heng)/xie)*180/math.pi
        #rw=pygame.transform.rotate(rw,fx-jd)
        jd=fx

    x+=heng
    y+=zong
    
    screen.blit(rw,(x,y))#画人物
    screen.blit(pd,(m+20,n+50))#画判定点
    pygame.draw.aaline(screen,(255,255,255),(m+25,n+55),(x+20,y+50),1)#连线
    screen.blit(text_df,(710,100))#画得分
    pygame.draw.aaline(screen,(0,0,0),(701,0),(701,720),1)#分割线
    pygame.draw.aaline(screen,(0,0,0),(702,0),(702,720),1)
    pygame.display.flip()#刷新绘制线条
    pygame.display.update()
    clock.tick(60)#限制更新频率
