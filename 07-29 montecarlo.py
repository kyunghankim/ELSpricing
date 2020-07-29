#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


#몬테카를로 기법으로 원 넓이, pi 근사값구해보기
N = 1000 ; count = 0


# In[23]:


x = np.zeros([N,1]) ; y = np.zeros([N,1])


# In[24]:


z = np.zeros([N,1]) ; r = np.zeros([N,1])


# In[25]:


x = 2*np.random.random((N,1)) -1
y = 2*np.random.random((N,1)) -1
z=np.power(x,2)+np.power(y,2)
r=np.sqrt(z)


# In[27]:


for i in range(N):
    if r[i]<1:
        count = count + 1
        plt.plot(x[i], y[i], 'k*', markersize=5)
    else:
        plt.plot(x[i], y[i], 'ko', markersize=5)
t = np.linspace(0, 2*np.pi,100)
plt.plot(np.cos(t),np.sin(t),'k',linewidth=2)
plt.axis('image'); plt.show()
Pi=4*count/N
print('Pi is %f' % Pi)


# In[28]:


# 주가경로 Stock Process 생성
N = 180 ; S = np.zeros([N,1]) ; S[0]=100
vol = 0.079 ; r = 0.0165; T=1; dt = T/N
t = np.linspace(0,T,N)


# In[30]:


# 무위험 이자율 1.65%, 변동성 7.9%
z = np.random.normal(0,1,N)
for i in range(N-1):
    S[i+1,0] = S[i,0]*np.exp((r-0.5*vol**2)*dt                            +vol*z[i]*np.sqrt(dt))
plt.plot(t,S[:,0],'ko-')
plt.xlabel('Time')
plt.ylabel('Stock Process')
plt.show()


# In[33]:


# 주가경로 50개 Stock Process 생성
N = 365 ; S = np.zeros([N,1]) ; S[0]=100
vol = 0.079 ; r = 0.021; T=1; dt = T/N
t = np.linspace(0,T,N)
plt.xlabel('Time')
plt.ylabel('Stock Process')
for k in range(0,50):
    z = np.random.normal(0,1,N)
    for i in range(N-1):
        S[i+1,0]=S[i,0]*np.exp((r-0.5*vol**2)*dt                              +vol*z[i]*np.sqrt(dt))
    plt.plot(t[:],S[:],'k-',linewidth=0.3)
plt.show()


# In[ ]:




