#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[2]:


np.random.seed(7)


# In[10]:


np.random.normal(size=(3,3))


# In[12]:


np.random.uniform(size=(3,4))


# In[23]:


x=np.random.rand(4,6)
x


# In[28]:


x.reshape(2,2,6)


# In[30]:


x.reshape((2,2,6), order="F")


# In[31]:


x.reshape(2,2,-1)


# In[33]:


x.ravel()


# In[41]:


x=[[1,3,5,6],[21,22,23,24]]


# In[49]:


arr1=np.array(x)


# In[50]:


y=[[11,13,15,16],[112,113,114,115]]


# In[51]:


arr2=np.array(y)


# In[52]:


np.concatenate((arr1,arr2),axis=0)


# In[53]:


np.concatenate((arr1,arr2),axis=1)


# In[56]:


np.vstack((arr1,arr2))


# In[58]:


np.hstack((arr1,arr2))


# In[59]:


x=[11, 12, 13, 14, 15, 16, 17, 19]


# In[60]:


d=np.array(x)


# In[61]:


d


# In[63]:


np.split(d,[2,5])


# In[3]:


x=[[11, 12, 13, 14, 15, 16, 17, 19],
   [1, 2, 3, 4, 5, 6, 7, 9]]


# In[4]:


d=np.array(x)


# In[6]:


np.split(d,[4,6],axis=1)


# In[7]:


np.split(d,[1],axis=0)


# In[8]:


x=[1,3,4]


# In[9]:


d=np.array(x)


# In[10]:


np.repeat(d,3)


# In[11]:


np.tile(d,3)


# In[ ]:




