#!/usr/bin/env python
# coding: utf-8

# In[ ]:


210722넘파이의 자료형


# In[9]:


import numpy as np

c = np.zeros((5)) #np.zeros : 0으로 구성된 배열을 만든다
c


# In[10]:


b = np.zeros((2 , 3)) #()로 묶어주는 튜플 입력시 다차원 배열의 생성이 가능
b


# In[16]:


c = np.ones((5,2) , dtype="i")  #np.ones : 1로 구성된 배열을 만든다
c                               #dtype=i : 정수형의 배열을 생성하라


# In[18]:


c = np.ones_like(b)  #np.ones_like : 튜플로 생성한 배열을 타 배열과 같은 모습으로 
c                               


# In[21]:


g = np.empty ((4,3)) #np.empty : 원소의 값이 없는 배열의 구성만 생성
g


# In[24]:


np.arange(10) #np.arange : numpy의 배열을 생성하는 range 명령 
np.arange(3 , 12 , 2) #(시작 , 끝 , 불포함)  (3에서 , 12까지 ,2칸씩 건너뛴다)


# In[25]:


np.linspace(0 , 100 , 5) #np.linspace : 선형 구간을 지정한 수 만큼 분할
                            #(0에서 , 100까지 ,5개로 나누어라)


# In[26]:


np.logspace(0.1 , 1 , 10 ) #np.linspace : 로그형 구간을 지정한 수 만큼 분할


# In[29]:


A = np.array([[1, 2, 3], [4, 5, 6]])
A


# In[ ]:




