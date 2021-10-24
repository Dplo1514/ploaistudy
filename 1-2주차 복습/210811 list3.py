#.append 함수를 이용한 리터럴 추가
test_list = ['one' , 'two' , 'three' , 'four' ,'five']
test_list.append('six')
print(test_list)

#insert 함수를 이용한 원하는 위치에 리터럴 추가
test_list2 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list2.insert( 2 , 'yeah')
print(test_list2)

#extend 함수를 이용한 리스트의 결합
test_list3 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list4 = [1 , 2 , 3 , 4 , 5 ]
test_list3.extend(test_list4)
print(test_list3)

#append 함수를 이용한 리스트의 결합은 리스트안에 리스트를 만듦
test_list5 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list6 = ['six' , 'seven']
test_list5.append(test_list6)
print(test_list5)
print(test_list5[5])

#offset을 이용하여 원소의 교체가 가능
test_list7 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list7[2] = '3'
print(test_list7)