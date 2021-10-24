#split(기준이 될 문자) 함수로 문자를 나누는 것이 가능

introduce = "hi my name is in hyuk Lim"
print(introduce.split())

#문자열을 list객체에 join함수를 이용하여 join 후 list 객체를 str타입으로 출력이 가능

jlist=["apple" , "banana" , "grape" , "melon"]
jstr = ",".join(jlist)
print(jstr)

#replace 함수를 이용하여 문자열의 특정 문자를 인덱싱 후 변경이 가능

teststr = "This is replace test str"
print(teststr.replace("This","Yes"))

