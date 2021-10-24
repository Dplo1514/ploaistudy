letters = 'abcdefghijklmnopqestuvwxyz'
print(letters[0]) #letters 문자열의 0번째를 인덱싱하여 프린트가 가능
print(letters[0:10]) #letters 문자열의 0에서 10번째 슬라이싱 프린트가 가능
print(letters[0:10:2]) #letters 문자열의 0에서 10까지 2개씩 건너뛰며
print(letters[-5:-2]) #끝에서부터 5번째의 3개 리터럴 추출

#letters[0] = 'x' #문자열은 불변이기에 인덱싱을 통한 변경이 불가능

print(letters.replace('a','xxxxx')) #replace함수를 이용하여 변경이 가능
print('change' + letters[1:]) #연산자와 슬라이싱을 이용하여 변경이 가능
print(len(letters)) #문자열의 길이 확인
