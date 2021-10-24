print("#슬라이스는 하위 리스트에 값을 할당할 수 있다.")
a_list = [1,2,3,4,5]
a_list[1:3] =7,8,9
print(a_list)

print(sep='\n')

print("#del 메서드를 통한 함수의 삭제가 가능하다.")
del a_list[2:4]
print(a_list)

print(sep='\n')

print('#pop함수는 리스트의 끝 항목을 추출 후 제거한다.')
b_list=[1,2,3,4,5]
print(b_list.pop())
print(b_list)

print(sep='\n')

print('#clear함수는 리스트의 모든 항목을 제거한다.')
b_list.clear()
print(b_list)


