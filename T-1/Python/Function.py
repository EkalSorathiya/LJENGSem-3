#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Default Argument

def d1(name="ABC",m):
    print("Hello",name,m)
    
d1("Ekal")
d1()


# In[38]:


#variable length argument

def d1(*n):
    for i in n:
        print(i)
        
d1(1,2,3,4,5)


# In[48]:


#variable length argument

def d1(*n,s):
    for i in n:
        print(i)
    print(s)
d1(1,2,3,4,5,s=10)


# In[64]:


def d1(*m,**n):
    for k,v in n.items():
        print(k,'=',v)
        
    for i in m:
        print(i)
d1(1,2,3,5,A=1,B=2,C=3,D=4)


# In[70]:


b=5
def d1():
    global b
    b=7
    print(b)
d1()

def d2():
    print(b)
d2()


# In[3]:


#wap to find armstrong number using user dfine function


def arm(a):
    temp=a
    power=len(str(a))
    s=0
    while(a>0):
        d=a%10
        s=s+(d**power)
        a=a//10

    if(s==temp):
        print("armstrong Number")
    else:
        print("Not Armstrong Number")

a=int(input("Enter Number:"))
arm(a)


# In[5]:


def d(x,y=3,*z):
    sum=x-y
    for i in z:
        sum+=i
    return sum
print(d(1,5,7,4,3))





# In[37]:


days=int(input("Enter Days:"))
w=days//7
mon=1
sun=7
s=0
for i in range(w):
    for j in  range(mon,sun+1):
        s=s+j
    mon+=1
    sun+=1
for k in range(days%7):
    s=s+mon
    mon+=1
    
print("Sum is ",s)


# In[35]:


def f(a,*b,c=6,**d):
    print(a,b,c,d)

f(1,2,3,c=7,x=4,y=5)


# In[69]:


def collatz(num):
    while num>1:
        print(num,end=" ")
        if(num%2):
            num=(3*num)+1
        else:
            num=num//2
    print(1)
        
num=int(input("ENter Number"))
collatz(num)


# In[121]:


k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()


# In[183]:


for i in range(6):
    
    for j in range(i,6):
        print("",end=" ")
        
    for k in range(0,i+1):
        print("*",end=" ")
    print()

    
for i in range(7,0,-1):
    
    for j in range(i,7):
        print("",end=" ")
        
    for k in range(0,i):
        print("*",end=" ")
    
    print()


# In[ ]:




