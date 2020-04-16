import program
import math
import pygame
color=program.Color()
init=program.Init(screen_size=(1584,864),fps=60)
clock,screen=init.start()
class Ball:
    def __init__(self,size,local):
        self.size=size
        self.local=local
        self.direction=0
        self.flag=1
        self.tail_list=[self.local]*10
        self.tail_image=pygame.image.load("E:/桌面/Python程序/弹球/effects/fire.png")
        self.tail_flag=0
        self.crash_effects=-1
        self.local_list=[]*2
        self.circle=[0]*36
        for i in range(0,360,10):
            self.circle[i//10]=pygame.image.load(f"E:/桌面/Python程序/弹球/ball/pao{i}.png")
            #self.circle[i//10]=pygame.image.load(f"E:/桌面/Python程序/弹球/ball/pao{i}.png")
            self.circle[i//10]=pygame.transform.smoothscale(self.circle[i//10],(self.size*2,self.size*2))
        self.fire=[0]*9
        for i in range(0,9):
            self.fire[i]=pygame.image.load(f"E:/桌面/Python程序/弹球/fire/fire{i}.png")
            self.fire[i]=pygame.transform.smoothscale(self.fire[i],(self.size*2,self.size*2))
    def effects(self,local):
        for temp in range(len(self.local_list)):
            screen.blit(self.fire[self.local_list[temp][1]//3],self.local_list[temp][0])
            self.local_list[temp][1]+=1
            if self.local_list[temp][1]==24:
                del self.local_list[temp]
    def tail(self):
        for i in range(10):
            tail_image=pygame.transform.smoothscale(self.tail_image,((i+1)*5,(i+1)*5))
            screen.blit(tail_image,self.tail_list[i])
            if i!=9 and self.tail_flag==0:
                self.tail_list[i]=self.tail_list[i+1]
        self.tail_list[9]=(self.local[0]-self.size,self.local[1]-self.size)
        self.tail_flag+=1
        if self.tail_flag==2:
            self.tail_flag=0
    def show(self):
        if self.direction==360:
            self.direction=0
        screen.blit(self.circle[self.direction//10],(int(self.local[0]-self.size),int(self.local[1])-self.size))
        if self.flag==1:
            self.direction+=10
        elif self.flag==-1:
            if self.direction==0:
                self.direction=360
            self.direction-=10
    def move(self):
        speed=vector.speed/init.fps
        direction=vector.direction%360
        if 270<direction<360:
            direction=360-direction
            vector_high=(-1)*speed*math.sin(direction/180*math.pi)
            vector_lenght=speed*math.cos(direction/180*math.pi)
        elif direction==270:
            vector_high=0-speed
            vector_lenght=0
        elif 180<direction<270:
            direction=direction-180
            vector_high=(-1)*speed*math.sin(direction/180*math.pi)
            vector_lenght=(-1)*speed*math.cos(direction/180*math.pi)
        elif direction==180:
            vector_high=0
            vector_lenght=0-speed
        elif 90<direction<180:
            direction=180-direction
            vector_high=speed*math.sin(direction/180*math.pi)
            vector_lenght=(-1)*speed*math.cos(direction/180*math.pi)
        elif direction==90:
            vector_high=speed
            vector_lenght=0
        elif 0<direction<90:
            vector_high=speed*math.sin(direction/180*math.pi)
            vector_lenght=speed*math.cos(direction/180*math.pi)
        elif direction==0:
            vector_high=0
            vector_lenght=speed
        self.local=(list(self.local)[0]+vector_lenght,list(self.local)[1]-vector_high)
    def crash(self):
        if self.local==(self.size,self.size):
            vector.direction+=180
            self.flag=0-self.flag
        elif self.local==(init.screen_size[0]-self.size,self.size):
            vector.direction+=180
            self.flag=0-self.flag
        elif self.local==(self.size,init.screen_size[1]-self.size):
            vector.directio-=180
            self.flag=0-self.flag
        elif self.local==(init.screen_size[0]-self.size,init.screen_size[1]-self.size):
            vector.direction-=180
            self.flag=0-self.flag
        elif self.local[0]<=self.size:
            if 90<vector.direction<=180:
                vector.direction=180-vector.direction
                self.flag=0-self.flag
            elif 180<vector.direction<270:
                vector.direction=540-vector.direction
                self.flag=0-self.flag
            self.crash_effects=0
            self.local_list.append([(self.local[0]-self.size*2,self.local[1]-self.size),self.crash_effects])
            self.crash_effects=-1
        elif self.local[0]>=init.screen_size[0]-self.size:
            if 0<vector.direction<=90:
                vector.direction=180-vector.direction
                self.flag=0-self.flag
            elif 270<vector.direction<360:
                vector.direction=540-vector.direction
                self.flag=0-self.flag
            self.crash_effects=0
            self.local_list.append([(self.local[0],self.local[1]-self.size),self.crash_effects])
            self.crash_effects=-1
        elif self.local[1]<=self.size:
            if 0<vector.direction<180:
                vector.direction=360-vector.direction
                self.flag=0-self.flag
            self.crash_effects=0
            self.local_list.append([(self.local[0]-self.size,self.local[1]-self.size*2),self.crash_effects])
            self.crash_effects=-1
        elif self.local[1]>=init.screen_size[1]-self.size:
            if 180<vector.direction<360:
                vector.direction=360-vector.direction
                self.flag=0-self.flag
            self.crash_effects=0
            self.local_list.append([(self.local[0]-self.size,self.local[1]),self.crash_effects])
            self.crash_effects=-1
class Vector:
    def __init__(self,direction,speed):
        self.direction=direction
        self.speed=speed
ball=Ball(size=50,local=(792,432))
vector=Vector(direction=60,speed=240)
while True:
    init.background(screen)
    for event in pygame.event.get():
        program.Quit.exit(event)
    ball.move()
    ball.crash()
    ball.tail()
    ball.show()
    ball.effects((ball.local[0]-ball.size,ball.local[1]-ball.size*2))
    pygame.display.update()
    clock.tick(init.fps)