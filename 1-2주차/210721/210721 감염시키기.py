import pygame
import random
import itertools
import matplotlib.pyplot as plt
import numpy as np

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("시뮬레이션")

clock = pygame.time.Clock()

infecCnt = []

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


boardValue = [[0]*100 for x in range(0,100)]

hCnt = 0
while hCnt < 100:
    x= random.randrange(0,100)
    y= random.randrange(0,100)
    if boardValue[x][y] == 0:
        boardValue[x][y] = 1
        hCnt = hCnt +1

hCnt = 0
while hCnt <1:
    x = random.randrange(0,100)
    y = random.randrange(0,100)
    if boardValue[x][y] == 0:
        boardValue[x][y] = -1
        hCnt = hCnt +1

def drawBoard():
    SCREEN.fill(WHITE)
    for x in range(0,100):
        if boardValue[x][y] ==1:
            pygame.draw.circle(SCREEN,BLUE,[x * 10+5,y * 10 + 5],5,2)
        elif boardValue[x][y] == -1:
            pygame.draw.circle(SCREEN,RED,[x * 10+5,y * 10 + 5],5,2)
    pygame.display.flip()

drawBoard()

playing = True

while playing:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         playing=False

     if event.type == pygame.KEYUP:
         if event.key == pygame.K_q:
             playing=False

     for x in range(0,100):
         for y in range(0,100):
             if boardValue[x][y] == 1:
                x1 = x + random.randrange(-1,2)
                y1 = y + random.randrange(-1,2)
                if (-1 < x1 < 100) and (-1 < y1 < 100):
                    if boardValue[x][y] == 0:
                        boardValue[x][y] = 0
                        boardValue[x1][y1] = 1
             elif boardValue[x][y] == -1:
                 x1 = x + random.randrange(-1,2)
                 y1 = y + random.randrange(-1,2)
                 if (-1 < x1 <100) and (-1 < y1 < 100):
                     if boardValue[x1][y1] == 0:
                         boardValue[x][y] = 0
                         boardValue[x1][y1] = -1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for x in range(0,100):
        for y in range(0,100):
            if boardValue[x][y] == -1:
                for i in range(4):
                    x1 = x + dx[i]
                    y1 = y + dy[i]
                    if (-1 < x1 < 100) and (-1 < y1 <100):
                        if boardValue[x][y] ==1:
                            boardValue[x1][y1] = -1

    drawBoard()

    clock.tick(20)