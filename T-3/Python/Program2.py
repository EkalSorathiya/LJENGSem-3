#!/usr/bin/env python
# coding: utf-8

# In[18]:


f=open("ireverse.txt",'r')
data1=f.readline()
data2=data1.split()
print(data2)
data3=[]
for i in data2:
    if i[0]=="i" or i[0]=='I':
        d=i[::-1]
        data3.append(d)
    else:
        data3.append(i)        
f.close()
print(data3)


# In[68]:


# for python file to remove comment lines 
f=open("python#.txt",'r')
fw=open("python#write.txt",'w')
while True:
    data=f.readline()
    if len(data)!=0:
        if data[0]=="#":
            continue
        if "#" in data:
            for i in range(1,len(data)):
                if data[i]=="#":
                    fw.write(data[0:i]+"\n")
        else:
            fw.write(data)
    else:
        break


# In[80]:


# to read data from 2 diff files and find dirst difference occured at which line no and index number
f1=open("filediff1.txt",'r')
f2=open("filediff2.txt",'r')

data1=f1.readlines()
data2=f2.readlines()
for i,j in enumerate(data1):
    if j!=data2[i]:
        for p,q in enumerate(j):
            if q!=data2[i][p]:
                print("Line No.-",i+1)
                print("Index No.-",p)
                break
        break


# In[ ]:




