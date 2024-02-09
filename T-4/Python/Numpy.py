#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(np.__version__)


# In[11]:


import numpy as np
a=np.array(40)
b=np.array([1,2])
c=np.array([[1,2],[3,4]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[7,8,9]]])
print(d.ndim)
print(d)


# In[ ]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6]])


# In[18]:


# to return array of odd rows and even columns for the given sample array
import numpy as np

s=np.array([[3,6,9,12],
   [15,18,21,24],
   [27,30,33,66],
   [39,42,45,48],
   [51,54,57,60]])

print(s[::2,1::2])


# In[1]:


import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
new_array=a.reshape(2,2,2)
print(new_array)


# In[2]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(a):
    print(i)


# In[3]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
for i,j in np.ndenumerate(a):
    print(i,"--",j)


# In[5]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
new_array=np.array_split(a,3)
print(new_array)


# In[7]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
new_array=np.array_split(a,3,axis=1)
print(new_array)


# In[18]:


import numpy as np
a=np.array([1,2,4,3,4,7,8,5,6])
new_array=np.where(a==4)
print(new_array)
print(np.where(a%2==0))
print(np.sort(a))
a1=np.array([[1,2,10,3,4],[5,6,7,9,8]])
print(np.sort(a1))
a2=np.arange(10,15)
print(a2)


# In[46]:


# there is an array of marks of 5 students in four diff subjects persorm the following tasks 1)add marks to every student 
# of extra sub in same array and print the array 2) add two new student in respctive 5 sub and print the array 
# 3) add extra columns with sum of all subjects marks and print the array 
# sort the array non assending order on total marks columns and print the array

import numpy as np
marks=np.array([[13,10,9,33],[63,46,90,42],[39,76,13,29],[82,9,29,78],[67,61,59,36]])
exsub=np.array([[30],[40],[50],[60],[70]])
marks1=np.concatenate((marks,exsub),axis=1)
# print(marks1)
stud6=np.array([[99,40,50,45,97]])
stud7=np.array([[69,46,59,55,46]])
marks2=np.concatenate((marks1,stud6,stud7),axis=0)
# print(marks2)
print()

l=[]
for i in marks2:
    sum=0
    for j in i:
        sum=sum+j
        
    l.append(sum)
sum_stud=np.array(l).reshape(7,1)
marks3=np.concatenate((marks2,sum_stud),axis=1)
# print(marks3)

li=list(marks3)
li=sorted(li,key=lambda x:x[-1],reverse=True)
print(np.array(li))

