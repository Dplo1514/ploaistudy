print('#1과 5 사이에서 홀수 리스트를 만드는 새 컴프리헨션을 만들어보자')
print('#표현식 for 항목 in 순회가능한 객체 if 조건식')
a_list = [number for number in range(1,50) if number %2==1]
print(a_list)

print(sep = '\n')

print('#상단 컴프리헨션이 지금까지 사용했던 방식보다 좀 더 단순하며 강력하다.')
b_list =[]
#for 항목 in 순회가능한 객체
for text in range(0,50):
    if text %2 == 1:
        b_list.append(text)
print(b_list)

print(sep='\n')

print("#루프에 상응하는 하나 이상의 for 절을 사용할 수 있다.")
rows = range(1,4)
cols = range(1,3)
#항목 in 순회가능한 객체
for row in rows:
    for col in cols:
        print(row,col)
