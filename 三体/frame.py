import sys,pygame
from pygame.locals import *
class Color:
    def __init__(self):
        self.BLACK=(0,0,0)
        self.WHITE=(255,255,255)
        self.RED=(255,0,0)
        self.GREEN=(0,255,0)
        self.BLUE=(0,0,255)
        self.YELLOW=(255,255,0)
class Quit:
    def exit(event):
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit() 
class Init:
    def __init__(self,length,width,screen):
        self.length=length
        self.width=width
        self.screen=screen
    def start(self):
        pygame.init()
        pygame.mixer.init()
        clock=pygame.time.Clock()
        screen=pygame.display.set_mode((self.length,self.width),self.screen,32)
        pygame.display.set_caption("天体")
        return clock,screen
class Local:
    def __init__(self,star1,star2,star3):
        self.star1=star1
        self.star2=star2
        self.star3=star3       