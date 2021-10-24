import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("시뮬레이션")

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# 보드
boardValue = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],]

boardValue[3][1] = 1
boardValue[8][8] = -1

SCREEN.fill(WHITE)
x,y = (3,1)
pygame.draw.circle(SCREEN,BLUE,[x*100+50 ,y*100+50],20,2)
x,y = (8,8)
pygame.draw.circle(SCREEN,BLUE,[x*100+50 ,y*100+50],20,2)
pygame.display.flip()

playing = True

while playing:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         playing=False

     if event.type == pygame.KEYUP:
         if event.key == pygame.K_q:
             playing=False

     for x in range(0,10):
         for y in range(0,10):
             if boardValue[x][y] == 1:
                x1 = x + random.randrange(-1,2)
                y1 = y + random.randrange(-1,2)
                if (-1 < x1 < 10) and (-1 < y1 <10):
                    if boardValue[x1][y1] == 0:
                        boardValue[x][y] = 0
                        boardValue[x1][y1] = 1
             elif boardValue[x][y] == -1:
                 x1 = x + random.randrange(-1,2)
                 y1 = y + random.randrange(-1,2)
                 if (-1 < x1 <10) and (-1 < y1 < 10):
                     if boardValue[x1][y1] == 0:
                         boardValue[x][y] = 0
                         boardValue[x1][y1] = -1
     SCREEN.fill(WHITE)
     for x in range(0,10):
         for y in range(0,10):
             if boardValue[x][y] == 1:
                 pygame.draw.circle(SCREEN,BLUE,[x*100+50 , y*100+50],20,2)
             elif boardValue[x][y] == -1:
                 pygame.draw.circle(SCREEN,RED,[x*100+50 , y*100+50],20,2)
    clock.tick(100)
    pygame.display.flip()