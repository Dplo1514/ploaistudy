#튜플언패킹 : 한번에 여러개 원소에 튜플을 지정
test_tuple1 = ('test1' , 'test2' ,'test3')
a,b,c = test_tuple1
print(a)
print(b)
print(c)
print(a,b,c)

#tuple 함수를 이용하여 list를 tuple 타입으로 변환이가능
test_list = [123 , 456 , 789]
print(tuple(test_list))

#튜플의 결합
print(('inhyuk',) + ('seo' , 'yeon' , 'yang'))