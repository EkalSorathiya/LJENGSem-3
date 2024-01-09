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


# In[14]:


f=open("Word80.txt","r",encoding='utf-8')

l=[]
def text_line(a):
    if len(a)<=80:
        l.append(a)
    else:
        if [79]==" ":
            l.append(a[:80])
            text_line(a[80:])
        elif a[79]!=" ":
            ind=a.rfind(" ",0,79)
            l.append(a[:ind+1])
            text_line(a[ind+1:])
for i in f:
    if len(i)<=80:
        l.append(i)
    else:
        text_line(i)
print(l)
f.close()

f=open("Read80.txt","w")
for x in l:
    if x[-1]==" ":
        x=x[0:-1]+"\n"
    else:
        x=x+"\n"
    f.write(x)
f.close()


# In[13]:


# using a file which consist of multiple stat find all the words from the file that can be made from all the char of given user string 

user=input("Enter String: ")
d={}
for i in user:
    d[i]=d.get(i,0)+1
    
f=open("Word80.txt","r")
for line in f:
    for j in line.split():
        e={}
        for x in j:
            e[x]=e.get(x,0)+1
        flag=True
        
        for k in d:
            if k not in e or d[k]>e[k]:
                flag=False
        if flag:
            print(j)

