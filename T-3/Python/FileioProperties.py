#!/usr/bin/env python
# coding: utf-8

# In[5]:


f=open("a.txt","w")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# In[4]:


f=open("a.txt","r")
print(f.read())


# In[6]:


f=open("a.txt","w")
print(f.read(5)) 
f.close()


# In[16]:


f=open("a.txt","r") 
print(f.readline(1)) 
print(f.readline(5)) 
print(f.readline(4)) 
print(f.readline(40)) 
f.close()


# In[10]:


f=open("a.txt","r") 
print(f.readlines())
f.close()


# In[19]:


# WAP to count number of line from text file

f=open("a.txt","r") 
l=f.readlines()
count=len(l)
f.close()
print(count)


x=0
f=open("a.txt","r") 
for i in f:
    x+=1
print(x)
f.close()


# In[27]:


# wap to display odd number of lines from text file
f=open("a.txt","r") 
l=f.readlines()
print(l[::2])
f.close()


# In[32]:


f=open("a.txt","r") 
c=0
for i in f:
    if c%2==0:
        print(i)
    c=c+1

