#strip 함수를 이용하여 str타입 객체의 특정 문자열을 인덱싱하여 제거가 가능

teststr = "This is strip test string show me have strip position!!"
print(teststr.strip("!!"))

print(teststr.startswith("This")) #teststr은 This로 시작하는가?
print(teststr.endswith("!!")) #teststr은 !!로 끝나는가?

print(teststr.find("is")) #teststr에서 is가 등장하는 첫번째 오프셋 find : 검색
print(teststr.index("is")) #teststr에서 is를 인덱싱 결과값을 반환 index : 선택

print(teststr.rfind("!"))   #rfind , rindex는 문자열의 끝에서부터 문자열을 찾아 반환

print(teststr.count(" ")) #teststr에 공백이 몇번 들어가는가
print(teststr.isalnum()) #teststr의 모든 문자는 알파벳 또는 숫자로 이루어져 있는가?