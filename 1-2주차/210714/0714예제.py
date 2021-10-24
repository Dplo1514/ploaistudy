ori =[1,3,5,2,7,9,8,2,1,4,2,5]
evens =[]
for ele in ori: #ele변수에 ori의 값을 하나씩 대입했을 때
    if ele % 2 == 0: #ele의 값들을 2로 나누었을 때 결과값이 0과 같으면
        evens.append(ele) #append : list에 추가하라
print(evens)