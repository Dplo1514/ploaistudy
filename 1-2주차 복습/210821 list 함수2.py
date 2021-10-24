print('#인덱싱을 통하여 문자열 분할을 통한 리스트의 생성이 가능하다')
today = '2021/02/21'
print(today.split('/'))

print(sep="\n")

print('#reverse 메서드를 이용하여 리스트의 뒤집기가 가능하다')
a_list = list(range(1,11))
a_list.reverse()
print(a_list)

print(sep="\n")

print('#list.append 함수를 이용하여 리스트 마지막 원소를 추가할 수 있다.')
b_list = list(range(0,11,2))
print(b_list)
b_list.append(12)
print(b_list)

print(sep="\n")

print('#list.insert 함수를 이용하여 원하는 위치에 원소를 추가할 수 있다.')
c_list = list(range(0,15,3))
print(c_list)
c_list.insert(3, 7.5)
print(c_list)