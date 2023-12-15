#!/usr/bin/env python
# coding: utf-8

# In[8]:


s={i**2 for i in range(1,11) if i%2==0}
print(s)

l=[i**2 for i in range(1,11) if i%2==0]
print(l)


d={i:i**2 for i in range(1,11) if i%2==0}
print(d)

