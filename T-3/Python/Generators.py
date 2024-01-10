#!/usr/bin/env python
# coding: utf-8

# In[2]:


def abc():
    for i in range(10):
        if(i%2==0):
            yield i
            
for i in abc():
    print(i)


# In[1]:


def xyz():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
obj=xyz()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


# In[5]:


l=[1,2,3,4]
z=(x**2 for x in l)
print(z)
for i in z:
    print(i)


# In[16]:


l=[1,2,3,4,5,6,7,8,9,10]
t=[x*5 for x in l]
for i,j in enumerate(t):
    print("5 *",i+1,"=",j)

