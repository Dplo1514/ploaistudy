print('#tuple 함수는 다른 객체를 튜플로 만들어준다.')
a_list = [1,2,3,4,5]
print(tuple(a_list))

print(sep="\n")

print("#튜플은 불변객체이므로 기존 튜플을 변경할 수 없고 문자열과 같이 결합하여 새 튜플을 만들어야함")
t1 = ('one' , 'two' , 'three')
t2 = ('four',)
print(t1 + t2)
print("#튜플이 수정된 것 같으나 새로운 튜플이 생성됨을 id함수를 이용하여 확인할 수 있다.")
print(id(t1) , id(t2) ,id(t1 + t2))