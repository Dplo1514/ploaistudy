import random #python libarary random 함수 호출

score = 0 #초기 score를 0으로 설정

while True:
    난수 = random.randrange(0,2) #난수가 0 혹은 1로 발생
    컴퓨터입력 = str(난수)

    사용자입력 = input('입력하세요:')
    #'''사용자가 값을 입력할 수 있는 함수
    # 프로그램 상에서 입력하세요 문구 표시

    if 사용자입력 =='q': #사용자가 q를 입력할시 프로그램이 종료
        break

    if 사용자입력 == 컴퓨터입력:
        score = score+1
        print('맞음')
        #사용자가 컴퓨터의 난수를 맞출시 점수 1증가와 맞음 출력

    else:
        score = score-1
        print('틀림')
        #사용자가 컴퓨터의 난수를 맞추지 못할 시 점수 1감소와 틀림 출력

    print('점수:',score) #매번 반복마다 점수:score객체 출력