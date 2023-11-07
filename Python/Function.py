#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Default Argument

def d1(name="ABC",m):
    print("Hello",name,m)
    
d1("Ekal")
d1()


# In[38]:


#variable length argument

def d1(*n):
    for i in n:
        print(i)
        
d1(1,2,3,4,5)


# In[48]:


#variable length argument

def d1(*n,s):
    for i in n:
        print(i)
    print(s)
d1(1,2,3,4,5,s=10)


# In[64]:


def d1(*m,**n):
    for k,v in n.items():
        print(k,'=',v)
        
    for i in m:
        print(i)
d1(1,2,3,5,A=1,B=2,C=3,D=4)


# In[70]:


b=5
def d1():
    global b
    b=7
    print(b)
d1()

def d2():
    print(b)
d2()


# In[ ]:




