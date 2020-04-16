import sys,pygame,time
from pygame.locals import *
pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((900,700),0,32)
#定义颜色的RGB参数
WHITE=(255,255,255)
BLACK=(0,0,0)
#设置窗口标题
pygame.display.set_caption("生命游戏")
#设置字体
#界面字体
text_jie=pygame.font.Font("字体/simsun.ttc",50)
#生命字体
text=pygame.font.Font("字体/simsun.ttc",20)
#生命
live=text.render("■",1,WHITE)
die=text.render("□",1,WHITE)
#文字
start=text_jie.render("开始",1,WHITE)
cell_restart=0
while True:
    #初始化
    #屏幕初始化
    screen.fill(BLACK)
    #生命初始化
    if cell_restart==0:
        cell=[[0 for i in range(0,45)] for j in range(0,32)]
        cell_restart=1
    game_start=0
    #界面
    for x in range(0,32):
        for y in range(0,45):
            if cell[x][y]==0:
                screen.blit(die,(y*20,x*20))
            if cell[x][y]==1:
                screen.blit(live,(y*20,x*20))
    #开始
    screen.blit(start,(400,645))
    #监视键盘
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            m,n=pygame.mouse.get_pos()
            if 400<m<500 and 645<n<695:
                game_start=1
                cell_restart=0
            if 0<m<900 and 0<n<640:
                if cell[int(n/20)][int(m/20)]==0:
                    cell[int(n/20)][int(m/20)]=1
                #elif cell[int(n/20)][int(m/20)]==1:
                    #cell[int(n/20)][int(m/20)]=0
            m=450
            n=670
    pygame.display.update()
    clock.tick(30)
    
    while game_start:
        #界面
        screen.fill(BLACK)
        for x in range(0,32):
            for y in range(0,45):
                if cell[x][y]==0:
                    screen.blit(die,(y*20,x*20))
                if cell[x][y]==1:
                    screen.blit(live,(y*20,x*20))
        #监视键盘
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    game_start=0
                    
        for x in range(0,32):
            for y in range(0,45):
                #左上
                try:
                    if cell[x-1][y-1]==1:
                        cell_ul=1
                    else:
                        cell_ul=0
                except:
                    cell_ul=0
                #中上
                try:
                    if cell[x][y-1]==1:
                        cell_um=1
                    else:
                        cell_um=0
                except:
                    cell_um=0
                #右上
                try:
                    if cell[x+1][y-1]==1:
                        cell_ur=1
                    else:
                        cell_ur=0
                except:
                    cell_ur=0
                #左中
                try:
                    if cell[x-1][y]==1:
                        cell_lm=1
                    else:
                        cell_lm=0
                except:
                    cell_lm=0
                #右中
                try:
                    if cell[x+1][y-1]==1:
                        cell_rm=1
                    else:
                        cell_rm=0
                except:
                    cell_rm=0
                #左下
                try:
                    if cell[x-1][y+1]==1:
                        cell_ld=1
                    else:
                        cell_ld=0
                except:
                    cell_ld=0
                #下中
                try:
                    if cell[x][y+1]==1:
                        cell_md=1
                    else:
                        cell_md=0
                except:
                    cell_dm=0
                #右下
                try:
                    if cell[x+1][y+1]==1:
                        cell_rd=1
                    else:
                        cell_rd=0
                except:
                    cell_rd=0
                cell_around=cell_ul+cell_um+cell_ur+cell_lm+cell_rm+cell_ld+cell_md+cell_rd
                if cell_around==3:
                    cell[x][y]=1
                elif cell_around==2:
                    cell[x][y]=cell[x][y]
                else:
                    cell[x][y]=0
    
        pygame.display.update()
        clock.tick(1)
    
