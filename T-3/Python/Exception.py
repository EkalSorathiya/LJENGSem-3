#!/usr/bin/env python
# coding: utf-8

# In[14]:


def div(a,b):
    try:
        print(a/b)
        print(a)
    except Exception as e:
        print(e)
    else:
        print("Pass")
    finally:
        print("FINALLY RUN")
div(10,0)


# In[27]:


def add(a,b):

    if type(a)==str:
        raise TypeError("A must be int")
    if type(b)==str:
        raise TypeError("B must be int")
    return a+b    

try:
    print(add(12,12))
    print(add(12,'w'))
except Exception as e:
    print(e)


# In[ ]:




