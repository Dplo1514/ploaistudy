empty_list=[]
a=weekdays=['monday','tuesday','wednesday','thursday','friday']
b=birds=['참새',['뱁새','독수리'],'학']
c=first_names=['graham','john','terry','terry','michael']
d=leap_years=[2000,2004,2008]
f=randomness=['Pinxatawney',{'groundhog':'phil'},'Feb.w']

a[0:3]=['sunday','sunday','sunday'] #a객체 리스트의 0~3번째를 sunday로 바꿔라 (slicing)
print(a) #a 리스트를 프린트해라

b_tuple=tuple(b) #b_tuple 객체에 b리스트를 tuple 속성으로 변환 후 지정
b_tuple[1][0:1]=['비둘기','비둘기','비둘기'] #b_tuple의 1번째(뱁새,독수리)리스트의 0~1번째 값을 비둘기x3으로 바꿔라
                                            #indexing에서의 0~1번째는 마지막 숫자 앞의 값까지 선택됨 (silicing)
                                             #tuple 속성은 불변이나 tuple안의 리스트는 가변이기 때문에 슬라이싱으로 변환이 가능
print(b_tuple)

c[1]="plo" #c에 지정된 first names 리스트의 첫번째 원소를 "plo"로 변환하라 (indexing)
print(c)