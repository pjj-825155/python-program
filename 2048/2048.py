import sys,random,pygame,time
from pygame.locals import *
pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((720,720),FULLSCREEN,32)
#定义颜色的RGB参数
WHITE=(255,255,255)
YELLOW=(255,255,0)
GOLD=(255,215,0)
RED=(255,0,0)
colour_2=(255,250,240)
colour_4=(255,218,185)
colour_8=(233,150,122)
colour_16=(255,165,0)
colour_32=(255,127,80)
colour_64=(255,99,71)
colour_128=(255,0,0)
colour_256=(255,105,180)
colour_512=(255,20,147)
colour_1024=(255,0,255)
colour_2048=(208,32,144)
colour_4096=(176,48,96)
colour_8192=(153,50,204)
BLACK=(0,0,0)
#设置窗口标题
pygame.display.set_caption("2048")
#加载音乐
pygame.mixer.music.load(r'音乐/Thomas Newman - Por Una Cabeza.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()
#设置字体
text=pygame.font.Font("字体/simsun.ttc",40)
#背景
screen.fill(WHITE)
#文字
start=text.render("开始游戏",1,BLACK)
#数字
num2=text.render("2",1,BLACK)
num4=text.render("4",1,BLACK)
num8=text.render("8",1,BLACK)
num16=text.render("16",1,BLACK)
num32=text.render("32",1,BLACK)
num64=text.render("64",1,BLACK)
num128=text.render("128",1,BLACK)
num256=text.render("256",1,BLACK)
num512=text.render("512",1,BLACK)
num1024=text.render("1024",1,BLACK)
num2048=text.render("2048",1,BLACK)
num4096=text.render("4096",1,BLACK)
num8192=text.render("8192",1,BLACK)
while True:
    screen.fill(WHITE)
    #初始化
    flag=0
    appear=1
    sum11=0
    sum12=0
    sum13=0
    sum14=0
    sum21=0
    sum22=0
    sum23=0
    sum24=0
    sum31=0
    sum32=0
    sum33=0
    sum34=0
    sum41=0
    sum42=0
    sum43=0
    sum44=0
    screen.blit(start,(280,340))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            m,n = pygame.mouse.get_pos()
            if 280<=m<=440 and 340<=n<=380:
                m=0
                n=0
                flag=1
    while flag==1:
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.play()
        screen.fill(WHITE)
        pygame.draw.polygon(screen,YELLOW,[(75,75),(75,645),(645,645),(645,75)],0)
        #格子
        pygame.draw.polygon(screen,GOLD,[(75,75),(75,81),(645,81),(645,75)],0)
        pygame.draw.polygon(screen,GOLD,[(75,216),(75,222),(645,222),(645,216)],0)
        pygame.draw.polygon(screen,GOLD,[(75,357),(75,363),(645,363),(645,357)],0)
        pygame.draw.polygon(screen,GOLD,[(75,498),(75,504),(645,504),(645,498)],0)
        pygame.draw.polygon(screen,GOLD,[(75,639),(75,645),(645,645),(645,639)],0)
        pygame.draw.polygon(screen,GOLD,[(75,75),(81,75),(81,645),(75,645)],0)
        pygame.draw.polygon(screen,GOLD,[(216,75),(222,75),(222,645),(216,645)],0)
        pygame.draw.polygon(screen,GOLD,[(357,75),(363,75),(363,645),(357,645)],0)
        pygame.draw.polygon(screen,GOLD,[(498,75),(504,75),(504,645),(498,645)],0)
        pygame.draw.polygon(screen,GOLD,[(639,75),(645,75),(645,645),(639,645)],0)
        #方向键
        pygame.draw.polygon(screen,RED,[(360,0),(335,25),(385,25)],0)#上
        pygame.draw.polygon(screen,RED,[(720,360),(695,335),(695,385)],0)#右
        pygame.draw.polygon(screen,RED,[(0,360),(25,335),(25,385)],0)#左
        pygame.draw.polygon(screen,RED,[(360,720),(335,695),(385,695)],0)#下
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    flag=0
                if event.key==pygame.K_w or event.key==pygame.K_UP:
                    for i in range(0,5):
                        if sum11==0 or sum11==sum21:
                            if sum21!=0:
                                sum11=sum11+sum21
                                sum21=0
                                appear=1
                        if sum12==0 or sum12==sum22:
                            if sum22!=0:
                                sum12=sum12+sum22
                                sum22=0
                                appear=1
                        if sum13==0 or sum13==sum23:
                            if sum23!=0:
                                sum13=sum13+sum23
                                sum23=0
                                appear=1
                        if sum14==0 or sum14==sum24:
                            if sum24!=0:
                                sum14=sum14+sum24
                                sum24=0
                                appear=1
                        if sum21==0 or sum21==sum31:
                            if sum31!=0:
                                sum21=sum21+sum31
                                sum31=0
                                appear=1
                        if sum22==0 or sum22==sum32:
                            if sum32!=0:
                                sum22=sum22+sum32
                                sum32=0
                                appear=1
                        if sum23==0 or sum23==sum33:
                            if sum33!=0:
                                sum23=sum23+sum33
                                sum33=0
                                appear=1
                        if sum24==0 or sum24==sum34:
                            if sum34!=0:
                                sum24=sum24+sum34
                                sum34=0
                                appear=1
                        if sum31==0 or sum31==sum41:
                            if sum41!=0:
                                sum31=sum31+sum41
                                sum41=0
                                appear=1
                        if sum32==0 or sum32==sum42:
                            if sum42!=0:
                                sum32=sum32+sum42
                                sum42=0
                                appear=1
                        if sum33==0 or sum33==sum43:
                            if sum43!=0:
                                sum33=sum33+sum43
                                sum43=0
                                appear=1
                        if sum34==0 or sum34==sum44:
                            if sum44!=0:
                                sum34=sum34+sum44
                                sum44=0
                                appear=1
                if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                    for i in range(0,5):
                        if sum41==0 or sum41==sum31:
                            if sum31!=0:
                                sum41=sum41+sum31
                                sum31=0
                                appear=1
                        if sum42==0 or sum42==sum32:
                            if sum32!=0:
                                sum42=sum42+sum32
                                sum32=0
                                appear=1
                        if sum43==0 or sum43==sum33:
                            if sum33!=0:
                                sum43=sum43+sum33
                                sum33=0
                                appear=1
                        if sum44==0 or sum44==sum34:
                            if sum34!=0:
                                sum44=sum44+sum34
                                sum34=0
                                appear=1
                        if sum31==0 or sum31==sum21:
                            if sum21!=0:
                                sum31=sum21+sum31
                                sum21=0
                                appear=1
                        if sum32==0 or sum22==sum32:
                            if sum22!=0:
                                sum32=sum22+sum32
                                sum22=0
                                appear=1
                        if sum33==0 or sum23==sum33:
                            if sum23!=0:
                                sum33=sum23+sum33
                                sum23=0
                                appear=1
                        if sum34==0 or sum24==sum34:
                            if sum24!=0:
                                sum34=sum24+sum34
                                sum24=0
                                appear=1
                        if sum21==0 or sum21==sum11:
                            if sum11!=0:
                                sum21=sum21+sum11
                                sum11=0
                                appear=1
                        if sum22==0 or sum22==sum12:
                            if sum12!=0:
                                sum22=sum22+sum12
                                sum12=0
                                appear=1
                        if sum23==0 or sum13==sum23:
                            if sum13!=0:
                                sum23=sum13+sum23
                                sum13=0
                                appear=1
                        if sum24==0 or sum24==sum14:
                            if sum14!=0:
                                sum24=sum24+sum14
                                sum14=0
                                appear=1
                if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                    for i in range(0,5):
                        if sum11==0 or sum11==sum12:
                            if sum12!=0:
                                sum11=sum11+sum12
                                sum12=0
                                appear=1
                        if sum21==0 or sum21==sum22:
                            if sum22!=0:
                                sum21=sum21+sum22
                                sum22=0
                                appear=1
                        if sum31==0 or sum31==sum32:
                            if sum32:
                                sum31=sum31+sum32
                                sum32=0
                                appear=1
                        if sum41==0 or sum41==sum42:
                            if sum42!=0:
                                sum41=sum41+sum42
                                sum42=0
                                appear=1
                        if sum12==0 or sum12==sum13:
                            if sum13!=0:
                                sum12=sum12+sum13
                                sum13=0
                                appear=1
                        if sum22==0 or sum22==sum23:
                            if sum23!=0:
                                sum22=sum22+sum23
                                sum23=0
                                appear=1
                        if sum32==0 or sum32==sum33:
                            if sum33!=0:
                                sum32=sum32+sum33
                                sum33=0
                                appear=1
                        if sum42==0 or sum42==sum43:
                            if sum43!=0:
                                sum42=sum42+sum43
                                sum43=0
                                appear=1
                        if sum13==0 or sum13==sum14:
                            if sum14!=0:
                                sum13=sum13+sum14
                                sum14=0
                                appear=1
                        if sum23==0 or sum23==sum24:
                            if sum24!=0:
                                sum23=sum23+sum24
                                sum24=0
                                appear=1
                        if sum33==0 or sum33==sum34:
                            if sum34!=0:
                                sum33=sum33+sum34
                                sum34=0
                                appear=1
                        if sum43==0 or sum43==sum44:
                            if sum44!=0:
                                sum43=sum43+sum44
                                sum44=0
                                appear=1
                if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                    for i in range(0,5):
                        if sum14==0 or sum14==sum13:
                            if sum13!=0:
                                sum14=sum14+sum13
                                sum13=0
                                appear=1
                        if sum24==0 or sum24==sum23:
                            if sum23!=0:
                                sum24=sum24+sum23
                                sum23=0
                                appear=1
                        if sum34==0 or sum34==sum33:
                            if sum33!=0:
                                sum34=sum34+sum33
                                sum33=0
                                appear=1
                        if sum44==0 or sum44==sum43:
                            if sum43!=0:
                                sum44=sum44+sum43
                                sum43=0
                                appear=1
                        if sum13==0 or sum12==sum13:
                            if sum12!=0:
                                sum13=sum12+sum13
                                sum12=0
                                appear=1
                        if sum23==0 or sum22==sum23:
                            if sum22!=0:
                                sum23=sum22+sum23
                                sum22=0
                                appear=1
                        if sum33==0 or sum32==sum33:
                            if sum32!=0:
                                sum33=sum32+sum33
                                sum32=0
                                appear=1
                        if sum43==0 or sum42==sum43:
                            if sum42!=0:
                                sum43=sum42+sum43
                                sum42=0
                                appear=1
                        if sum12==0 or sum12==sum11:
                            if sum11!=0:
                                sum12=sum12+sum11
                                sum11=0
                                appear=1
                        if sum22==0 or sum22==sum21:
                            if sum21!=0:
                                sum22=sum21+sum22
                                sum21=0
                                appear=1
                        if sum32==0 or sum32==sum31:
                            if sum31!=0:
                                sum32=sum32+sum31
                                sum31=0
                                appear=1
                        if sum42==0 or sum42==sum41:
                            if sum41!=0:
                                sum42=sum42+sum41
                                sum41=0
                                appear=1
            if event.type==pygame.MOUSEBUTTONDOWN:
                m,n = pygame.mouse.get_pos()
                if 0<=m<=50 and 0<=n<=75:
                    m=0
                    n=0
                    flag=0
                if 335<m<385 and 0<n<25:#上
                    for i in range(0,5):
                        if sum11==0 or sum11==sum21:
                            if sum21!=0:
                                sum11=sum11+sum21
                                sum21=0
                                appear=1
                        if sum12==0 or sum12==sum22:
                            if sum22!=0:
                                sum12=sum12+sum22
                                sum22=0
                                appear=1
                        if sum13==0 or sum13==sum23:
                            if sum23!=0:
                                sum13=sum13+sum23
                                sum23=0
                                appear=1
                        if sum14==0 or sum14==sum24:
                            if sum24!=0:
                                sum14=sum14+sum24
                                sum24=0
                                appear=1
                        if sum21==0 or sum21==sum31:
                            if sum31!=0:
                                sum21=sum21+sum31
                                sum31=0
                                appear=1
                        if sum22==0 or sum22==sum32:
                            if sum32!=0:
                                sum22=sum22+sum32
                                sum32=0
                                appear=1
                        if sum23==0 or sum23==sum33:
                            if sum33!=0:
                                sum23=sum23+sum33
                                sum33=0
                                appear=1
                        if sum24==0 or sum24==sum34:
                            if sum34!=0:
                                sum24=sum24+sum34
                                sum34=0
                                appear=1
                        if sum31==0 or sum31==sum41:
                            if sum41!=0:
                                sum31=sum31+sum41
                                sum41=0
                                appear=1
                        if sum32==0 or sum32==sum42:
                            if sum42!=0:
                                sum32=sum32+sum42
                                sum42=0
                                appear=1
                        if sum33==0 or sum33==sum43:
                            if sum43!=0:
                                sum33=sum33+sum43
                                sum43=0
                                appear=1
                        if sum34==0 or sum34==sum44:
                            if sum44!=0:
                                sum34=sum34+sum44
                                sum44=0
                                appear=1
                if 0<m<25 and 335<n<385:#左
                    for i in range(0,5):
                        if sum11==0 or sum11==sum12:
                            if sum12!=0:
                                sum11=sum11+sum12
                                sum12=0
                                appear=1
                        if sum21==0 or sum21==sum22:
                            if sum22!=0:
                                sum21=sum21+sum22
                                sum22=0
                                appear=1
                        if sum31==0 or sum31==sum32:
                            if sum32:
                                sum31=sum31+sum32
                                sum32=0
                                appear=1
                        if sum41==0 or sum41==sum42:
                            if sum42!=0:
                                sum41=sum41+sum42
                                sum42=0
                                appear=1
                        if sum12==0 or sum12==sum13:
                            if sum13!=0:
                                sum12=sum12+sum13
                                sum13=0
                                appear=1
                        if sum22==0 or sum22==sum23:
                            if sum23!=0:
                                sum22=sum22+sum23
                                sum23=0
                                appear=1
                        if sum32==0 or sum32==sum33:
                            if sum33!=0:
                                sum32=sum32+sum33
                                sum33=0
                                appear=1
                        if sum42==0 or sum42==sum43:
                            if sum43!=0:
                                sum42=sum42+sum43
                                sum43=0
                                appear=1
                        if sum13==0 or sum13==sum14:
                            if sum14!=0:
                                sum13=sum13+sum14
                                sum14=0
                                appear=1
                        if sum23==0 or sum23==sum24:
                            if sum24!=0:
                                sum23=sum23+sum24
                                sum24=0
                                appear=1
                        if sum33==0 or sum33==sum34:
                            if sum34!=0:
                                sum33=sum33+sum34
                                sum34=0
                                appear=1
                        if sum43==0 or sum43==sum44:
                            if sum44!=0:
                                sum43=sum43+sum44
                                sum44=0
                                appear=1
                if 335<m<385 and 695<n<720:#下
                    for i in range(0,5):
                        if sum41==0 or sum41==sum31:
                            if sum31!=0:
                                sum41=sum41+sum31
                                sum31=0
                                appear=1
                        if sum42==0 or sum42==sum32:
                            if sum32!=0:
                                sum42=sum42+sum32
                                sum32=0
                                appear=1
                        if sum43==0 or sum43==sum33:
                            if sum33!=0:
                                sum43=sum43+sum33
                                sum33=0
                                appear=1
                        if sum44==0 or sum44==sum34:
                            if sum34!=0:
                                sum44=sum44+sum34
                                sum34=0
                                appear=1
                        if sum31==0 or sum31==sum21:
                            if sum21!=0:
                                sum31=sum21+sum31
                                sum21=0
                                appear=1
                        if sum32==0 or sum22==sum32:
                            if sum22!=0:
                                sum32=sum22+sum32
                                sum22=0
                                appear=1
                        if sum33==0 or sum23==sum33:
                            if sum23!=0:
                                sum33=sum23+sum33
                                sum23=0
                                appear=1
                        if sum34==0 or sum24==sum34:
                            if sum24!=0:
                                sum34=sum24+sum34
                                sum24=0
                                appear=1
                        if sum21==0 or sum21==sum11:
                            if sum11!=0:
                                sum21=sum21+sum11
                                sum11=0
                                appear=1
                        if sum22==0 or sum22==sum12:
                            if sum12!=0:
                                sum22=sum22+sum12
                                sum12=0
                                appear=1
                        if sum23==0 or sum13==sum23:
                            if sum13!=0:
                                sum23=sum13+sum23
                                sum13=0
                                appear=1
                        if sum24==0 or sum24==sum14:
                            if sum14!=0:
                                sum24=sum24+sum14
                                sum14=0
                                appear=1
                if 695<m<720 and 335<n<385:#右
                    for i in range(0,5):
                        if sum14==0 or sum14==sum13:
                            if sum13!=0:
                                sum14=sum14+sum13
                                sum13=0
                                appear=1
                        if sum24==0 or sum24==sum23:
                            if sum23!=0:
                                sum24=sum24+sum23
                                sum23=0
                                appear=1
                        if sum34==0 or sum34==sum33:
                            if sum33!=0:
                                sum34=sum34+sum33
                                sum33=0
                                appear=1
                        if sum44==0 or sum44==sum43:
                            if sum43!=0:
                                sum44=sum44+sum43
                                sum43=0
                                appear=1
                        if sum13==0 or sum12==sum13:
                            if sum12!=0:
                                sum13=sum12+sum13
                                sum12=0
                                appear=1
                        if sum23==0 or sum22==sum23:
                            if sum22!=0:
                                sum23=sum22+sum23
                                sum22=0
                                appear=1
                        if sum33==0 or sum32==sum33:
                            if sum32!=0:
                                sum33=sum32+sum33
                                sum32=0
                                appear=1
                        if sum43==0 or sum42==sum43:
                            if sum42!=0:
                                sum43=sum42+sum43
                                sum42=0
                                appear=1
                        if sum12==0 or sum12==sum11:
                            if sum11!=0:
                                sum12=sum12+sum11
                                sum11=0
                                appear=1
                        if sum22==0 or sum22==sum21:
                            if sum21!=0:
                                sum22=sum21+sum22
                                sum21=0
                                appear=1
                        if sum32==0 or sum32==sum31:
                            if sum31!=0:
                                sum32=sum32+sum31
                                sum31=0
                                appear=1
                        if sum42==0 or sum42==sum41:
                            if sum41!=0:
                                sum42=sum42+sum41
                                sum41=0
                                appear=1
        #生成
        while appear==1:
            ro=random.randint(1,2)
            if ro==1:
                rc=random.randint(1,4)
                if rc==1:
                    rm=random.randint(1,3)
                    if rm==1:
                        if sum11==0:
                            sum11=2
                            appear=0
                    if rm==2:
                        if sum12==0:
                            sum12=2
                            appear=0
                    if rm==3:
                        if sum13==0:
                            sum13=2
                            appear=0
                if rc==2:
                    rm=random.randint(1,3)
                    if rm==1:
                        if sum14==0:
                            sum14=2
                            appear=0
                    if rm==2:
                        if sum24==0:
                            sum24=2
                            appear=0
                    if rm==3:
                        if sum34==0:
                            sum34=2
                            appear=0
                if rc==3:
                    rm=random.randint(1,3)
                    if rm==1:
                        if sum44==0:
                            sum44=2
                            appear=0
                    if rm==2:
                        if 43==0:
                            sum43=2
                            appear=0
                    if rm==3:
                        if sum42==0:
                            sum42=2
                            appear=0
                if rc==4:
                    rm=random.randint(1,3)
                    if rm==1:
                        if sum41==0:
                            sum41=2
                            appear=0
                    if rm==2:
                        if sum31==0:
                            sum31=2
                            appear=0
                    if rm==3:
                        if sum21==0:
                            sum21=2
                            appear=0
            if ro==2:
                rc=random.randint(1,4)
                if rc==1:
                    if sum22==0:
                        sum22=2
                        appear=0
                if rc==2:
                    if sum23==0:
                        sum23=2
                        appear=0
                if rc==3:
                    if sum32==0:
                        sum32=2
                        appear=0
                if rc==4:
                    if sum33==0:
                        sum33=2
                        appear=0
        #显示2            
        if sum11==2:
            pygame.draw.polygon(screen,colour_2,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num2,(138.5,128.5))
        if sum12==2:
            pygame.draw.polygon(screen,colour_2,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num2,(279.5,128.5))
        if sum13==2:
            pygame.draw.polygon(screen,colour_2,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num2,(420.5,128.5))
        if sum14==2:
            pygame.draw.polygon(screen,colour_2,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num2,(561.5,128.5))
        if sum21==2:
            pygame.draw.polygon(screen,colour_2,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num2,(138.5,269.5))
        if sum22==2:
            pygame.draw.polygon(screen,colour_2,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num2,(279.5,269.5))
        if sum23==2:
            pygame.draw.polygon(screen,colour_2,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num2,(420.5,269.5))
        if sum24==2:
            pygame.draw.polygon(screen,colour_2,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num2,(561.5,269.5))
        if sum31==2:
            pygame.draw.polygon(screen,colour_2,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num2,(138.5,410.5))
        if sum32==2:
            pygame.draw.polygon(screen,colour_2,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num2,(279.5,410.5))
        if sum33==2:
            pygame.draw.polygon(screen,colour_2,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num2,(420.5,410.5))
        if sum34==2:
            pygame.draw.polygon(screen,colour_2,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num2,(561.5,410.5))
        if sum41==2:
            pygame.draw.polygon(screen,colour_2,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num2,(138.5,551.5))
        if sum42==2:
            pygame.draw.polygon(screen,colour_2,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num2,(279.5,551.5))
        if sum43==2:
            pygame.draw.polygon(screen,colour_2,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num2,(420.5,551.5))
        if sum44==2:
            pygame.draw.polygon(screen,colour_2,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num2,(561.5,551.5))
        #显示4            
        if sum11==4:
            pygame.draw.polygon(screen,colour_4,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num4,(138.5,128.5))
        if sum12==4:
            pygame.draw.polygon(screen,colour_4,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num4,(279.5,128.5))
        if sum13==4:
            pygame.draw.polygon(screen,colour_4,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num4,(420.5,128.5))
        if sum14==4:
            pygame.draw.polygon(screen,colour_4,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num4,(561.5,128.5))
        if sum21==4:
            pygame.draw.polygon(screen,colour_4,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num4,(138.5,269.5))
        if sum22==4:
            pygame.draw.polygon(screen,colour_4,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num4,(279.5,269.5))
        if sum23==4:
            pygame.draw.polygon(screen,colour_4,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num4,(420.5,269.5))
        if sum24==4:
            pygame.draw.polygon(screen,colour_4,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num4,(561.5,269.5))
        if sum31==4:
            pygame.draw.polygon(screen,colour_4,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num4,(138.5,410.5))
        if sum32==4:
            pygame.draw.polygon(screen,colour_4,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num4,(279.5,410.5))
        if sum33==4:
            pygame.draw.polygon(screen,colour_4,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num4,(420.5,410.5))
        if sum34==4:
            pygame.draw.polygon(screen,colour_4,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num4,(561.5,410.5))
        if sum41==4:
            pygame.draw.polygon(screen,colour_4,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num4,(138.5,551.5))
        if sum42==4:
            pygame.draw.polygon(screen,colour_4,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num4,(279.5,551.5))
        if sum43==4:
            pygame.draw.polygon(screen,colour_4,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num4,(420.5,551.5))
        if sum44==4:
            pygame.draw.polygon(screen,colour_4,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num4,(561.5,551.5))

        #显示8
        if sum11==8:
            pygame.draw.polygon(screen,colour_8,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num8,(138.5,128.5))
        if sum12==8:
            pygame.draw.polygon(screen,colour_8,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num8,(279.5,128.5))
        if sum13==8:
            pygame.draw.polygon(screen,colour_8,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num8,(420.5,128.5))
        if sum14==8:
            pygame.draw.polygon(screen,colour_8,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num8,(561.5,128.5))
        if sum21==8:
            pygame.draw.polygon(screen,colour_8,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num8,(138.5,269.5))
        if sum22==8:
            pygame.draw.polygon(screen,colour_8,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num8,(279.5,269.5))
        if sum23==8:
            pygame.draw.polygon(screen,colour_8,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num8,(420.5,269.5))
        if sum24==8:
            pygame.draw.polygon(screen,colour_8,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num8,(561.5,269.5))
        if sum31==8:
            pygame.draw.polygon(screen,colour_8,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num8,(138.5,410.5))
        if sum32==8:
            pygame.draw.polygon(screen,colour_8,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num8,(279.5,410.5))
        if sum33==8:
            pygame.draw.polygon(screen,colour_8,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num8,(420.5,410.5))
        if sum34==8:
            pygame.draw.polygon(screen,colour_8,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num8,(561.5,410.5))
        if sum41==8:
            pygame.draw.polygon(screen,colour_8,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num8,(138.5,551.5))
        if sum42==8:
            pygame.draw.polygon(screen,colour_8,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num8,(279.5,551.5))
        if sum43==8:
            pygame.draw.polygon(screen,colour_8,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num8,(420.5,551.5))
        if sum44==8:
            pygame.draw.polygon(screen,colour_8,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num8,(561.5,551.5))

        #显示16
        if sum11==16:
            pygame.draw.polygon(screen,colour_16,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num16,(128.5,128.5))
        if sum12==16:
            pygame.draw.polygon(screen,colour_16,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num16,(269.5,128.5))
        if sum13==16:
            pygame.draw.polygon(screen,colour_16,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num16,(410.5,128.5))
        if sum14==16:
            pygame.draw.polygon(screen,colour_16,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num16,(551.5,128.5))
        if sum21==16:
            pygame.draw.polygon(screen,colour_16,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num16,(128.5,269.5))
        if sum22==16:
            pygame.draw.polygon(screen,colour_16,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num16,(269.5,269.5))
        if sum23==16:
            pygame.draw.polygon(screen,colour_16,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num16,(410.5,269.5))
        if sum24==16:
            pygame.draw.polygon(screen,colour_16,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num16,(551.5,269.5))
        if sum31==16:
            pygame.draw.polygon(screen,colour_16,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num16,(128.5,410.5))
        if sum32==16:
            pygame.draw.polygon(screen,colour_16,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num16,(269.5,410.5))
        if sum33==16:
            pygame.draw.polygon(screen,colour_16,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num16,(410.5,410.5))
        if sum34==16:
            pygame.draw.polygon(screen,colour_16,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num16,(551.5,410.5))
        if sum41==16:
            pygame.draw.polygon(screen,colour_16,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num16,(128.5,551.5))
        if sum42==16:
            pygame.draw.polygon(screen,colour_16,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num16,(269.5,551.5))
        if sum43==16:
            pygame.draw.polygon(screen,colour_16,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num16,(410.5,551.5))
        if sum44==16:
            pygame.draw.polygon(screen,colour_16,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num16,(551.5,551.5))

        #显示32
        if sum11==32:
            pygame.draw.polygon(screen,colour_32,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num32,(128.5,128.5))
        if sum12==32:
            pygame.draw.polygon(screen,colour_32,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num32,(269.5,128.5))
        if sum13==32:
            pygame.draw.polygon(screen,colour_32,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num32,(410.5,128.5))
        if sum14==32:
            pygame.draw.polygon(screen,colour_32,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num32,(551.5,128.5))
        if sum21==32:
            pygame.draw.polygon(screen,colour_32,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num32,(128.5,269.5))
        if sum22==32:
            pygame.draw.polygon(screen,colour_32,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num32,(269.5,269.5))
        if sum23==32:
            pygame.draw.polygon(screen,colour_32,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num32,(410.5,269.5))
        if sum24==32:
            pygame.draw.polygon(screen,colour_32,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num32,(551.5,269.5))
        if sum31==32:
            pygame.draw.polygon(screen,colour_32,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num32,(128.5,410.5))
        if sum32==32:
            pygame.draw.polygon(screen,colour_32,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num32,(269.5,410.5))
        if sum33==32:
            pygame.draw.polygon(screen,colour_32,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num32,(410.5,410.5))
        if sum34==32:
            pygame.draw.polygon(screen,colour_32,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num32,(551.5,410.5))
        if sum41==32:
            pygame.draw.polygon(screen,colour_32,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num32,(128.5,551.5))
        if sum42==32:
            pygame.draw.polygon(screen,colour_32,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num32,(269.5,551.5))
        if sum43==32:
            pygame.draw.polygon(screen,colour_32,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num32,(410.5,551.5))
        if sum44==32:
            pygame.draw.polygon(screen,colour_32,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num32,(551.5,551.5))

        #显示64
        if sum11==64:
            pygame.draw.polygon(screen,colour_64,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num64,(128.5,128.5))
        if sum12==64:
            pygame.draw.polygon(screen,colour_64,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num64,(269.5,128.5))
        if sum13==64:
            pygame.draw.polygon(screen,colour_64,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num64,(410.5,128.5))
        if sum14==64:
            pygame.draw.polygon(screen,colour_64,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num64,(551.5,128.5))
        if sum21==64:
            pygame.draw.polygon(screen,colour_64,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num64,(128.5,269.5))
        if sum22==64:
            pygame.draw.polygon(screen,colour_64,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num64,(269.5,269.5))
        if sum23==64:
            pygame.draw.polygon(screen,colour_64,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num64,(410.5,269.5))
        if sum24==64:
            pygame.draw.polygon(screen,colour_64,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num64,(551.5,269.5))
        if sum31==64:
            pygame.draw.polygon(screen,colour_64,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num64,(128.5,410.5))
        if sum32==64:
            pygame.draw.polygon(screen,colour_64,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num64,(269.5,410.5))
        if sum33==64:
            pygame.draw.polygon(screen,colour_64,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num64,(410.5,410.5))
        if sum34==64:
            pygame.draw.polygon(screen,colour_64,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num64,(551.5,410.5))
        if sum41==64:
            pygame.draw.polygon(screen,colour_64,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num64,(128.5,551.5))
        if sum42==64:
            pygame.draw.polygon(screen,colour_64,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num64,(269.5,551.5))
        if sum43==64:
            pygame.draw.polygon(screen,colour_64,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num64,(410.5,551.5))
        if sum44==64:
            pygame.draw.polygon(screen,colour_64,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num64,(551.5,551.5))

        #显示128
        if sum11==128:
            pygame.draw.polygon(screen,colour_128,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num128,(118.5,128.5))
        if sum12==128:
            pygame.draw.polygon(screen,colour_128,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num128,(259.5,128.5))
        if sum13==128:
            pygame.draw.polygon(screen,colour_128,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num128,(400.5,128.5))
        if sum14==128:
            pygame.draw.polygon(screen,colour_128,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num128,(541.5,128.5))
        if sum21==128:
            pygame.draw.polygon(screen,colour_128,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num128,(118.5,269.5))
        if sum22==128:
            pygame.draw.polygon(screen,colour_128,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num128,(259.5,269.5))
        if sum23==128:
            pygame.draw.polygon(screen,colour_128,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num128,(400.5,269.5))
        if sum24==128:
            pygame.draw.polygon(screen,colour_128,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num128,(541.5,269.5))
        if sum31==128:
            pygame.draw.polygon(screen,colour_128,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num128,(118.5,410.5))
        if sum32==128:
            pygame.draw.polygon(screen,colour_128,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num128,(259.5,410.5))
        if sum33==128:
            pygame.draw.polygon(screen,colour_128,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num128,(400.5,410.5))
        if sum34==128:
            pygame.draw.polygon(screen,colour_128,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num128,(541.5,410.5))
        if sum41==128:
            pygame.draw.polygon(screen,colour_128,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num128,(118.5,551.5))
        if sum42==128:
            pygame.draw.polygon(screen,colour_128,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num128,(259.5,551.5))
        if sum43==128:
            pygame.draw.polygon(screen,colour_128,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num128,(400.5,551.5))
        if sum44==128:
            pygame.draw.polygon(screen,colour_128,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num128,(541.5,551.5))

        #显示256
        if sum11==256:
            pygame.draw.polygon(screen,colour_256,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num256,(118.5,128.5))
        if sum12==256:
            pygame.draw.polygon(screen,colour_256,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num256,(259.5,128.5))
        if sum13==256:
            pygame.draw.polygon(screen,colour_256,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num256,(400.5,128.5))
        if sum14==256:
            pygame.draw.polygon(screen,colour_256,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num256,(541.5,128.5))
        if sum21==256:
            pygame.draw.polygon(screen,colour_256,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num256,(118.5,269.5))
        if sum22==256:
            pygame.draw.polygon(screen,colour_256,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num256,(259.5,269.5))
        if sum23==256:
            pygame.draw.polygon(screen,colour_256,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num256,(400.5,269.5))
        if sum24==256:
            pygame.draw.polygon(screen,colour_256,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num256,(541.5,269.5))
        if sum31==256:
            pygame.draw.polygon(screen,colour_256,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num256,(118.5,410.5))
        if sum32==256:
            pygame.draw.polygon(screen,colour_256,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num256,(259.5,410.5))
        if sum33==256:
            pygame.draw.polygon(screen,colour_256,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num256,(400.5,410.5))
        if sum34==256:
            pygame.draw.polygon(screen,colour_256,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num256,(541.5,410.5))
        if sum41==256:
            pygame.draw.polygon(screen,colour_256,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num256,(118.5,551.5))
        if sum42==256:
            pygame.draw.polygon(screen,colour_256,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num256,(259.5,551.5))
        if sum43==256:
            pygame.draw.polygon(screen,colour_256,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num256,(400.5,551.5))
        if sum44==256:
            pygame.draw.polygon(screen,colour_256,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num256,(541.5,551.5))

        #显示512
        if sum11==512:
            pygame.draw.polygon(screen,colour_512,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num512,(118.5,128.5))
        if sum12==512:
            pygame.draw.polygon(screen,colour_512,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num512,(259.5,128.5))
        if sum13==512:
            pygame.draw.polygon(screen,colour_512,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num512,(400.5,128.5))
        if sum14==512:
            pygame.draw.polygon(screen,colour_512,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num512,(541.5,128.5))
        if sum21==512:
            pygame.draw.polygon(screen,colour_512,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num512,(118.5,269.5))
        if sum22==512:
            pygame.draw.polygon(screen,colour_512,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num512,(259.5,269.5))
        if sum23==512:
            pygame.draw.polygon(screen,colour_512,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num512,(400.5,269.5))
        if sum24==512:
            pygame.draw.polygon(screen,colour_512,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num512,(541.5,269.5))
        if sum31==512:
            pygame.draw.polygon(screen,colour_512,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num512,(118.5,410.5))
        if sum32==512:
            pygame.draw.polygon(screen,colour_512,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num512,(259.5,410.5))
        if sum33==512:
            pygame.draw.polygon(screen,colour_512,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num512,(400.5,410.5))
        if sum34==512:
            pygame.draw.polygon(screen,colour_512,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num512,(541.5,410.5))
        if sum41==512:
            pygame.draw.polygon(screen,colour_512,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num512,(118.5,551.5))
        if sum42==512:
            pygame.draw.polygon(screen,colour_512,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num512,(259.5,551.5))
        if sum43==512:
            pygame.draw.polygon(screen,colour_512,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num512,(400.5,551.5))
        if sum44==512:
            pygame.draw.polygon(screen,colour_512,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num512,(541.5,551.5))

        #显示1024
        if sum11==1024:
            pygame.draw.polygon(screen,colour_1024,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num1024,(108.5,128.5))
        if sum12==1024:
            pygame.draw.polygon(screen,colour_1024,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num1024,(249.5,128.5))
        if sum13==1024:
            pygame.draw.polygon(screen,colour_1024,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num1024,(390.5,128.5))
        if sum14==1024:
            pygame.draw.polygon(screen,colour_1024,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num1024,(531.5,128.5))
        if sum21==1024:
            pygame.draw.polygon(screen,colour_1024,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num1024,(108.5,269.5))
        if sum22==1024:
            pygame.draw.polygon(screen,colour_1024,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num1024,(249.5,269.5))
        if sum23==1024:
            pygame.draw.polygon(screen,colour_1024,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num1024,(390.5,269.5))
        if sum24==1024:
            pygame.draw.polygon(screen,colour_1024,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num1024,(531.5,269.5))
        if sum31==1024:
            pygame.draw.polygon(screen,colour_1024,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num1024,(108.5,410.5))
        if sum32==1024:
            pygame.draw.polygon(screen,colour_1024,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num1024,(249.5,410.5))
        if sum33==1024:
            pygame.draw.polygon(screen,colour_1024,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num1024,(390.5,410.5))
        if sum34==1024:
            pygame.draw.polygon(screen,colour_1024,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num1024,(531.5,410.5))
        if sum41==1024:
            pygame.draw.polygon(screen,colour_1024,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num1024,(108.5,551.5))
        if sum42==1024:
            pygame.draw.polygon(screen,colour_1024,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num1024,(249.5,551.5))
        if sum43==1024:
            pygame.draw.polygon(screen,colour_1024,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num1024,(390.5,551.5))
        if sum44==1024:
            pygame.draw.polygon(screen,colour_1024,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num1024,(531.5,551.5))

        #显示2048
        if sum11==2048:
            pygame.draw.polygon(screen,colour_2048,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num2048,(108.5,128.5))
        if sum12==2048:
            pygame.draw.polygon(screen,colour_2048,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num2048,(249.5,128.5))
        if sum13==2048:
            pygame.draw.polygon(screen,colour_2048,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num2048,(390.5,128.5))
        if sum14==2048:
            pygame.draw.polygon(screen,colour_2048,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num2048,(531.5,128.5))
        if sum21==2048:
            pygame.draw.polygon(screen,colour_2048,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num2048,(108.5,269.5))
        if sum22==2048:
            pygame.draw.polygon(screen,colour_2048,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num2048,(249.5,269.5))
        if sum23==2048:
            pygame.draw.polygon(screen,colour_2048,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num2048,(390.5,269.5))
        if sum24==2048:
            pygame.draw.polygon(screen,colour_2048,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num2048,(531.5,269.5))
        if sum31==2048:
            pygame.draw.polygon(screen,colour_2048,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num2048,(108.5,410.5))
        if sum32==2048:
            pygame.draw.polygon(screen,colour_2048,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num2048,(249.5,410.5))
        if sum33==2048:
            pygame.draw.polygon(screen,colour_2048,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num2048,(390.5,410.5))
        if sum34==2048:
            pygame.draw.polygon(screen,colour_2048,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num2048,(531.5,410.5))
        if sum41==2048:
            pygame.draw.polygon(screen,colour_2048,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num2048,(108.5,551.5))
        if sum42==2048:
            pygame.draw.polygon(screen,colour_2048,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num2048,(249.5,551.5))
        if sum43==2048:
            pygame.draw.polygon(screen,colour_2048,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num2048,(390.5,551.5))
        if sum44==2048:
            pygame.draw.polygon(screen,colour_2048,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num2048,(531.5,551.5))

        #显示4096
        if sum11==4096:
            pygame.draw.polygon(screen,colour_4096,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num4096,(108.5,128.5))
        if sum12==4096:
            pygame.draw.polygon(screen,colour_4096,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num4096,(249.5,128.5))
        if sum13==4096:
            pygame.draw.polygon(screen,colour_4096,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num4096,(390.5,128.5))
        if sum14==4096:
            pygame.draw.polygon(screen,colour_4096,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num4096,(531.5,128.5))
        if sum21==4096:
            pygame.draw.polygon(screen,colour_4096,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num4096,(108.5,269.5))
        if sum22==4096:
            pygame.draw.polygon(screen,colour_4096,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num4096,(249.5,269.5))
        if sum23==4096:
            pygame.draw.polygon(screen,colour_4096,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num4096,(390.5,269.5))
        if sum24==4096:
            pygame.draw.polygon(screen,colour_4096,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num4096,(531.5,269.5))
        if sum31==4096:
            pygame.draw.polygon(screen,colour_4096,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num4096,(108.5,410.5))
        if sum32==4096:
            pygame.draw.polygon(screen,colour_4096,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num4096,(249.5,410.5))
        if sum33==4096:
            pygame.draw.polygon(screen,colour_4096,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num4096,(390.5,410.5))
        if sum34==4096:
            pygame.draw.polygon(screen,colour_4096,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num4096,(531.5,410.5))
        if sum41==4096:
            pygame.draw.polygon(screen,colour_4096,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num4096,(108.5,551.5))
        if sum42==4096:
            pygame.draw.polygon(screen,colour_4096,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num4096,(249.5,551.5))
        if sum43==4096:
            pygame.draw.polygon(screen,colour_4096,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num4096,(390.5,551.5))
        if sum44==4096:
            pygame.draw.polygon(screen,colour_4096,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num4096,(531.5,551.5))

        #显示8192
        if sum11==8192:
            pygame.draw.polygon(screen,colour_8192,[(81,81),(216,81),(216,216),(81,216)],0)
            screen.blit(num8192,(108.5,128.5))
        if sum12==8192:
            pygame.draw.polygon(screen,colour_8192,[(222,81),(357,81),(357,216),(222,216)],0)
            screen.blit(num8192,(249.5,128.5))
        if sum13==8192:
            pygame.draw.polygon(screen,colour_8192,[(363,81),(498,81),(498,216),(363,216)],0)
            screen.blit(num8192,(390.5,128.5))
        if sum14==8192:
            pygame.draw.polygon(screen,colour_8192,[(504,81),(639,81),(639,216),(504,216)],0)
            screen.blit(num8192,(531.5,128.5))
        if sum21==8192:
            pygame.draw.polygon(screen,colour_8192,[(81,222),(216,222),(216,357),(81,357)],0)
            screen.blit(num8192,(108.5,269.5))
        if sum22==8192:
            pygame.draw.polygon(screen,colour_8192,[(222,222),(357,222),(357,357),(222,357)],0)
            screen.blit(num8192,(249.5,269.5))
        if sum23==8192:
            pygame.draw.polygon(screen,colour_8192,[(363,222),(498,222),(498,357),(363,357)],0)
            screen.blit(num8192,(390.5,269.5))
        if sum24==8192:
            pygame.draw.polygon(screen,colour_8192,[(504,222),(639,222),(639,357),(504,357)],0)
            screen.blit(num8192,(531.5,269.5))
        if sum31==8192:
            pygame.draw.polygon(screen,colour_8192,[(81,363),(216,363),(216,498),(81,498)],0)
            screen.blit(num8192,(108.5,410.5))
        if sum32==8192:
            pygame.draw.polygon(screen,colour_8192,[(222,363),(357,363),(357,498),(222,498)],0)
            screen.blit(num8192,(249.5,410.5))
        if sum33==8192:
            pygame.draw.polygon(screen,colour_8192,[(363,363),(498,363),(498,498),(363,498)],0)
            screen.blit(num8192,(390.5,410.5))
        if sum34==8192:
            pygame.draw.polygon(screen,colour_8192,[(504,363),(639,363),(639,498),(504,498)],0)
            screen.blit(num8192,(531.5,410.5))
        if sum41==8192:
            pygame.draw.polygon(screen,colour_8192,[(81,504),(216,504),(216,639),(81,639)],0)
            screen.blit(num8192,(108.5,551.5))
        if sum42==8192:
            pygame.draw.polygon(screen,colour_8192,[(222,504),(357,504),(357,639),(222,639)],0)
            screen.blit(num8192,(249.5,551.5))
        if sum43==8192:
            pygame.draw.polygon(screen,colour_8192,[(363,504),(498,504),(498,639),(363,639)],0)
            screen.blit(num8192,(390.5,551.5))
        if sum44==8192:
            pygame.draw.polygon(screen,colour_8192,[(504,504),(639,504),(639,639),(504,639)],0)
            screen.blit(num8192,(531.5,551.5))
        #返回键
        pygame.draw.polygon(screen,BLACK,[(0,75/2),(25,0),(25,25),(50,25),(50,50),(25,50),(25,75)],0)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
    pygame.display.update()
    clock.tick(30)
                    
