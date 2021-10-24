print('#list에서 어떤 원소의 존재를 알기위하여 in 함수를 사용한다 갯수값을 반환할 때에는 count메서드를 사용한다')
a_list = list(range(1,30,2))
print(a_list)
print(10 in a_list)
print(5 in a_list)
print(a_list.count(5))

print(sep='\n')

print('# ","에 join을 이용하여 문자열로 리스트의 반환이 가능하다.')
marxes = ['Groucho' , 'Choio' , 'Harpo']
print(','.join(marxes))

print(sep='\n')

print('#sort와 sorted를 이용하여 리스트의 내부 정렬이 가능하다. / sorted는 정렬된 복사본을 반환한다. /내림차순 정렬은 reverse =true를 추가한다.')
b_list = [3,5,2,1,8,10,-1]
b_list.sort()
print(b_list)

c_list= [5,1,2,88,34,63,56,12]
sorted_c_list = sorted(c_list)
print(c_list)
print(sorted_c_list)

c_list.sort(reverse=True)
print(c_list)