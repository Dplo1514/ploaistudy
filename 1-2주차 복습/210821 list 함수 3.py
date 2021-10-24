print('#list.extend 메서드를 이용하여 다른 리스트를 병합할 수 있다.')
a_list = list(range(1,11,2))
b_list = list(range(1,11,5))
a_list.extend(b_list)
print(a_list)

sep="\n"

print('#append 메서드를 이용하면 리스트안에 또다른 리스트가 생성된다.')

c_list = list(range(10,21,2))
d_list = list(range(10,21,4))
c_list.append(d_list)
print(c_list)
print('#인덱싱을 통한 리스트안에 원소변경이 가능하다.')
c_list[-1] = 100
print(c_list)


