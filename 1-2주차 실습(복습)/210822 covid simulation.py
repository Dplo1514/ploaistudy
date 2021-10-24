import random
import pygame
import matplotlib.pyplot as plt

#스크린의 가로 , 세로 객체 지정 후 파이게임 초기화 / SCREEN 객체 지정
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#게임창 이름 설정 , FPS를 위한 CLOCK 생성 FPS : Fream Per Sceond
pygame.display.set_caption("시뮬레이션")
clock = pygame.time.Clock()

#각종 변수
NUMHEALTH = 200
NUMINFECTION = 60
ARRRATIO = 0.1
healthCnt = 0
infeCnt = []
infecntionCoord =[]
arrCoord =[]

#색상객체 생성
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0 , 255 , 0)
RED = (255,0,0)
VIOLET = (255 , 0 , 255)

#보드생성
boardValue = [[0] * 100 for x in range (0,100)]
#보드에 초기인원 10명
hCnt = 0
while hCnt < NUMHEALTH:
    x = random.randrange(0,100)
    y = random.randrange(0,100)
    if boardValue[x][y] ==0:
        boardValue[x][y] =1
        hCnt = hCnt+1

#감염자
hCnt = 0
while hCnt < NUMINFECTION:
    x = random.randrange(0,100)
    y = random.randrange(0,100)
    if boardValue[x][y] ==0:
        boardValue[x][y] =-1
        hCnt = hCnt+1

#화면그리기 함수
def drawboard():
    SCREEN.fill(WHITE)
    global healthCnt
    healthCnt =0
    for x in range(0,100):
        for y in range(0,100):
            if boardValue[x][y] == 1:
                healthCnt = healthCnt + 1
                pygame.draw.circle(SCREEN,BLUE,[x *10 +5, y*10+5] ,5,2)
            elif boardValue[x][y] == -1:
                pygame.draw.circle(SCREEN,RED,[x *10 +5, y*10+5] ,5,2)
            elif boardValue[x][y] == 2:
                healthCnt = healthCnt +1
                pygame.draw.circle(SCREEN,BLUE,[x *10 +5, y*10+5] ,5,2)
                pygame.draw.circle(SCREEN,GREEN,[x *10 +5, y*10+5] ,10,1)
            elif boardValue[x][y] == -2:
                pygame.draw.circle(SCREEN,RED,[x*10 + 5, y*10 +5,],5,2)
                pygame.draw.circle(SCREEN,GREEN,[x*10 + 5, y*10 +5],10,1)
            elif boardValue[x][y] == 9:
                pygame.draw.circle(SCREEN, BLACK, [x * 10 + 5, y * 10 + 5], 5,2)
                pygame.draw.circle(SCREEN, VIOLET,[x * 10 + 5, y * 10 + 5] ,10,1)

    pygame.display.flip()

def moveHuman():
    for x in range(0,100):
        for y in range(0,100):
            hValue = boardValue[x][y]
            if hValue != 0 and hValue !=9:
                loopCnt = 0
                while loopCnt <100:
                    loopCnt = loopCnt + 1
                    x1 = x + random.randrange(-1,2)
                    y1 = y + random.randrange(-1,2)
                    if (-1 < x1 <100) and (-1 < y1 < 100):
                        if boardValue[x1][y1] ==0:
                            boardValue[x][y] =0
                            boardValue[x1][y1] =hValue
                            break
    doInfection()
    drawboard()

#감염인파악
def serachInfection():
    global infectionCoord
    global infeCnt
    infectionCoord = []
    for x in range(0,100):
        for y in range(0,100):
            if boardValue[x][y] == -1 or boardValue[x][y] == -2:
                infectionCoord.append((x,y))
    infeCnt.append(len(infectionCoord))
    return()

#감염
def doInfection():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    serachInfection()
    for (x,y) in infecntionCoord:
        infectionRatio= 0.8
        if boardValue[x][y] == -2:
            infectionRatio = 0.1
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if(-1 < x1 <100) and (-1 , y1 ,100):
                if boardValue[x1][y1] == 1 and random.random() < 0.2 * infectionRatio :
                    boardValue[x1][y1] = -1
                if boardValue[x1][y1] == 2 and random.random() < 0.05 * infectionRatio:
                    boardValue[x1][y1] = -1
    return()

drawboard()
playing = True
turnCnt = 0
arrTurn = 0
unbindTurn = 0
while playing:
    #이벤트처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                playing=False
            if event.key == pygame.K_SPACE:
                moveHuman()
    moveHuman()

    #1초에 60번 빈도로 순환하기
    clock.tick(60)
    if healthCnt < 1:
        playing = False

    arrTurn = arrTurn+1
    if arrTurn >10:
        for x in range(0,100):
            for y in range(0,100):
                if boardValue [x][y] < 0 and random.random() < ARRRATIO :
                    boardValue[x][y] =9
                    arrCoord.append((x,y))
        arrTurn=0

    turnCnt = turnCnt +1
    if turnCnt > 19:
        for x in range(0,100):
            for y in range(0,100):
                if abs(boardValue[x][y] == 2):
                    boardValue[x][y] = int(boardValue[x][y] / 2)
                if abs(boardValue[x][y] == 1 and random.random() < 0.3):
                    boardValue[x][y] = int(boardValue[x][y] * 2)
        turnCnt = 0

    unbindTurn = unbindTurn +1
    if unbindTurn > 15:
        if len(arrCoord) >0:
            ux , uy = arrCoord.pop(0)
            boardValue[ux][uy] =1
        unbindTurn =0
    #print(healthCnt, ':' , infeCnt[-1])
plt.plot(infeCnt)
plt.show()