import copy

print('#같은 주소를 참고하는 리스트의 값을 하나라도 변경하게 되면 두개의 리스트 값 모두 변경된다. (얕은복사)')
a_list = list(range(1,10))
b = a_list
b[5] = 'suprise'
print(a_list)
print(b)

print(sep='\n')

print('copy 메서드를 이용하여 복사한 리스트는 값을 변경하게 되더라도 하나의 리스트만 새 값을 갖는다.(깊은복사)')
c_list = list(range(0,10,2))
list_copy =c_list.copy()
print(c_list)
print(list_copy)
c_list[:] = ''
print(c_list , id(c_list))
print(list_copy , id(list_copy))

print(sep='\n')

print('#deepcopy 메서드를 이용하여 내부 객체까지 참조하는 리스트를 생성한다. (깊은복사)')
tiger = [[1,2],[3,4],5]
cat =  copy.deepcopy(tiger)
print(cat)
tiger = list('elephant')
print(tiger)
print(cat)

