teststr = "a duck goes into a bar..."
#strip함수를 이용하여 문자열에서 특정 시퀀스가 삭제된 결과값을 생성 반환한다.
print(teststr.strip('.'))
#captilize는 문자열에서 첫번째 문자를 인덱싱 후 대문자로 변환 결과값을 반환한다.
print(teststr.capitalize())
#title은 모든 문자열의 첫번째 글자를 인덱싱 후 대문자로 변환 결과값을 반환한다.
print(teststr.title())
#str타입의 모든 문자를 대문자로 변환 후 반환
print(teststr.upper())
#str타입의 모든 문자를 소문자로 변환 후 반환
print(teststr.lower())
swapcasestr="AbCdEfGhIjK"
#swapcase는 str 타입의 문자열의 대,소문자를 변환한다.
print(swapcasestr.swapcase())
