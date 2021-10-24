import numpy as np
ori = [1,3,5,2,7,9,8,2,1,4,2,5] #객체 ori의 리스트 리터럴 지정
npori = np.array(ori) #npori 객체에 ori를 np.array형태로 지정
print(npori %2 == 0) #npori 객체의 각 값들을 2로 나누었을 때 결과값이 0인 리터럴을 출력 (짝수인 값을 true false 형태로 출력)
evens = npori[npori %2==0] #evens 객체에 npori의 짝수 결과값을 지정 np.array값 true인 값들을 지정
evens = list(evens) #evens의 리터럴을 리스트형태로 지정
print(evens) #evens를 출력