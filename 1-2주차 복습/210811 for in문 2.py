word = "thud"
#letter 객체에 word 함수 지정
for letter in word:
    #letter 함수 안에 'x'가 존재하는지 하나씩 순회 비교 후 첫번째 코드블럭 실행
    if letter == 'x':
        print("letter in x")
        break

    #letter 함수 안에 'x'가 존재하지 않으면 실행되는 코드블럭
    else:
        print(letter)
        print("Can not find letter in x")