test_tuple=('test1',) #원소가 하나인 튜플을 만들 때에는 하나의 원소 뒤에 ,를 입력한다
print(test_tuple)

test_tuple='test1', #튜플의 괄호는 생략이 가능하다
print(test_tuple)
print(type(test_tuple))

test_tuple='test1' #튜플의 ,를 생략하면 str타입으로 인식된다.
print(test_tuple)
print(type(test_tuple))

marx_tuple = 'one' , 'two' , 'three' #튜플에 여러개의 원소를 지정할 때의 , 사용법
print(marx_tuple)
print(type(marx_tuple))

marx_tuple = ('one' , 'two' , 'three') #튜플을 지정할 때의 괄호를 입력시 파이썬은 괄호까지 출력한다.
print(marx_tuple)

