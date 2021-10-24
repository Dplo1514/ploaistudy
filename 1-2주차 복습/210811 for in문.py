word = 'foud'
offset = 0
#offset이 word의 객체 수 보다 작은동안 반복
while offset < len(word):
    print(word[offset])
    offset+=1

#for문을 이용한 반복문 생성
for offset in word:
    print(offset)

for offset in word:
    if offset == "u":
        break
    print(offset)