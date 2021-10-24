#반복문을 생성
while True:
    #stuff 는 사용자로부터 입력값을 받는다 input
    stuff = input("String to capitalize [type q to quit]:")
    #stuff에 q가 입력되면 멈춘다
    if stuff == "q":
        break
    #stuff에 q가 입력되지 않으면 입력값을 대문자로 변환하여 반환한다.
    print(stuff.capitalize())