#or을 이용하여 letter 함수안의 값 맞추기
letter = 'o'
#letter 객체안에 l 또는 e 또는 t 또는 o가 있다면
if letter == 'l' or letter == 'e' or letter == 't' or letter =='o':
    print("o in letter")  #o in letter를 프린트하라
else: #letter 객체안에 아무 것도 없다면 I can't find letter in o를 프린트하라
    print("I can't find letter in o")

viowel = 'violet'
if letter in viowel: #viowel 안에 letter객체의 리터럴이 존재한다면
    print('letter in viowel') #letter in viowel을 프린트하라
else:
    print("I can't find viowel in o")

#데이터 값에 대한 in 찾기
viowel_set = {'a' , 'e' , 'i' ,'o' , 'u'}
print(letter in viowel_set)

viowel_list = ['a' , 'e' , 'i' ,'o' , 'u']
print(letter in viowel_list)

viowel_tuple = ('a' , 'e' , 'i' ,'o' , 'u')
print(letter in viowel_tuple)

viowel_str = 'aeiou'
print(letter in viowel_str)

