from frame import *
import pygame,math
color=Color()
init=Init(660,660,0)
clock,screen=init.start()
local=Local((330,100),(100,550),(550,550))
#绘制
class Definition:
    def __init__(self,radius):
        self.radius=radius
    def star1(self,screen,local):
        local=(int(local[0]),int(local[1]))
        pygame.draw.circle(screen,color.BLUE,local,self.radius,0)
    def star2(self,screen,local):
        local=(int(local[0]),int(local[1]))
        pygame.draw.circle(screen,color.RED,local,self.radius,0)
    def star3(self,screen,local):
        local=(int(local[0]),int(local[1]))
        pygame.draw.circle(screen,color.GREEN,local,self.radius,0)
    def star(self,screen,local1,local2,local3):
        self.star1(screen,local1)
        self.star2(screen,local2)
        self.star3(screen,local3)
class Vector:
    def __init__(self,a):
        self.a=a
    #通过矢量和方向算出x,y轴上分力
    def vector_hl(self,vector,direction):
        direction=direction%360
        if 270<direction<360:
            direction=360-direction
            vector_high=(-1)*vector*math.sin(direction/180*math.pi)
            vector_lenght=vector*math.cos(direction/180*math.pi)
        elif direction==270:
            vector_high=0-vector
            vector_lenght=0
        elif 180<direction<270:
            direction=direction-180
            vector_high=(-1)*vector*math.sin(direction/180*math.pi)
            vector_lenght=(-1)*vector*math.cos(direction/180*math.pi)
        elif direction==180:
            vector_high=0
            vector_lenght=0-vector
        elif 90<direction<180:
            direction=180-direction
            vector_high=vector*math.sin(direction/180*math.pi)
            vector_lenght=(-1)*vector*math.cos(direction/180*math.pi)
        elif direction==90:
            vector_high=vector
            vector_lenght=0
        elif 0<direction<90:
            vector_high=vector*math.sin(direction/180*math.pi)
            vector_lenght=vector*math.cos(direction/180*math.pi)
        elif direction==0:
            vector_high=0
            vector_lenght=vector
        return vector_high,vector_lenght
    #通过两个力和方向算出合力和方向
    def vector_angle(self,vector1,direction1,vector2,direction2):#角度
        vector1_high,vector1_lenght=self.vector_hl(vector1,direction1)
        vector2_high,vector2_lenght=self.vector_hl(vector2,direction2)
        vector_high=vector1_high+vector2_high
        vector_lenght=vector1_lenght+vector2_lenght
        vector=(vector_high**2+vector_lenght**2)**0.5
        if vector_high>0 and vector_lenght>0:
            direction=math.asin(vector_high/vector)
        elif vector_high>0 and vector_lenght==0:
            direction=90
        elif vector_high>0 and vector_lenght<0:
            direction=180-math.asin(vector_high/vector)
        elif vector_high==0 and vector_lenght<0:
            direction=180
        elif vector_high<0 and vector_lenght<0:
            direction=180+math.asin(abs(vector_high)/vector)
        elif vector_high<0 and vector_lenght==0:
            direction=270
        elif vector_high<0 and vector_lenght>0:
            direction=360-math.asin(abs(vector_high)/vector)
        elif vector_high==0 and vector_lenght>0:
            direction=0
        return vector,direction
#速度和方向
class Speed:
    def __init__(self,speed1,speed2,speed3):
        self.speed1=speed1
        self.speed2=speed2
        self.speed3=speed3
    def speed_angle(self,speed1,direction1,speed2,direction2):#角度
        speed,direction=Vector.vector_angle(speed1,direction1,speed2,direction2)
#质量和方向
class Direction:
    def __init__(self,star1,star2,star3):
        self.star1=star1
        self.star2=star2
        self.star3=star3
    def power_angle(self,power1,direction1,power2,direction2):
        power,direction=Vector.vector_angle(power1,direction1,power2,direction2)