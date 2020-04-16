import sys,random,math,pygame,time,os
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((860,720),FULLSCREEN,32)


#定义白、黑、红、绿、蓝、黄的RGB参数 
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

#设置窗口标题
pygame.display.set_caption("东方打飞机")

#加载音乐
pygame.mixer.music.load(r'背景音乐/上海アリス幻樂団 - 輝く針の小人族 .mp3')
pygame.mixer.music.set_volume(0.2)#设置音量
pygame.mixer.music.play()

#设置字体
text=pygame.font.Font("字体/simsun.ttc",20)
text_df=text.render("得分:",1,BLACK)
start=text.render("开始游戏",1,WHITE)
end=text.render("游戏结束",1,WHITE)
restart=text.render("重新开始",1,WHITE)
jie_shao0=text.render("控制方向",1,RED)
jie_shao1=text.render("W",1,RED)
jie_shao2=text.render("ASD",1,RED)
jie_shao3=text.render("↑",1,RED)
jie_shao4=text.render("←↓→",1,RED)
jie_shao5=text.render("攻击",1,RED)
jie_shao6=text.render("Z或J",1,RED)
jie_shao7=text.render("人物身上有一个黄色的判定点",1,RED)
jie_shao8=text.render("只有碰到黄色判定点才会死亡",1,RED)
jie_shao9=text.render("人物子弹最低为一个，最高为四个",1,RED)
jie_shao10=text.render("当人物子弹数高于一个时",1,RED)
jie_shao11=text.render("碰到敌机不会死亡",1,RED)
jie_shao12=text.render("但子弹数量会减一",1,RED)
jie_shao13=text.render("生成的导弹不可被摧毁",1,RED)
jie_shao14=text.render("按空格可以暂停游戏",1,RED)

#设置背景
bg=pygame.image.load("背景图片/背景.jpg").convert()#不透明
bg=pygame.transform.smoothscale(bg,(860,720))
screen.blit(bg,(0,0))

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

#加载敌方
dd1=pygame.image.load("敌方/敌方1.png").convert_alpha()#透明
dd1=pygame.transform.smoothscale(dd1,(50,150))
dd2=pygame.image.load("敌方/敌方2.png").convert_alpha()#透明
dd2=pygame.transform.smoothscale(dd2,(50,150))
dd3=pygame.image.load("敌方/敌方3.png").convert_alpha()#透明
dd3=pygame.transform.smoothscale(dd3,(50,150))

dj1=pygame.image.load("敌方/鸡.png").convert_alpha()#透明
dj1=pygame.transform.smoothscale(dj1,(64,64))
dj2=pygame.image.load("敌方/水母.png").convert_alpha()#透明
dj2=pygame.transform.smoothscale(dj2,(64,64))

#加载暂停键和开始键
k_s=pygame.image.load("控制键/开始键.png").convert_alpha()#透明
k_s=pygame.transform.smoothscale(k_s,(50,50))
z_t=pygame.image.load("控制键/暂停键.png").convert_alpha()#透明
z_t=pygame.transform.smoothscale(z_t,(50,50))

while True:
    #游戏数值初始化
    #记录人物坐标
    x=320
    y=640

    #记录子弹
    zi_dan_num=1
    zi_dan_x=[0]*300
    zi_dan_y=[0]*300
    ge_shu=1#分为1到4
    jie_ji1=0
    jie_ji2=0
    jie_ji3=0

    #记录敌方
    df_x=[0]*10
    df_y=[0]*10
    df_num=0
    df_sum=[0]*10
    ji_zhong=[0]*10
    blood=[0]*10
    #出现速度
    sc_speed=360
    #前进速度
    qj_speed=1
    #击毁数
    ji_hui_num=0
    #导弹
    dao_dan_x=[0]*5
    dao_dan_y=[0]*5

    #记录类型
    rw=rw1#人物
    zd=zd1#人物子弹
    dj=dj1#敌机
    dd=dd1#导弹

    #记录鼠标坐标
    m=0
    n=0

    #记录游戏循环次数
    num=0
    shi_jian=0
    #记录状态
    flag=0
    zan_ting=0
    screen.blit(bg,(0,0))#画背景
    screen.blit(start,(400,350))#游戏开始
    screen.blit(jie_shao7,(310,380))
    screen.blit(jie_shao8,(310,400))
    screen.blit(jie_shao9,(290,420))
    screen.blit(jie_shao10,(330,440))
    screen.blit(jie_shao11,(365,460))
    screen.blit(jie_shao12,(365,480))
    screen.blit(jie_shao13,(345,500))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m,n = pygame.mouse.get_pos()
            if 400<=m<=480 and 350<=n<=370:
                m=0
                n=0
                flag=1
    while flag==1:
        if pygame.mixer.music.get_busy()==False:#循环播放歌曲
            pygame.mixer.music.play()

        screen.blit(bg,(0,0))#画背景
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#退出
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_SPACE:
                    zan_ting=1
                    screen.blit(k_s,(810,0))
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m,n = pygame.mouse.get_pos()
                if 810<=m<=860 and 0<=n<=50:#暂停
                    zan_ting=1
                    m=0
                    n=0
                    screen.blit(k_s,(810,0))
                    pygame.display.update()

        #暂停后开始
        while zan_ting==1:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#退出
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        zan_ting=0
                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    m,n = pygame.mouse.get_pos()
                    if 810<=m<=860 and 0<=n<=50:
                        m=0
                        n=0
                        zan_ting=0
                        break
            
        key_pressed=pygame.key.get_pressed()#监视方向
        if key_pressed[K_w] or key_pressed[K_UP]:
            if y!=0:
                y-=2
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            if y<=640:
                y+=2
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            if x>=200:
                x-=2
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            if x!=640:
                x+=2
            
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

        #发射子弹           
        if key_pressed[K_j] or key_pressed[K_z]:
            if zi_dan_num>=280:#子弹计数清零
                zi_dan_num=0
            while zi_dan_x[zi_dan_num]!=0:
                zi_dan_num+=1
            #一次发射子弹个数
            if ge_shu==1:
                zi_dan_x[zi_dan_num]=x+25#子弹赋坐标
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
            if ge_shu==2:
                zi_dan_x[zi_dan_num]=x+15
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x+35
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
            if ge_shu==3:
                zi_dan_x[zi_dan_num]=x+25
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x-10
                zi_dan_y[zi_dan_num]=y+30
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x+60
                zi_dan_y[zi_dan_num]=y+30
                zi_dan_num+=1
            if ge_shu==4:
                zi_dan_x[zi_dan_num]=x+15
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x+35
                zi_dan_y[zi_dan_num]=y-15
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x-10
                zi_dan_y[zi_dan_num]=y+30
                zi_dan_num+=1
                zi_dan_x[zi_dan_num]=x+60
                zi_dan_y[zi_dan_num]=y+30
                zi_dan_num+=1

        #子弹前移        
        for i in range(0,300):
            if zi_dan_y[i]<=0:
                zi_dan_x[i]=0
                zi_dan_y[i]=0
            #判断子弹与敌方飞机碰撞
            for k in range(0,10):
                if zi_dan_x[i]<=(df_x[k]+64) and (zi_dan_x[i]+10)>=df_x[k]:
                    if zi_dan_y[i]<=(df_y[k]+64) and (zi_dan_y[i]+30)>=df_y[k]:
                        if zi_dan_x[i]!=0 or zi_dan_y[i]!=0 or df_x[k]!=0 or df_y[k]!=0:
                            zi_dan_x[i]=0
                            zi_dan_y[i]=0
                            blood[k]-=1
                            ji_zhong[k]+=1
                        
            if zi_dan_y[i]!=0:
                screen.blit(zd,(zi_dan_x[i],zi_dan_y[i]))
                zi_dan_y[i]-=15
        
        #敌方飞机移动和销毁
        for i in range(0,10):
            #前进一格
            if df_x[i]!=0:
                df_y[i]+=qj_speed
                screen.blit(df_sum[i],(df_x[i],df_y[i]))
                pygame.draw.rect(screen,RED,[df_x[i]+7,df_y[i]+64,50-(100-blood[i])/2,5],0)
            #击中数量到达100消失，击毁数量加一
            if ji_zhong[i]>=100:
                df_x[i]=0
                df_y[i]=0
                ji_zhong[i]=0
                ji_hui_num+=1
            #前进到最后消失
            if df_y[i]>=720:
                df_x[i]=0
                df_y[i]=0
            #判定点与敌机碰撞
            if df_x[i]!=0:
                if (x+30)>=df_x[i] and (x+20)<=(df_x[i]+64):
                    if (y+60)>=df_y[i] and (y+50)<=(df_y[i]+64):
                        if ge_shu==1:
                            flag=0
                            break
                        else:
                            df_x[i]=0
                            df_y[i]=0
                            ge_shu-=1
        
        #生成敌方飞机
        if num>=sc_speed:
            num=0
            if df_num==10:
                df_num=0
            df_sum[df_num]=random.randint(1,2)#生成随机数
            df_x[df_num]=random.randint(200,636)
            df_y[df_num]=0
            blood[df_num]=100
            ji_zhong[df_num]=0
            if df_sum[df_num]==1:
                df_sum[df_num]=dj1
            if df_sum[df_num]==2:
                df_sum[df_num]=dj2
            screen.blit(df_sum[df_num],(df_x[df_num],df_y[df_num]))
            df_num+=1

        #生成导弹
        if shi_jian%1200==0 and shi_jian!=0:
            dd_sum=random.randint(1,3)
            if dd_sum==1:
                dd=dd1
            if dd_sum==2:
                dd=dd2
            if dd_sum==3:
                dd=dd3
            dao_dan_x[0]=random.randint(200,250)
            dao_dan_y[0]=-50
            dao_dan_x[1]=dao_dan_x[0]+100
            dao_dan_y[1]=-50
            dao_dan_x[2]=dao_dan_x[1]+100
            dao_dan_y[2]=-50
            dao_dan_x[3]=dao_dan_x[2]+100
            dao_dan_y[3]=-50
            dao_dan_x[4]=dao_dan_x[3]+100
            dao_dan_y[4]=-50

        #导弹前进
        if dao_dan_x[0]!=0:
            dao_dan_y[0]+=1
            if (x+30)>=dao_dan_x[0] and (x+20)<=(dao_dan_x[0]+50):
                if (y+60)>=dao_dan_y[0] and (y+50)<=(dao_dan_y[0]+150):
                    if ge_shu==1:
                        flag=0
                        break
                    else:
                        dao_dan_x[0]=0
                        dao_dan_y[0]=0
                        ge_shu-=1
            screen.blit(dd,(dao_dan_x[0],dao_dan_y[0]))
        if dao_dan_x[1]!=0:
            dao_dan_y[1]+=1
            if (x+30)>=dao_dan_x[1] and (x+20)<=(dao_dan_x[1]+50):
                if (y+60)>=dao_dan_y[1] and (y+50)<=(dao_dan_y[1]+150):
                    if ge_shu==1:
                        flag=0
                        break
                    else:
                        dao_dan_x[1]=0
                        dao_dan_y[1]=0
                        ge_shu-=1
            screen.blit(dd,(dao_dan_x[1],dao_dan_y[1]))
        if dao_dan_x[2]!=0:
            dao_dan_y[2]+=1
            if (x+30)>=dao_dan_x[2] and (x+20)<=(dao_dan_x[2]+50):
                if (y+60)>=dao_dan_y[2] and (y+50)<=(dao_dan_y[2]+150):
                    if ge_shu==1:
                        flag=0
                        break
                    else:
                        dao_dan_x[2]=0
                        dao_dan_y[2]=0
                        ge_shu-=1
            screen.blit(dd,(dao_dan_x[2],dao_dan_y[2]))
        if dao_dan_x[3]!=0:
            dao_dan_y[3]+=1
            if (x+30)>=dao_dan_x[3] and (x+20)<=(dao_dan_x[3]+50):
                if (y+60)>=dao_dan_y[3] and (y+50)<=(dao_dan_y[3]+150):
                    if ge_shu==1:
                        flag=0
                        break
                    else:
                        dao_dan_x[3]=0
                        dao_dan_y[3]=0
                        ge_shu-=1
            screen.blit(dd,(dao_dan_x[3],dao_dan_y[3]))
        if dao_dan_x[4]!=0:
            dao_dan_y[4]+=1
            if (x+30)>=dao_dan_x[4] and (x+20)<=(dao_dan_x[4]+50):
                if (y+60)>=dao_dan_y[4] and (y+50)<=(dao_dan_y[4]+150):
                    if ge_shu==1:
                        flag=0
                        break
                    else:
                        dao_dan_x[4]=0
                        dao_dan_y[4]=0
                        ge_shu-=1
            screen.blit(dd,(dao_dan_x[4],dao_dan_y[4]))

        #导弹销毁
        if dao_dan_y[4]==720:
            dao_dan_x=[0]*5
            dao_dan_y=[0]*5
    
        #加快生成速度
        if df_num==10:
            if sc_speed>=240:
                sc_speed-=5

        #升级子弹
        if ji_hui_num==50 and jie_ji1==0:
            if ge_shu<4:
                ge_shu+=1
                jie_ji1=1
        if ji_hui_num==200 and jie_ji2==0:
            if ge_shu<4:
                ge_shu+=1
                jie_ji2=1
        if ji_hui_num%200==0 and ji_hui_num!=0 and jie_ji3==0:
            if ge_shu<4:
                ge_shu+=1
                jie_ji3=1
        if ji_hui_num%200==199:
            jie_ji3=0
          
        screen.blit(rw,(x,y))#画人物
        screen.blit(pd,(x+20,y+50))#画判定点
        text_df=text.render("得分:%d"%ji_hui_num,1,WHITE)
        screen.blit(text_df,(710,100))#画得分
        
        #玩法介绍
        screen.blit(jie_shao0,(60,560))
        screen.blit(jie_shao1,(90,580))
        screen.blit(jie_shao2,(80,600))
        screen.blit(jie_shao3,(85,620))
        screen.blit(jie_shao4,(65,640))
        screen.blit(jie_shao5,(75,660))
        screen.blit(jie_shao6,(80,680))
        screen.blit(jie_shao14,(10,540))

        #绘制暂停键
        screen.blit(z_t,(810,0))

        #分割线
        #右侧
        pygame.draw.aaline(screen,BLACK,(701,0),(701,720),1)
        #左侧
        pygame.draw.aaline(screen,BLACK,(199,0),(199,720),1)
        
        pygame.display.flip()#刷新绘制线条
        pygame.display.update()
        clock.tick(120)#限制更新频率
        num+=1
        shi_jian+=1
        
    pygame.display.update()
