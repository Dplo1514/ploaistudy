#pop을 이용한 인덱싱과 동시에 원소 제거
test_list = ['one' , 'two' , 'three' , 'four' ,'five']
test_list.pop() #pop()이나 pop(-1)은 마지막 원소를 인덱싱과 동시에 삭제
print(test_list)

#clear를 이용한 모든 항목 삭제하기
test_list2 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list2.clear()
print(test_list2)

#index를 이용한 리스트내 원소의 위치값 반환
#in문을 이용한 리스트내 원소의 존재파악
test_list3 = ['one' , 'two' , 'three' , 'four' ,'five']
print(test_list3.index('two'))
print('one' in test_list3)

#count를 이용한 리스트내의 원소 갯수파악
test_list4 = ['one' , 'two' , 'one' , 'one' ,'one']
print(test_list4.count('two'))
print(test_list4.count('one'))
