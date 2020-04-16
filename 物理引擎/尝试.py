import random

import pygame
from pygame.key import *
from pygame.locals import *
from pygame.color import *

import pymunk
import pymunk.pygame_util

# pymunk初始化
space = pymunk.Space()        # 空间
space.gravity = (0.0, -900.0) # 设置重力

# pygame初始化
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
# 在pygame上创建画板
draw_options = pymunk.pygame_util.DrawOptions(screen)

FPS = 60
balls = []  # 所有的球
ticks_to_next_ball = 10  # 多少帧后出现下一个球
exact = 10  # 一帧计算几次

static_body = space.static_body
static_lines = [
	pymunk.Segment(static_body, (111.0, 280.0), (407.0, 246.0), 0.0),
	pymunk.Segment(static_body, (407.0, 246.0), (407.0, 343.0), 0.0)
]
for line in static_lines:
    line.elasticity = 0.95  # 弹性系数 0-1
    line.friction = 0.9     # 摩擦系数 0-1
space.add(static_lines)
