#!/usr/bin/env python
# coding: utf-8

# In[31]:


d={(91,2,3):(30,12,20),1:2,5:{1:2,6:8},8:0,2:8,54:6}
print(d)
print("----------")
for i in d:
    print(i,d[i])
print("----------")
print(d[1])
print(d.get(5))
print(d[5][6])
print(d.keys())
d['abc']=60
print(d)
d.pop('abc')
print(d)
d.popitem()
print(d)
d.popitem()
print(d)
del d[1]
print(d)
d.clear()
print(d)



# In[39]:


d={1:2,5:7,8:0,2:8,54:6}
print(len(d))
print(max(d))
print(min(d))
print(sorted(d))
print(sorted(d,reverse=True))
print(d.items())
d1={"a":1,"b":2}
d.update(d1)
print(d)


# In[42]:


s=['a','b','c']
d=dict.fromkeys(s,1)
print(d)


# In[48]:


# convert list of tuple into dict
s=[('a',5),('b',6),('c',7)]
d={}
for i,j in s:
    d[i]=j
print(d)


# In[69]:


# wap to count the words from the string starting with char  char are keys ,and count is value 
s='abc xyz bcd bdb'
l=s.split()
d={}
for i in l:
    d[i[0]]=d.get(i[0],0)+1
print(d)


# In[104]:


# wap to create a dict whose keys are numbers and values are how many times the number occure in 
# 5X5 matrix also print the three most common numbers

l=[[5,3,3,5,5],[2,3,4,3,3],[3,3,3,3,3],[3,4,5,3,3],[5,4,1,2,3]]
d={}
for i in range(len(l)):
    for j in l[i]:
        d[j]=d.get(j,0)+1

print(sorted(d))
print(d)
l=[]
d1=d.items()
print(d1)
for i,j in d1:
    l.append([j,i])
    
l.sort()
l.reverse()
l2=[]
for i in range(3):
    l2.append(l[i][1])
print(l2)


# In[ ]:




