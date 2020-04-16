import pygame
class Color:
    def __init__(self):
        #颜色初始化
        self.BLACK=(0,0,0)
        self.WHITE=(255,255,255)
        self.RED=(255,0,0)
        self.GREEN=(0,255,0)
        self.BLUE=(0,0,255)
        self.YELLOW=(255,255,0)
        self.GOLD=(255,215,0)

class Shape(Color):
    def __init__(self,length,width):
        Color.__init__(self)
        #长宽初始化
        self.length=length
        self.width=width
    def show(self,screen,x,y):
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.WHITE,[(self.x,self.y),(self.x+self.length,self.y),(self.x+self.length,self.y+self.width),(self.x,self.y+self.width)],0)

class Wall(Color):
    def __init__(self):
        Color.__init__(self)
    def ground(self,length,width,screen,x,y):
        self.length=length
        self.width=width
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.BLUE,[(self.x,self.y),(self.x+self.length,self.y),(self.x+self.length,self.y+self.width),(self.x,self.y+self.width)],0)

class Barrier(Color):
    def __init__(self,x,y,num):
        Color.__init__(self)
        self.xlocal=x
        self.ylocal=y
        self.num=num
        self.button=30
        self.height=40
    def triangle(self,screen,x,y):
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.BLUE,[(self.x,self.y),(self.x+self.button,self.y),(self.x+self.button/2,self.y-self.height)],0)
    def couple(self,screen,x,y):
        self.triangle(screen,x,y)
        self.triangle(screen,x+self.button,y)
    def triple(self,screen,x,y):
        self.triangle(screen,x,y)
        self.triangle(screen,x+self.button,y)
        self.triangle(screen,x+self.button*2,y)

class Star(Color):
    def __init__(self,x,y):
        Color.__init__(self)
        self.xlocal=x
        self.ylocal=y
        self.length=40
        self.width=40
    def star(self,screen,x,y):
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.GOLD,[(self.x,self.y+self.width/4),(self.x+self.length,self.y+self.width/4),(self.x+self.length/2,self.y+self.width)],0)
        pygame.draw.polygon(screen,self.GOLD,[(self.x,self.y+self.width*3/4),(self.x+self.length,self.y+self.width*3/4),(self.x+self.length/2,self.y)],0)

class Statue(Shape):
    def __init__(self,length,width):
        Shape.__init__(self,length,width)
        #1为向上,0为静止,-1为下落
        self.derection=0
        #下落速度
        self.speed=0
        #坐标
        self.x=350
        self.y=230
        #0位可以踩,1为不能踩
        self.down=0
    def jump(self,derection,speed,y,up,down):
        self.derection=derection
        self.speed=speed
        self.y=y
        if self.derection==-1:
            if self.y+self.width<down:
                self.speed+=0.5
                self.y+=self.speed
            if self.y+self.width>=down:
                self.y=down-self.width
                self.derection,self.speed=0,0
        if self.derection==1 and self.speed==0:
            self.derection=-1
        if self.derection==1 and self.y+self.width>down:
            self.y=down-self.width
            self.derection,self.speed=0,0
        if self.derection==1 and self.speed!=0:
            self.y-=self.speed
            self.speed-=1
            if self.y<up:
                self.y=up
                self.derection,self.speed=0,0
        if self.derection==0 and self.y+self.width<down:
            self.derection=-1
        if self.derection==0 and self.y+self.width>down:
            self.y=down-self.width
        if self.y+self.width==down and self.down==1:
            pygame.quit()
            sys.exit()
        return self.derection,self.speed,self.y