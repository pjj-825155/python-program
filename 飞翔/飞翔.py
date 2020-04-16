import sys,random,pygame,time
from pygame.locals import *
from fly_program import *

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((990,540),0,32)
#设置字体
text=pygame.font.Font("E:/桌面/Python程序/飞翔/字体/simsun.ttc",40)
score=0
#初始化
length,width=40,40
shape=Shape(length,width)
color=Color()
wall=Wall()
statue=Statue(length,width)
pillar=Pillar(120,40,500,40)
pillar_x,pillar_y=0,0
up,down=40,500
#设置窗口标题
pygame.display.set_caption("飞翔")

while True:
    screen.fill(color.BLUE)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_SPACE:
                statue.derection=1
                statue.speed=9
    
    #飞行状态判断
    statue.derection,statue.speed,statue.y=statue.jump(statue.derection,statue.speed,statue.y,up,down)
    #人物
    shape.show(screen,statue.x,statue.y)
    #柱体
    if pillar_x+80==0:
        pillar_x,pillar_y=990,random.randint(50,350)
    if pillar_x-width<=statue.x<=pillar_x+width*2:
        up,down=pillar_y,pillar_y+pillar.height
    else:
        up,down=40,500
    #游戏判输
    if statue.state==-1:
        pygame.quit()
        sys.exit()
    pillar.upward(screen,pillar_x,pillar_y)
    pillar.downward(screen,pillar_x,pillar_y)
    pillar_x-=2
    #地面和天空
    wall.ground(990,40,screen,0,0)
    wall.ground(990,40,screen,0,500)
    #得分
    if statue.x==pillar_x+width*2:
        score+=1
    num=text.render(f"{score}",1,color.BLACK)
    screen.blit(num,(470,40))
    pygame.display.update()
    clock.tick(60)#限制更新频率