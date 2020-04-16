import sys,random,math,pygame,time,os
from pygame.locals import *
from jump_program import *

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((990,540),0,32)

length,width=40,40
shape=Shape(length,width)
color=Color()
wall=Wall()
statue=Statue(length,width)
barrier=Barrier(0,500,2)
star=Star(0,375)

#设置窗口标题
pygame.display.set_caption("跳跃")

while True:
    screen.fill(color.BLACK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_SPACE and statue.derection==0:
                statue.derection=1
                statue.speed=15
            if event.key==K_SPACE and star.xlocal-width<=statue.x<=star.xlocal+star.length and star.ylocal-length<=statue.y<=star.ylocal+star.width:
                statue.derection=1
                statue.speed=15
    up,down=0,500
    #产生星星
    if star.xlocal+star.length<0:
        star.xlocal,star.ylocal=990,375
    star.star(screen,star.xlocal,star.ylocal)
    star.xlocal-=6
    #产生刺
    if barrier.xlocal+barrier.button*barrier.num<0:
        barrier.num=random.randint(2,3)
        barrier.xlocal,barrier.ylocal=990,500
    if barrier.num==2:
        barrier.couple(screen,barrier.xlocal,barrier.ylocal)
    elif barrier.num==3:
        barrier.triple(screen,barrier.xlocal,barrier.ylocal)
    barrier.xlocal-=6
    #碰到刺
    if barrier.xlocal-width<=statue.x<=barrier.xlocal+barrier.button*barrier.num:
        up,down=0,460
        statue.down=1
    else:
        up,down=0,500
        statue.down=0
    #状态判断
    statue.derection,statue.speed,statue.y=statue.jump(statue.derection,statue.speed,statue.y,up,down)
    #显示物体
    shape.show(screen,statue.x,statue.y)
    #显示墙
    wall.ground(990,40,screen,0,500)
    pygame.display.update()
    clock.tick(60)#限制更新频率