#!/usr/bin/env python
# coding: utf-8

# In[1]:


if 1:
    print("hello l")


# In[4]:


a=3
if a==3:
    print ("Здесь a=",a)


# In[7]:


if a>1:
    print ('hello 3')


# In[9]:


lst=[1,2,3]
if lst:
    print('hello 4')


# In[11]:


a=3
if a>2:
    print('H')
else:
    print('L')
    


# In[12]:


a=17
b=True if a>10 else False
print  (b)


# In[13]:


a=int(input('введите число:'))
if a<0:
    print('Neg')
elif a==0:
    print('Zero')
else:
    print('Pos')


# In[14]:


a=0
while a<7:
    print('A')
    a+=1


# In[ ]:


a=0
while a==0:
    print('A')


# In[ ]:


a=0
while a>=0:
    if a==7:
        break
    a+=1
    print('A')


# In[ ]:


a=-1
while a<10:
    a+=1
    if a>7:
        continue
    print('A')


# In[ ]:


lst=[1,3,5,7,9]
for i in lst:
    print(i**2)


# In[ ]:


word_str='Hello, world!'
for g in word_str:
    print(g)


# In[ ]:




