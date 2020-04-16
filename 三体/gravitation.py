from star import *
definition=Definition(10)
Vector=Vector(1)
speed=Speed(1,1,1)
direction=Direction(180,300,60)
class Gravitation:
    def __init__(self,star1,star2,star3):
        self.G=6.67e-11#N·m²/kg²
        self.star1=star1
        self.star2=star2
        self.star3=star3
    #合力和方向
    def power(self,quality1,quality2,local1,local2):
        redius=abs((local1[0]-local2[0])*1e+12)**2+abs((local1[1]-local2[1])*1e+12)**2
        direction=abs(local2[0]-local1[0])/(abs(local2[0]-local1[0])**2+abs(local2[1]-local1[1])**2)**0.5
        if local2[0]-local1[0]>0 and local2[1]-local1[1]>0:
            direction=direction
        elif local2[0]-local1[0]==0 and local2[1]-local1[1]>0:
            direction=90
        elif local2[0]-local1[0]<0 and local2[1]-local1[1]>0:
            direction=180-direction
        elif local2[0]-local1[0]<0 and local2[1]-local1[1]==0:
            direction=180
        elif local2[0]-local1[0]<0 and local2[1]-local1[1]<0:
            direction=180+direction
        elif local2[0]-local1[0]==0 and local2[1]-local1[1]<0:
            direction=270
        elif local2[0]-local1[0]>0 and local2[1]-local1[1]<0:
            direction=360-direction
        elif local2[0]-local1[0]>0 and local2[1]-local1[1]==0:
            direction=0
        return self.G*quality1*quality2/redius,direction
    #计算坐标影响
    def local_influence(self):
        speed1_high,speed1_lenght=Vector.vector_hl(speed.speed1,direction.star1)
        speed2_high,speed2_lenght=Vector.vector_hl(speed.speed2,direction.star2)
        speed3_high,speed3_lenght=Vector.vector_hl(speed.speed3,direction.star3)
        local.star1=(local.star1[0]+speed1_lenght,local.star1[1]-speed1_high)
        local.star2=(local.star2[0]+speed2_lenght,local.star2[1]-speed2_high)
        local.star3=(local.star3[0]+speed3_lenght,local.star3[1]-speed3_high)
    #计算速度影响
    def speed_influence(self):
        power12,direction12=self.power(self.star1,self.star2,local.star1,local.star2)
        power13,direction13=self.power(self.star1,self.star3,local.star1,local.star3)
        power1,direction1=Vector.vector_angle(power12,direction12,power13,direction13)
        speed.speed1,direction.star1=speed.speed_angle(speed.speed1,direction.star1,(power1/self.star1),direction1)
        power21,direction21=self.power(self.star2,self.star1,local.star2,local.star1)
        power23,direction23=self.power(self.star2,self.star3,local.star2,local.star3)
        power2,direction2=Vector.vector_angle(power21,direction21,power23,direction23)
        speed.speed2,direction.star2=speed.speed_angle(speed.speed2,direction.star2,(power2/self.star2),direction2)
        power31,direction31=self.power(self.star3,self.star1,local.star3,local.star1)
        power32,direction32=self.power(self.star3,self.star2,local.star3,local.star2)
        power3,direction3=Vector.vector_angle(power31,direction31,power32,direction32)
        speed.speed3,direction.star3=speed.speed_angle(speed.speed3,direction.star3,(power3/self.star3),direction3)