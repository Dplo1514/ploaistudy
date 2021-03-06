# -*- coding: utf-8 -*-
"""210823 비대면수업

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x9QiOVVHDsJImJBuS04oQo7wfFRrZ6By

![image.png](attachment:image.png)

# Matplotlib: Visualization with Python

Matplotlib 패키지의 서브패키지인 pyplot는 매트랩(MATLAB)이라는 수치해석 소프트웨어의 시각화 명령을 거의 그대로 사용할 수 있도록 하였다.   
간단한 시각화 프로그램을 만드는 경우에는 pyplot 서브패키지의 명령만으로도 충분하다.

# ❦ 설치
"""

pip install matplotlib

"""# ❦ 주피터노트북 환경에서 실행"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""# ❦ 임포트"""

import matplotlib.pyplot as plt

"""# ❦ Hello world!"""

# [1, 2, 3, 4]를 그래프로 나타내기
plt.plot([1,2,3,4])
plt.show

"""x축이 0-3이고 y축이 1-4 인 이유 : 플로팅 할 **단일** 목록 또는 배열을 제공하는 경우 matplotlib는 이를 y값의 시퀀스라고 가정하고 자동으로 x값을 생성한다. 파이썬은 범위를 0부터 시작하므로 기본 x 벡터는 y와 길이가 같지만 0으로 시작한다. 따라서 x 데이터는 [0, 1, 2, 3]이다.   

플롯은 다목적 함수이며 **임의의 수의 인수**를 사용합니다. 예를들어 x 대 y를 플로팅하려면 위 코드를 다음과 같이 수정할 수 있다.
"""

# plt.plot([1, 2, 3, 4]) 수정
plt.plot([1,2,3,4],[2,4,6,8])
plt.show

"""# ❦ 플롯 스타일 서식 지정

모든 x, y쌍의 인수에 대해 플롯의 색상과 선 유형을 나타내는 형식 문자열인 세 번째 인수(옵션)가 있다. 형식 문자열의 문자와 기호는 MATLAB에서 가져온 것이며 색상 문자열을 선 스타일 문자열과 연결한다.   
**기본** 형식 문자열은 **파란색 실선인 'b-'** 이다. 위 코드를 빨간색 원으로 그려보자.
"""

# 서식지정 : 빨간색 원형 마커
plt.plot([1,2,3,4],[2,4,6,8] , 'ro')

"""### matplotlib.pyplot.plot 함수 사용법

![image-5.png](attachment:image-5.png)
<br>
![image-2.png](attachment:image-2.png)

### 스타일 적용 실습
"""

# 빨간색 사각형 dashed line
plt.plot([1,2,3,4],[2,4,6,8] , 'rs--')

# 녹색 삼각형 dash-dot
plt.plot([1,2,3,4],[2,4,6,8] , 'g^-.')

# 분홍색 다이아몬드 dotted 
plt.plot([1,2,3,4],[2,4,6,8] , 'mD:')

# 빨간색 원형 선없음
plt.plot([1,2,3,4],[2,4,6,8] , 'ro')

# 검은색 실선, 마커없음
plt.plot([1,2,3,4],[2,4,6,8] , 'k-')

"""![image.png](attachment:image.png)
<br><br>

![image-3.png](attachment:image-3.png)
"""



import numpy as np

# plt.plot([10, 20, 30, 40], [1, 4, 9, 16]) 에 색상, 선스타일, 선너비, 마커, 마커사이즈, 마커테두리색, 마커테두리 두께 지정
plt.plot([10,20,30,45] , [1,4,9,16] , 
         color='g' , linestyle ='--' , linewidth ='5' , marker ='o' ,
         markersize ='15' , markeredgecolor = 'b' , markeredgewidth='3')
plt.show

cc

# 한 번 더 연습
c

"""# ❦ 여러 개의 그래프를 하나의 윈도우에 그리기

### I. 하나의 plot 함수 이용
"""

import numpy as np
t = np.arange(0., 5., 0.2)
plt.title("Multiple line graphs on a window, Method 1")
plt.plot(t,t,'r--', t, 0.5*t**2 ,'bs:',t, 0.3* t**2 ,'g^-.')

"""### II. 여러 개의 plot 함수 이용"""

c

# 사인, 코사인 그래프
X = np.linspace(-np.pi , np.pi , 256)
C , S = np.cos(X) , np.sin(X)
plt.plot(X,C,'b--' , label = 'Cosign')
plt.plot(X,S, 'r:' , label = 'sine')
plt.xlabel('Angle(radian)')
plt.ylabel('Ampltude')
plt.legend()
plt.show

# 범례추가
# 사인, 코사인 그래프
X = np.linspace(-np.pi , np.pi , 256)
C , S = np.cos(X) , np.sin(X)
plt.plot(X,C,'b--')
plt.plot(X,S, 'r:')
plt.xlabel('Angle(radian)')
plt.ylabel('Ampltude')
plt.show

"""# ❦ 하나의 Figure를 여러 개의 윈도우로 나누기"""

# 1행 3열 중 1열
plt.subplot(131)
plt.plot([1,3,5])

# 1행 3열 중 2열
plt.subplot(132)
plt.scatter([1,2,3],[1,2,3])

# 1행 3열 중 3열
ax = plt.subplot(133)
plt.bar([10,11,12] , [1,3,5])

# 1행 3열 중 3열 -> 축 전달 방식 : 3.3부터는 지원하지 않음
plt.subplot(ax)
plt.bar([13,14,15] , [2,4,8])

# 자동 레이아웃
plt.tight_layout()

"""# ❦ bar/barh"""

y = [1.8, 2.5, 0.7]
x = np.arange(len(y))

np.random.seed(0)

people = ['Cho', 'Kim', 'Shin', 'Na']
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

"""# ❦ stem"""

x = np.linspace(0, 2 * np.pi, 10)
plt.title("Stem")

"""# ❦ scatter"""

X = np.random.normal(0, 1, 200)
Y = np.random.rand(200)
plt.title("Scatter Plot")

N = 30
x = np.random.rand(N)
y1 = np.random.rand(N)
y2 = np.random.rand(N)
y3 = np.pi * (15 * np.random.rand(N))**2
plt.title("Bubble Chart")

"""# ❦ pie"""



"""# ❦ Histogram"""



"""# ❦ 판다스(Pandas)에서 plot"""

import pandas as pd
np.random.seed(0)
df1 = pd.DataFrame(np.random.randn(100, 3),
                   index=pd.date_range('1/1/2018', periods=100),
                   columns=['A', 'B', 'C'])

# pandas.DataFrame.cumsum()으로 위와 동일한 효과 나타내기
np.random.seed(0)

"""# 참고문헌
https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

"""