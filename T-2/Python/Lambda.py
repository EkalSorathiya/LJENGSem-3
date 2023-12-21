#!/usr/bin/env python
# coding: utf-8

# In[5]:


s=lambda x:"Even" if x%2==0 else "Odd"
print(s(10))
print(s(11))
a=lambda x,y:x+y
print(a(10.5,10))


# In[15]:


l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5]
sq=lambda x:x*x
s=list(map(sq,l1))
s1=set(map(lambda x,y:x**x+y**y,l1,l2))
s1=tuple(map(lambda x,y:x**x+y**y,l1,l2))
s1=list(map(lambda x,y:x**x+y**y,l1,l2))
print(s)
print(s1)


# In[20]:


l1=[1,2,3,4,5,6]
from functools import *
r=reduce(lambda x,y:x+y,l1)
print(r)


# In[24]:


l=[1,2,3,4,5,6,7,8,9,10]
f=set(filter(lambda x:x %2==0,l))
f=tuple(filter(lambda x:x %2==0,l))
f=list(filter(lambda x:x %2==0,l))
print(f)


# In[29]:


# using lambda fun to get list whose elemenet are divisible 13 and 19
l=[13,18,123,51,247]
s=list(filter(lambda x:x%13==0 and x%19==0,l))
print(s)


# In[32]:


# to segrigate two diff list with positive and nevative number

l=[1,2,-3,0,4,-5,6,7,-8,9]
p=list(filter(lambda c:c<0,l))
print(p)
n=list(filter(lambda c:c>=0,l))
print(n)


# In[68]:


# for encrypt the string with rail fence cipher technique in rail fence cipher you can break string by any int number like 2,3,4
# also decrypt the same key value 


    


# In[77]:


s="This Message Is For Ekal"
k=3
m=""

for i in range(key):
    m+=s[i::3]
print(m)

l=len(s)
p=l//k
e=l%k

p1=m[:(p+1)*e]
p2=m[(p+1)*e:]
msg=""

for i in range(p+1):
    if i<p:
        msg+=p1[i::p+1]+p2[i::p]
    else:
        msg+=p1[i::p+1]    
print(msg)    


# In[84]:


# wap to create a dict from a string in which key is a first letter of word and value is list of words in that start with the key

s="wap to create a dict from a string in which key is a first letter of word and value is list of words in that start with the key"

l=s.split()
d={}
for i in l:
    fc=i[0].lower()
    if fc in d:
        d[fc].append(i)
    else:
        d[fc]=[i]
    
print(d)


# In[6]:


# all passible combination of 3 digit
l=[1,2,2]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and k!=i:
                print(str(l[i])+str(l[j])+str(l[k]))
            elif k==j:
                print(str())


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


# a company has decided to give gifts the employee for that company has given the rank to each emp based on the ranlk company has mads certai rules to distribue the gift each emp must recive atlest 1 gigt emp having higher ranking get > number of gigt then their neighbours what is the min no. of gift req by the company

test=int(input("Enter No. of Test Case"))

while test>0:
    sumgift=0
    
    n=int(input("Enter No. of Employee"))
    a=list(map(int,input().split()))
    gift=[1]
    
    for i in range(1,n):
        if a[i]>a[i-1]:
            gift.append(gift[i-1]+1)
            
        else:
            gift.append(1)
    
    print(gift)
    for i in range(n-2,-1,-1):
        if a[i]>a[i+1]:
            gift[i]=max(gift[i+1]+1,gift[i])
    print(gift)
    for i in gift:
        sumgift+=i
    print(sumgift)
    test=test-1
        


# In[24]:


# longest common per fix from the given list of given string if there is no prefix then return -1
a=['lesson','less','length']
size=len(a)
if size==0:
    print("Nothing")
if size==1:
    print(a[0])
a.sort()
end=min(len(a[0]),len(a[-1]))
i=0

pre=""
while (i<end and a[0][i]==a[-1][i]):
    
    i=i+1
    pre=a[0][0:i]
    
if(pre==""):
    print(-1)
else:
    print(pre)


# In[23]:


# to rotate nXn matrix by 90 deg clockwise write proper code to take input of n from user and then take input of nXn matrix from user print the original matrix and 90 deg colckwise matrix
# note: you are not allowed extra list or tuple to do the rotation of matrix you need to make changes in that matrix itself to rotate 


n=int(input("Enter N"))
matrix=[]

for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input("Enter Number")))
    matrix.append(a)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
    
for i in range(n):
    for j in range(i,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
    
    
for i in matrix:
    i.reverse()
        
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

