# def do_nothing(): #매개변수가 없는 함수 정의 ()안에는 파라미터가 들어감
#     pass

# def make_a_sound(): #매개변수가 없는 함수 정의
#     print('quack')   #함수 내 코드
# make_a_sound()        #함수 호출

# def agreee(): #agreee 함수정의
#     return True   #함수 내 코드의 값은 참이다
# if agreee():  #만약 함수가 참이면
#     print('Splendid!')    #텍스트를 출력하라
# else:
#     print('That was unexpected!') #값이 거짓이면 해당 텍스트를 출력하라

# def echo(anything): #echo 함수에 anything 매개변수 정의
#     return anything + '' + anything   #매개변수 사이에 공백을 넣어 리턴
# print(echo('Rumplestilltskin'))   #함수 호출 및 리턴값 확인
                                        #함수로 전달한 값은 인수라고 부르며 인수와 함수를 호출하면 인수의 값은 함수내의 해당하는 매개변수에 복사

def commentary(color):
    if color == 'red':
        return ('red')
    elif color == 'blue':
        return ('blue')
    elif color == 'green':
        return ('green')
    else:
        return "Ive never heard of the color " + color + "."

comment = commentary('purple')
# blue 값을 color 매개변수에 할당
# if-elif-else문을 실행 문자열 반환
# 호출자는 반환된 문자열을 comment 변수에 할당

print(comment)


