#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os

os.mkdir("package")


# In[14]:



os.chdir("C:\\Users\\LJENG\\Ekal\\package")


# In[15]:



get_ipython().run_cell_magic('writefile', 'mod1.py', 'def foo():\n    print("Foo")')


# In[16]:


get_ipython().run_cell_magic('writefile', 'mod2.py', "def bar():\n    print('bar')")


# In[26]:


# from package import mod1
import package as p
mod1.foo()


# In[ ]:




