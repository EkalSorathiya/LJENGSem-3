#!/usr/bin/env python
# coding: utf-8

# In[5]:


s="Python is very polular language!!"
print(s[5])
print(s[-5])


# In[60]:


s="Python is very polular language!!"
print(s[-1:-5:2])
del s
print(s)


# In[72]:


s1="java"
s2="python"
s4="Ekal"
s5="Ekal"
print(s1+s2)
print(id(s4))
print(id(s5))
str="Hello "
print(id(str))
str+="Student"
print(id(str))
print(s3=35)
print(s1+s3)
print(s1*3)


# In[89]:


str="Ekal  "
index=0
for i in str:
    print(index,"--",i)
    print("ekal")
    index+=1
    


# In[102]:


str="Ekal"
for a,b in enumerate(str):
    print(a,"--",b)

print("E" in str)
print("D" not in str)


# In[109]:


str="Ekal"
print(len(str))
print(min(str))
print(max(str))
print(sorted(str))
print(sorted(str,reverse=True))


# In[3]:


str="Ekal Sorathiya"
print(dir(str))
print(str.title())
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.count("E"))
print(str.count(str))
print(str.find("E",2,len(str)))
print(str.rfind("E",2,len(str)))
print(str.rfind("a"))
s="Ekal"
print(s.isidentifier())


# In[7]:


#wap to calculate sum and avg of the digits present in given string s abc8hijg23klm56
s ="abc8hijg23klm56"
sum=0
count=0
for i in s:
    if i.isdigit()==True:
        sum=sum+int(i)
        count+=1
print("sum is ",sum)
print("Average",sum/count)


# In[ ]:




