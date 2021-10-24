print('#이터레이터와 range함수를 이용하여 리스트를 만들 수 있다.')
a = []
for b in list(range(0,10)):
    a.append(b)
print(a)

print(sep = '\n')

print('#리스트 컴프리헨션으로 정수 리스트를 만들어보자.')
print('#표현식 for 항목 in 순회가능한 객체')
number_list=[numbers+1 for numbers in range(1,10)]
print(number_list)
