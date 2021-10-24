# number_list=[]
# for number in range(1,6):
#     number_list.append(number) #1에서 5까지 number에 순회 append시키며 1~5로 구성된 리스트를 number에 할당
#     # print(number_list)          #number_list의 list 속성을 할당받아 list 형태로 출력
#     print(number)

# number_list=list(range(1,6)) #list속성을 할당받아 1~6까지 range되는 list를 할당
# print(number_list)

# number_list = [number-1 for number in range(1,10)]
#                #표현식  for  항목  in 순회가능한 객체
# print(number_list)

# a_list = [number for number in range (1,6) if number % 2 ==1]
#          #표현식 for  항목    in 순회가능한 객체 if 조건문 (2로 나누었을 때에 1이 나머지가 1과 같은 정수) (홀수)
# print(a_list)

a_list = []
for number in range(1,6):
