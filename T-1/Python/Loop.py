#!/usr/bin/env python
# coding: utf-8

# In[11]:


for i in range(10,11,-2):
    print(i)


# In[19]:


for i in range(10,0,-1):
    if i==5:
        continue
    print(i)
    
        
        


# In[32]:


for i in range(10,5,-1):
    if i==7:
        continue
    print(i)
else:
    print("Hello")
    print(i)


# In[31]:


i=1
while i<=5:
    print("Ekal")
    i+=1
else:
    print(i)


# In[33]:


#wap to print multiplication table 

num=int(input("Enter the Number:"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)


# In[14]:


#find factorial

num=int(input("Enter Number:"))
fact=1

for i in range(1,num+1):
    fact=fact*i
print(fact)


# In[29]:


num=int(input("Enter Number:"))
a=0
b=1
print(a,b,end=" ")
for i in range(num-2):
    
    c=a+b
    print(c,end=" ")
    a=b
    b=c


# In[13]:


# find prime number from given range by user

a=int(input("Enter start range:"))
b=int(input("Enter end range:"))

for i in range(a,b+1):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
    if(f==0):
        print(i," is Prime Number")


# In[3]:


#wap to check entered number is palindrome


a=int(input("Enter number:"))
rev=0
temp=a

while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10

if(temp==rev):
    print("palindrome")
else:
    print("Not Palindrome")


# In[26]:


# armstrong number
a=int(input("Enter Number:"))
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


# In[32]:


#HCF AND LCM



a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))

hcf=1

for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        hcf=i

print("HCF is =",hcf)

lcm=(a*b)/hcf

print("LCM is =",lcm)


# In[45]:


# Strong Number

num=int(input("Enter Number:"))
temp=num
s=0

while(num!=0):
    d=num%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    s=s+fact
    num=num//10

if(temp==s):
    print("Strong Number")
else:
    print("Not Strong Number")
    
  


# In[51]:


#Perfect Number

a=int(input("Enter Number:"))
temp=a
s=0

for i in range(1,a):
    if a%i==0:
        s=s+i
        
if(temp==s):
    print("Perfect Number")
else:
    print("No Perfect Number")

