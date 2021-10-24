print(str (98.6)) #98.6의 실수를 문자열로 변환
print(str (True)) #True의 참값을 문자열로 변환

teststr = "\" hello I'm \" escape testing str" # "\를 이용하여 "출력가능
print(teststr)

#문자열 타입을 +연산자를 이용하여 결합이 가능
teststr2 = "test2"
teststr3 = "test3"
print(teststr2 + teststr3)

#*를 사용하여 같은문자의 여러번 출력이 가능
teststr4 = '4번 출력됩니다' *4
print(teststr4)