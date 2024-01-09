#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_cell_magic('writefile', 'module1.py', 'x=500\ndef add(a,b):\n    print(a+b)\ndef sub(a,b):\n    print(a-b)')


# In[11]:


get_ipython().run_cell_magic('writefile', 'module2.py', 'x=500\ndef mul(a,b):\n    print(a*b)\ndef div(a,b):\n    print(a/b)')


# In[10]:


import module1 as m1

m1.add(5,10)

module1.sub(5,10)


# In[23]:


from module2 import *

print(x)

mul(10,20)


# In[36]:


import os
print(os.getcwd())
print(os.listdir())
# print(os.mkdir("C:\\Users\\LJENG\\Vraj"))
# print(os.chdir())
print(os.getcwd())
# print(os.rmdir("C:\\Users\\LJENG\\Vraj"))
print(os.remove("C:\\Users\\LJENG\\Ekal\\Untitled.ipynb"))

