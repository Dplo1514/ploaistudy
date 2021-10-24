#a=[1,2,3]
#b=a
#a[0]=2
#print(b) #얕은복사,참조 주소만 복사

#a=[1,2,3]
#b=a.copy()
#c=list(a)
#d=a[:]
#a[0:3]='b'
#print(a,b,c,d) #깊은복사 , 새로운 주소를 생성


# a=[1,2,3,[4,5]]
# b=a.copy()
# c=list(a)
# d=a[:]
# a[3][1]=10 #a 객체의 3번째 리스트 원소의 1번째 값을 10으로 바꾸어라
# print(a,b,c,d) #b,c,d의 깊은복사는 [4,5]리터럴의 새로운 주소를 만들지 않는다.
                 #그렇기 때문에 a객체의 리스트 값을 변경하면 복사한 다른 리스트의 값도 변경된다

import copy #copy 라이브러리 호출
a=[1,2,3,[4,5]]
b=copy.deepcopy(a) #copy 라이브러리의 deepcopy 메소드 사용
a[3][1]=10
print(a)
print(b)