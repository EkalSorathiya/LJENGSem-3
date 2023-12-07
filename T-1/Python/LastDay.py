#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hardy ramanujan number
for n in range(1,5000):
    m=int(n**(1/3))+1
    for a in range(1,m):
        for b in range(a,m):
            for c in range(1,m):
                for d in range(c,m):
                    if a**3+b**3==n and c**3+d**3==n:
                        if a!=c:
                            print(f"{n}={a}^3+{b}^3")
                            print(f"{n}={c}^3+{d}^3")
                            


# In[1]:


#wap to print number between a to b divided by c
a=int(input("Enter A:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
for i in range(a,b+1):
    if i%c==0:
        print(i)


# In[1]:


n=int(input("Enter Single Digit Number"))
for i in range(100000,1000000):
    p=1
    for d in str(i):
        p=p*int(d)
    if p==n:
        print(i)


# In[3]:


#find happy number from 1 to 100 

for i in range(1,101):
    n=i
    while(n!=1 and n!=4):
        r=s=0
        while(n>0):
            r=n%10
            s=s+(r**2)
            n=n//10
        n=s
    if(n==1):
        print(i)
        


# In[ ]:




