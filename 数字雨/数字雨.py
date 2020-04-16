import sys,random,math,pygame,time,os
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,640),FULLSCREEN,32)

col=31

GREEN=(0,col,0)

pygame.display.set_caption("数字雨")

text=pygame.font.Font("字体/simsun.ttc",20)

ch=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0','1','2','3','4','5','6','7','8','9','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']

st=[[0]*128 for i in range(32)]
xs=[[0]*128 for i in range(32)]

m=0
n=0

for x in range(0,32):
    for y in range(0,128):
        st[x][y]=random.choice(ch)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#退出
                pygame.quit()
                sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    screen.fill((0,0,0))
    n=620
    col=255
    for x in range(0,32):
        m=1260
        x=31-x
        for y in range(0,128):
            GREEN=(0,col,0)
            y=63-y
            if x!=0:
                st[x][y]=st[x-1][y]
            else:
                st[x][y]=random.choice(ch)
            xs[x][y]=text.render(st[x][y],1,GREEN)
            screen.blit(xs[x][y],(m,n))
            m-=20
        n-=20
        col-=7
    clock.tick(15)
    pygame.display.update()
