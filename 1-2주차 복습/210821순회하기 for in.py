print("#zip 함수로 여러 시퀀스의 병렬 순회가 가능하다.")
print("#zip 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다 deseert 시퀀스의 원소가 4개이나 다른 시퀀스가 3개이기에 pouding은 출력되지 않는다.")
days = ['Monday' , 'Tuesday' , 'Wednesday']
drinks = ['cola' , 'cider' , 'beer']
fruits = ['banana' , 'orange' , 'apple']
dessert = ['cake' , 'cookie' , 'wapple' ,'pouding']

for day,friut,drink,dessert in zip(days,fruits,drinks,dessert):
    print(day , ":drink" , drink , "-eat" , friut , "-enjoy" ,dessert)

print(sep ='\n')

print('#zip 함수의 병렬순회를 이용하여 두개의 리스트를 이용한 사전 만들기 (dict)')
weeks = ['Monday' , 'Tuesday' , 'Wenesday' , 'Thrusday']
scadule = ['work' , 'study' , 'dance' , 'travel']
a=dict(zip(weeks,scadule))
print(a)