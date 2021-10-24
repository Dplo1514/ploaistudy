a = (1,[1,2],[3,4]) #(정수 리터럴,튜플,불변) ,[객체(리스트,가변)] ,[객체(리스트,가변)])
#a[0]= 2 #TypeError: 'tuple' object does not support item assignment (튜플은 불변이기 때문에 0번째 원소의 변경은 불가능)
a[1][1]=5
print(a)