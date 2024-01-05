#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f=open("a.txt","w")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# In[ ]:


f=open("a.txt","r")
print(f.read())


# In[ ]:


f=open("a.txt","w")
print(f.read(5)) 
f.close()


# In[ ]:


f=open("a.txt","r") 
print(f.readline(1)) 
print(f.readline(5)) 
print(f.readline(4)) 
print(f.readline(40)) 
f.close()


# In[ ]:


f=open("a.txt","r") 
print(f.readlines())
f.close()


# In[ ]:


# WAP to count number of line from text file

f=open("a.txt","r") 
l=f.readlines()
count=len(l)
f.close()
print(count)


x=0
f=open("a.txt","r") 
for i in f:
    x+=1
print(x)
f.close()


# In[ ]:


# wap to display odd number of lines from text file
f=open("a.txt","r") 
l=f.readlines()
print(l[::2])
f.close()


# In[ ]:


f=open("a.txt","r") 
c=0
for i in f:
    if c%2==0:
        print(i)
    c=c+1


# In[ ]:


f=open("a.txt","r")
vd=f.read(5)
print(vd)
print(f.tell())
d=f.read()
print(d)
f.seek(0)
print(f.tell())
f.close()


# In[ ]:


# to ask user for name and age and into file

name=input("Enter Your Name:")
age=int(input("Enter Your age:"))
f=open("NameAge.txt","w")
f.write("My name is "+name)
f.write("\nMy age is "+str(age))
f.close()


# In[ ]:


f=open("NameAge.txt","r")
print(f.read())
f.close()


# In[ ]:


f1=open("f1.txt","w")
f2=open("f2.txt","w")
f1.write("1\n")
f1.write("2\n")
l2=['a\n','b\n','c\n','d\n','e\n']
f2.writelines(l2)
f1.close()
f2.close()

r1=open("f1.txt","r")
r2=open("f2.txt","r")
l1=r1.readlines()
l2=r2.readlines()
f3=open("f3.txt","w")
for i in range(len(max(l1,l2))):
    if len(l1)>i:
        f3.write(l1[i])
    if len(l2)>i:
        f3.write(l2[i])
f1.close()
f2.close()
f3.close()


# In[2]:


# which display 25 lines at a time from the file after 25 lines each time to ask the user to press any key to continue
f=open("read25.txt","r")
data=f.readlines()
a=0
b=25
while True:
    if b<=len(data):
        choice=input("Press c Key To Continue or 0 for exit")
        if choice=="0":
            break
        elif choice=="c":
            for i in range(a,b):
                print(str(data[i]))
            a=b
            b=a+25
    else:
        break
f.close()



OR

f=open("read25.txt",r)


# In[9]:


# to remove line entered by user and write content to another file
f=open("delline.txt","r")
data=f.readlines()
f.close()

line=int(input("Enter Line Number:"))
w=open("writeline.txt","w")
w.writelines(data[:line-1])
w.writelines(data[line:])
w.close()


# In[3]:


with open("writeline.txt","r") as f:
    print(f.read())
print(f.closed)


# In[7]:


get_ipython().run_cell_magic('writefile', 'abc.txt', 'Hii\nHello\nPython')

