import random #랜덤라이브러리 호출

시도 = 0
난수 = random.randrange(0,101) #컴퓨터가 1~100까지의 난수를 입력
컴퓨터입력 = str(난수)

while True:
    사용자입력 = input('입력하세요')
    if 사용자입력 < 컴퓨터입력:
        print('작다')
    else:
        시도 = 시도+1
    if 사용자입력 > 컴퓨터입력:
        print('크다')
    else:
        시도 = 시도+1
    if 사용자입력 == 컴퓨터입력:
        print("정답",시도)


    #사용자입력이 컴퓨터입력보다 작을시 '크다'출력 후 반복
#사용자 입력이 컴퓨터입력보다 클시 '작다' 출력 후 반복
#위 과정을 숫자를 맞출 때 까지 반복하고 몇번만에 맞췄는지 출력