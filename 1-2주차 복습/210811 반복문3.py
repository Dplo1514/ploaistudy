while True:
    
    #value 는 사용자로부터 입력값을 받는다
    value = input("integer,please [q to quit]:")
    #value에 q가 입력되면 프로그램이 종료.
    if value == "q":
        break

    #number객체를 이용하여 value에 int값을 지정해준다.
    number = int(value)

    #number (value)에 사용자가 int값을 입력했을 때에 입력값을 2로 나눴을 때 홀수이면
    if number %2 == 1:

    #계속 진행
        continue

    #나머지가 짝수이면 입력 값을 제곱하여 반환한다.
    print(number,"squared is",number * number)

