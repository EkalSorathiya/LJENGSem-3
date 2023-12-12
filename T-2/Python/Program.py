#!/usr/bin/env python
# coding: utf-8

# In[4]:


l=[1,2,3]
l1=l
l1[0]=5
print(l)
print(l1)

print(list(enumerate(l)))
print(list(enumerate(l,5000)))


# In[25]:


#wap to generate list of words of string entered by user in which 1st end last will be capital of each word

s=input("Enter Statement")
l=s.split()
l1=[]
for i in l:
    if len(i)>1:
        l1.append(i[0].upper()+i[1:-1]+i[-1].upper())
    else:
        l1.append(i[0].upper())

print(l1)
        


# In[42]:


#wap to shift the number towards left side if the shift is > len of number then reverse the number
num=int(input("Enter Number"))
shift=int(input("Enter Shift"))
n1=str(num)
if shift>len(n1):
    new=n1[::-1]
else:
    new=n1[shift:]+n1[:shift]
print(new)


# In[61]:


#wap to sort the list in such a mannar that 1st element is smallest element of list 2nd element largest element 
#of list 3rd elemenet is smallest of remaining 4th largest element of it and so on

l=[1,3,44,5,7,11]
length=len(l)
i=0
l2=[]
while i<length:
    if i%2==0:   
        l2.append(min(l))
        l.remove(min(l))
        i+=1
    else:
        l2.append(max(l))
        l.remove(max(l))
        i+=1
        
print(l2 )


# In[ ]:


#WAP to convert entered string into mirror string

s=input("Enter String")
s1=''
for i in s:
    if i.islower():
        s1=s1+chr(ord('a')+ord('z')-ord(i))
    elif i.isupper():
        s1=s1+chr(ord('A')+ord('Z')-ord(i))
    else:
        s1=s1+" "
        
print(s1)    


# In[ ]:


# wap to count special element from list an element is special if removal of that element makes a 
# list balanced the list will be balanced if  sum of even index element is = the sum of odd index elements 

l=eval(input("Enter List:"))
count=0

for i in range(len(l)):
    a=l.copy()
    a.pop(i)
    sum1=sum(a[0::2])
    sum2=sum(a[1::2])
    if sum1==sum2:
        count+=1
        print("Index of element :",i)

if count!=0:
    print("number of element in list are:",count)
else:
    print("No such element in list")

