#slicing을 통한 리스트 항목 바꾸기
test_list = ['one' , 'two' , 'three' , 'four' ,'five']
test_list[0:3] = [1,2,3]
print(test_list)

#추가되는 원소의 값은 왼쪽의 슬라이스 항목과 수가 달라도된다.
test_list2 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list2[1:3] = [5,6,7,8]
print(test_list2)

#del 함수를 이용하여 리스트의 원소 삭제가 가능 중간에 있는 원소 제거시 한칸씩 앞으로 당겨짐
test_list3 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list3.append('six')
print(test_list3)
del test_list3[-1]
print(test_list3)

#
test_list4 = ['one' , 'two' , 'three' , 'four' ,'five']
test_list4.remove('three')
print(test_list4)