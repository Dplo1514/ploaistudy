print('#튜플로 한번의 여러개의 원소에 튜플 원소값을 할당할 수 있다, 이것을 "튜플 언패킹"이라 부른다')
marx_tuple = (1,2,3)
a,b,c = marx_tuple
print(a,b,c)

sep='\n'
print(sep)

print("#한 문장에서 값을 교환하기위하여 임시변수를 사용하지않고 튜플의 사용이 가능하다")
password = 'deeplo'
id = '1234567'
password,id = id,password
print("id:",id)
print("password:",password)


