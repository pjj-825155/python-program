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
        pygame.draw.polygon(screen,self.GREEN,[(self.x,self.y),(self.x+self.length,self.y),(self.x+self.length,self.y+self.width),(self.x,self.y+self.width)],0)

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
        #游戏状态,1为进行,-1为输
        self.state=1
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
            else:
                self.speed,self.derection=0,0
        if self.derection==1 and self.speed==0:
            self.derection=-1
        if self.derection==1 and self.speed!=0:
            self.y-=self.speed
            self.speed-=1
            if self.y<=up:
                self.y,self.speed=up,0
        if self.derection==0 and self.y+self.width<down:
            self.derection=-1
        if self.y+self.width>=down or self.y<=up:
            self.state=-1
        return self.derection,self.speed,self.y

class Pillar(Color):
    def __init__(self,height,up,down,width):
        Color.__init__(self)
        self.height=height
        self.up=up
        self.down=down
        self.width=width
    def upward(self,screen,x,y):
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.GREEN,[(self.x,self.up),(self.x+self.width*2,self.up),(self.x+self.width*2,self.y),(self.x,self.y)],0)
    def downward(self,screen,x,y):
        self.x=x
        self.y=y
        pygame.draw.polygon(screen,self.GREEN,[(self.x,self.y+self.height),(self.x+self.width*2,self.y+self.height),(self.x+self.width*2,self.down),(self.x,self.down)],0)
