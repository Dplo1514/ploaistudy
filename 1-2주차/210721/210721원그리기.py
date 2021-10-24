import pygame

#스크린 전체 크기지정
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#파이게임 초기화
pygame.init()

#스크린 객체 설정
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("시뮬레이션")

#FPS를 위한 CLOCK 생성 (FPS : Frame Per Second)
clock = pygame.time.Clock()

#RGB 변수
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

#좌표 (원이 생성되는 좌표)
coord=(4,4)

#화면을 흰색으로 채움 , x,y좌표 객체지정 , 원그리기 메서드 ,
SCREEN.fill(WHITE)
x,y = coord
pygame.draw.circle(SCREEN, BLUE,[x * 100 + 50 , y * 100 +50],50 ,2)
pygame.display.flip()

playing=True

#반복 while문
while playing:

    #이벤트처리
    for event in pygame.event.get():
        #창의 닫기 버튼 클릭시 게임 종료
        if event.type == pygame.QUIT:
            playing = False
        #이벤트의 종류가 키보드에서 발생한 이벤트인 경우
            #if 키보드에서 q를 눌렀을 때에
                #플레이를 종료한다 False문

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                playing = False

            # 방향키의 위 키를 눌렀을 때에
            #
            elif event.key == pygame.K_UP:
                SCREEN.fill(WHITE)
                x,y = coord
                y = y -1
                coord = (x,y)
                pygame.draw.circle(SCREEN,BLUE,[x * 100 +50,y * 100],50,2)
            elif event.key == pygame.K_DOWN:
                SCREEN.fill(WHITE)
                x,y = coord
                y = y + 1
                coord = (x,y)
                pygame.draw.circle(SCREEN,BLUE,[x * 100 + 50, y * 100],50,2)
            elif event.key == pygame.K_LEFT:
                SCREEN.fill(WHITE)
                x,y = coord
                x = x - 1
                coord = (x,y)
                pygame.draw.circle(SCREEN,BLUE,[x * 100 + 50, y * 100],50,2)
            elif event.key == pygame.K_RIGHT:
                SCREEN.fill(WHITE)
                x,y = coord
                x = x + 1
                coord = (x,y)
                pygame.draw.circle(SCREEN,BLUE,[x * 100 + 50, y * 100],50,2)

    clock.tick(60)
    pygame.display.flip()
