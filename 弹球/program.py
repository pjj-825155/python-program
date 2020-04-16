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
    def __init__(self,screen_size,fps):
        self.screen_size=screen_size
        self.fps=fps
        self.bg=pygame.image.load("E:/桌面/Python程序/弹球/background/background.jpg")
        self.bg=pygame.transform.smoothscale(self.bg,(1584,864))
    def start(self):
        pygame.init()
        pygame.mixer.init()
        clock=pygame.time.Clock()
        screen=pygame.display.set_mode(self.screen_size,FULLSCREEN,32)
        pygame.display.set_caption("弹球")
        return clock,screen
    def background(self,screen):
        screen.blit(self.bg,(0,0))