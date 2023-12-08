#!/usr/bin/env python
# coding: utf-8

# In[34]:


L=[1,2,"A",4,(1,2)]
print(L[3])
print(L)
L[1]=5
print(L)
del L[1]
print(L)
L.append(9)
print(L)
L.append([5,6])
print(L)
l=[]
l=list("Hello")#return string
print(l)
l=list(("Hello",))#return tuple
print(l)
l=list((1,2,3,4))
print(l)

l3=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(l3[1][1][0])

l1=[1,2,3,[1,2],'abcd']
print(l1[-1:-3:-1][-1][-2])

l2=[1,2,3,4]
l2.extend(('Hello',))
print(l2)
l2.extend(range(5))
print(l2)
l2.extend(['A','B'])
print(l2)


# In[44]:


l=[1,2,3]
l.insert(2,100)
print(l)
l.insert(1,[5,6,7])
print(l)
l1=[5,6,7]
l1[-1]=50
print(l1)
l1[1:2]=[60,70,80]
print(l1)
l1[1]=[60,70,80]
print(l1)


# In[55]:


l=[1,2,3,4,5,6,7]
del l[1]
print(l)
l.remove(5)
print(l)
l.pop()
print(l)
l.pop(2)
print(l)
l.clear()
print(l)
del l
print(l)
l.pop(8)
print(l)
l2.remove(50)


# In[69]:


l1=[1,2,3,4]
print(sum(l1))
print(min(l1))
print(max(l1))
l2=[5,6,7,8]
print(l1+l2)
print(l1*2)
print(1 in l1)
print(l1>l2)
print(len(l1))
i=0
while i<len(l1):
    print(l1[i])
    i+=1
    
for i,j in enumerate(l1):
    print(i,"--",j)


# In[79]:


print(min('ab','k','c'))
l=[8,3,6,1,9,1,0]
l.sort()
print(l)
print(sorted(l,reverse=True))


# In[86]:


l=[1,2,1,(1,2),(3,1)]
print(l.count(1))
print(l.count((1,2)))
print(l.index(1,1,3))


# In[ ]:


# to check strength of password entered by user 
# it hust have minimum 8 char 1 lower case 1 upper case 1 special char 1_ ,1 char digit

import string
while True:
    l=u=s=d=sp=0
    password=input("Enter password:")
    
    if len(password)>=8:
        if '_' in password:
            for i in password:
                if i.islower():
                    l=1
                if i.isupper():
                    u=1
                if i.isdigit():
                    d=1
                if i in string.punctuation:
                    sp=1
            if l==1 and u==1 and d==1 and sp==1 :
                print("Strong Password")
                break
            else:
                print("Week password")
        else:
            print("password must contain _ char")

    else:
        print("password must contain min 8 char")

