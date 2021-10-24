import random
print("Random 모듈")


print("random() : 0.0 <= x < 1.0 사이의 float를 리턴합니다" , random.random())

print("uniform(min , max) : 지정한 범위 사이의 float를 리턴합니다"  , random.uniform(10,20))

print("randrange(): 지정한 범위의 int값을 리턴합니다." , random.randrange(10))
#-randrange (max) : 0부터 max값 사이를 리턴합니다.
#--randrange (min , max) : min부터 max값 사이의 값을 리턴합니다.

print("choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택합니다" , random.choice([1,2,3,4,5]))


a=[1,2,3,4,5]
random.shuffle(a)
print("shuffle(list) : 리스트 내부의 요소들을 랜덤하게 섞습니다",a)

print("sample(list, k=숫자) : 리스트 내부의 요소중 k값 만큼 랜덤하게 추출합니다." , random.sample([1,2,3,4,5],k=2))




