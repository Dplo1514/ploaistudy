#!/usr/bin/env python
# coding: utf-8

# # EDA (Exploratory Data Analysis)
# 
# ### 사용 데이터 
#    **보스턴 집값 데이터** : https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/BostonHousing2.csv
# 
# ### 데이터 설명
# 
# [Boston Housing 1970](https://geodacenter.github.io/data-and-lab/boston-housing/) 데이터의 일부를 추출한 데이터로서,     
# 
# 레코드수 : 506 개      
# 컬럼개수 :  17 개
# 
# | 컬럼명 | 설명|
# |:-------|:------|
# |TOWN | 소속 도시 이름|
# |LON  | 해당 지역의 경도(Longitudes) 정보| 
# |LAT  | 해당 지역의 위도(Latitudes) 정보|
# | **CMEDV**| **해당 지역의 주택 가격 (중앙값) (corrected median values of housing in USD 1000)**|
# | CRIM | 지역 범죄율 (per capita crime)|
# | ZN   | 소속 도시에 25,000 제곱 피트(sq.ft) 이상의 주택지 비율|
# | INDUS | 소속 도시에 상업적 비즈니스에 활용되지 않는 농지 면적|
# | CHAS | 해당 지역이 Charles 강과 접하고 있는지 여부 (dummy variable)|
# | NOX | 소속 도시의 산화질소 농도|
# | RM | 해당 지역의 자택당 평균 방 갯수|
# | AGE | 해당 지역에 1940년 이전에 건설된 주택의 비율|
# | DIS | 5개의 보스턴 고용 센터와의 거리에 따른 가중치 부여|
# | RAD | 소속 도시가 Radial 고속도로와의 접근성 지수|
# | TAX | 소속 도시의 10000달러당 재산세|
# | PTRATIO | 소속 도시의 학생-교사 비율|
# | B | 해당 지역의 흑인 지수 (1000(Bk - 0.63)^2), Bk는 흑인의 비율|
# | LSTAT | 해당 지역의 빈곤층 비율|
# 

# ## 1. 라이브러리 및 데이터 로딩

# In[3]:


# 라이브러리 로딩
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_csv('https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/BostonHousing2.csv')
df.head()


# ## 2. EDA
# ### 2.1 데이터의 전반적인 검토(Overview)

# In[11]:


# 결측치 점검 : isnull() / notnull() df.isnull().sum() 모든 컬럼에 null값이 있는지 확인 결과값 = False
df.isnull().sum()


# In[12]:


# 데이터 자료형 확인 : TOWN을 제외한 나머지는 모두 숫자형 데이터
df.info()


# In[25]:


# 숫자형 변수(Numerical variable)에 대한 통계값 : describe()
df.describe() 


# In[24]:


# 범주형 변수(Categorical variable)의 종류 확인 : unique() set.TOWNS
towns = df.TOWN.unique() #df["TOWN"].unique()
print(f'도시의 개수 : {len(towns)}')
towns


# ### 2.2 목표(종속) 변수(CMEDV) 탐색 

# In[28]:


# 통계량
df["CMEDV"].describe()


# In[35]:


# 히스토그램 : hist()
df["CMEDV"].hist(bins=100)


# In[40]:


# boxplot : boxplot()
df.boxplot(column="CMEDV")
plt.show()

#seaborn
sns.catplot(data=df , x="CMEDV" , kind="box")
plt.show()

#matplotlib
plt.boxplot(df.CMEDV)
plt.show()


# ### 2.2 설명(독립) 변수 탐색

# In[46]:


# 히스토그램 
x= ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']
for xi in x:
    sns.displot(data = df , x=xi , bins=10)


# ### 2.3 설명변수와 목표변수 간 관계 분석

# In[ ]:


# 상관관계 분석 : Pearson 상관계수, corr()


# In[ ]:


# 히트맵 표현 


# In[ ]:


# CMDEV-RM 관계 분석 : scatter plot


# In[ ]:


# CMDEV-LSTAT 관계 분석 : scatter plot


# In[ ]:


# 상관관계가 적은 변수들과의 분포 비교  예)DIS(고용센터와의 거리)는 0.25


# ### 2.4 도시별 차이 분석

# In[ ]:


# 92개의 도시가 있었다. 각 도시별 빈도수를 확인한다.: value_counts()


# In[ ]:


# 히스토그램


# In[ ]:


# 도시별 주택가격 특징 


# In[ ]:


# 왜 보스턴 지역의 집값이 낮을까?  


# ## 3. 집값 예측 모델링

# ### 3.1 정규화 
# 특징들 간 크기(scale) 차이로 인한 중요도 오분석을 막기위해 특징들 간 정규화 수행

# In[ ]:


# 데이터 스케일 확인


# In[ ]:


# CHAS 더미 데이터 확인 --> 이 데이터는 제외하고 사용


# In[ ]:


# sklearn 설치
get_ipython().system('pip install scikit-learn ')
# !pip install scipy


# In[ ]:


# 정규화
from sklearn.preprocessing import StandardScaler


# In[ ]:


# 스케일링된 데이터 확인
df.head()


# ### 3.2 데이터셋 분할
# Training set과 Test set으로 나눠 Training set은 모델을 만드는 과정에서 사용하고, Test set은 완성된 모델의 성능을 확인할 때 사용한다.

# In[ ]:


from sklearn.model_selection import train_test_split

num_cols = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']  # 더미 변수 제거
X = df[num_cols]
y = df['CMEDV']


# In[ ]:


# 학습데이터 확인
X_train.shape, y_train.shape


# ### 3.3 다중공선성(Multicollinearity) 확인
# 
# 다중공선성(多重共線性)문제(Multicollinearity)는 통계학의 회귀분석에서 독립변수들 간에 강한 상관관계가 나타나는 문제이다.    
# VIF (Variance Inflation Factors, 분산팽창요인)으로 다중공선성을 판단하며, VIF > 10 인 변수들은 다른 변수와 상관관계가 높아 다중공선성이 존재하는 것으로 판단한다. 

# In[ ]:


# 통계모델 모듈 설치
get_ipython().system('pip install statsmodels')


# In[ ]:


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['features'] = X_train.columns
vif['VIF Factor'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif.round(1)


# ### 3.4 회귀 모델링
# 
# 선형회귀모델(Linear Regression Model)

# In[ ]:


from sklearn import linear_model

# training set으로 선형회귀모델 생성


# test set으로 예측결과 확인


# 회귀모델 계수 확인


# In[ ]:


# 모든 변수를 사용한 결과


# ### [비교] 변수를 줄여서 사용한 경우
# 

# In[ ]:


# 데이터셋 생성
num_cols = ['CRIM', 'ZN', 'INDUS', 'RM', 'AGE','PTRATIO', 'B', 'LSTAT']
X = df[num_cols]
y = df['CMEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train.shape, y_train.shape


# In[ ]:


# 다중공선성 확인
vif = pd.DataFrame()
vif['features'] = X_train.columns
vif['VIF Factor'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif.round(1)


# In[ ]:


# 회귀 모델링 --> 복사해서 사용


# In[ ]:


# 테스트 결과 : ['CRIM', 'ZN', 'INDUS', 'RM', 'AGE','PTRATIO', 'B', 'LSTAT']  --> 복사해서 사용


# #### 결과비교
# 1. 모든 변수를 사용한 경우
# ![image.png](attachment:image.png)
# 2. VIF > 4인 변수를 제거하고 사용한 경우
# ![image-2.png](attachment:image-2.png)

# # 참고문헌
# https://hyemin-kim.github.io/2020/08/11/E-Python-LinearRegression-1/
