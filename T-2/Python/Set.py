#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(dir(set))


# In[57]:


s={1,2,3,4,(3,5,7,3),'ekal'}
print(s)
print({1,2,3}=={2,3,1})

s1={1,2,3,4}
s1.add(5)
s1.update((6,))
s1.update([8,])
print(s1)
s1.discard(8)
print(s1)
s1.pop()
print(s1)
s1.remove(5)
print(s1)

s1.clear()
print(s1)

del s


# In[78]:


s={0,1,2,3,4,5,6,7,8,9}
s1={1,2,3,4,5}
s2={6,7,8,9,4}
print(s1|s2)#union
print(s1&s2)#intersection
print(s1-s2)#setdifference
print(s2-s1)#setdifference
print(s1^s2)#symmetric_difference
print(s.issuperset(s2))
print(s1.issubset(s))


# In[79]:


s={3,4,5,6,7,8,9,1,2}
print(s)
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(sorted(s,reverse=True))


# In[80]:


s=frozenset([1,2,3,4])
print(s)


# In[87]:


s={1,2,3,4,5}
print(dict(enumerate(s)))
print(list(enumerate(s)))
print(tuple(enumerate(s)))
print(enumerate(s))

