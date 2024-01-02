#!/usr/bin/env python
# coding: utf-8

# In[8]:


f=open('a.txt',"w")
f.write("Hell Ekal 12345")
f.close()


# In[15]:


# f=open('a.txt',"r")
f=open('a.txt')
data=f.read()
print(data)
f.close()


# In[14]:


f=open('a.txt',"a")
f.write(" Hii")
f.close()


# In[32]:


f=open('a.txt',"w+")
f.write("Hii")
f.close()
f=open('a.txt',"r")
print(f.read())
f.close()


# In[29]:


f=open('a.txt',"r+")
print(f.read())
print()
f.close()
f=open('a.txt',"r+")

f.write("Hii")

print(f.read())
f.close()


# In[39]:


f=open('a.txt',"a+")

f.write("Hii")
f.close()
f=open('a.txt',"a+")
print(f.read())
f.close()


# In[42]:


f=open('b.txt',"x")
f.write("Ekal")
f.close()


# In[7]:


f=open("a.txt","w")
l=['abc\n','hello\n','python\n',"Bye"]
f.writelines(l)
f.close()
f=open("a.txt","r")
print(f.read())

