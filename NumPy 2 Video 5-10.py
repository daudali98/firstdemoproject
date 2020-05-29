#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.array([1,3,4,5,6])


# In[3]:


x[2]


# In[4]:


x>5


# In[6]:


x[x<5] #boolean indexing


# In[8]:


x[[2,1]] #fancy Indexing


# # Slicing

# In[10]:


x=np.random.rand(10,10)


# In[11]:


x


# In[12]:


x[0]


# In[13]:


x[0][4]


# In[20]:


x[::,0:10:2]


# In[23]:


x=np.ones((5,5))
x


# In[24]:


x[1:-1,1:-1]=0
x


# In[25]:


x=np.ones((5,5))
x


# In[37]:


x[1:4:1]


# In[38]:


x=np.ones((5,5))
x


# In[43]:





# In[44]:





# In[45]:


x=np.ones((5,5))
x


# In[50]:


x[0:4:2]=0
x


# In[51]:


x[0:4:2]=0
x


# In[64]:


x=np.ones((6,6))
x


# In[65]:


x[0:5:2,0:5:2]=0
x


# In[63]:


x[0:5:2,0:5:2]=0
x


# In[70]:


x=np.array[10,2,4,1,6]
print("daud")
np.sqrt(x)
print("daud")


# In[1]:


print("daud")


# In[2]:


import numpy as np


# In[5]:


x=np.array([10,2,4,1,6])
np.sqrt(x)


# In[6]:


np.power(x,2)


# In[8]:


y=[98,12,0,4,1]
np.maximum(x,y)


# In[10]:


x=3
#x>1 ? "Hellow":"World" Ternary Operator


# In[12]:


salary=np.array([4500,2300,4600,780,-1,-9])
np.where(salary>0,"Okay","Not Okay")


# In[13]:


x=np.array([10,20,30])
x.mean()


# In[15]:


x.cumsum()


# In[16]:


x.cumprod()


# In[21]:


x=np.array([10,30,30])
y=x>20
y


# In[22]:


y.sum()


# In[23]:


y.all()


# In[24]:


x=[1,2,3,4,5,66]
np.save("testx",x)


# In[31]:


loadx=np.load("testx.npy")
loadx


# In[32]:


y=[2,4,5,6,8]
np.savez("testxy",x,y)


# In[35]:


loadxy=np.load("testxy.npz")
loadxy


# In[41]:


z=loadxy['x']
z


# In[43]:


x=np.random.rand(3,2)


# In[47]:


y=np.random.rand(2,3)


# In[48]:


x.dot(y)


# In[50]:


x.transpose()


# In[51]:


x.trace()


# In[ ]:




