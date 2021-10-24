#format의 이용 문자열중 대괄호를 원하는 위치에 삽입 후 format함수를 이용하여
#객체를 원하는 위치에 배치가 가능하다.
here1 = 'Yeah'
here2 = 'Yeahaaaaa'
print("This is test format here format1 {} here format2 {}".format(here1,here2))
#대괄호 안에 숫자를 0,1 등 순서를 지정하여 삽입이 가능하다 값0은 첫번째 인수 1은 두번째 인수.
print("This is test format here format1 {1} here format2 {0}".format(here1,here2))
#다음과 같이 객체는 위치를 지정 format함수를 이용하여 새로운 내용을 지정해주는 것도 가능하다
print("This is test format here format1 {here2} here format2 {here1}".format(here1='place',here2='lest'))
