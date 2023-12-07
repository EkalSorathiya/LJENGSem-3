#!/usr/bin/env python
# coding: utf-8

# In[8]:


for i in range(1,6):
    for j in range(i):
        print(" ",end=" ")
    for k in range(i,6):
        print(" ",k,end=" ")
    print()
for i in range(2,6):
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(5,5-i,-1):
        print(" ",k,end=" ")
    print()


# In[34]:


for i in range(1,6):    
    for k in range(1,10):
        if(i==1 and k==5) or (i==2 and k==4) or (i==2 and k==5) or (i==3 and (k==3 or k==4 or k==5)) or (i==4 and k==2) or (i==4 and k==7) or (i==5 and k==1) or (i==5 and k==8):
            print(" * ",end=" ")  
        else:
            print(" ",end=" ")
    print()


# In[43]:



for i in range(4):
    k=65
    l=97
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


# In[49]:



for i in range(5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()


# In[33]:


#wap that prompts the user to enter the numbers and stops when its done after this print the avg min and max number among them
count=0
avg=0.0
sum1=0
min2=-99999
max2=0

print("0-stop")
while(True):
    enter=int(input("Enter Number:"))
    if enter==0:
        break
    count=count+1
    sum1=sum1+enter
    avg=sum1/count

    
    if count==1:
        min1=max1=enter
    if enter>max1:
        max2=max1
        max1=enter
    elif enter>max2 and enter!=max1:
        max2=enter
    
    if enter<min1:
        min2=min1
        min1=enter
    elif enter<min2 and enter!=min1:
        min2=enter
        

print("Average=",avg)
print("count=",count)
print("Sum=",sum1)
print("Minimum=",min1)
print("S Maximum=",max2)
print("S Minimum =",min2)

