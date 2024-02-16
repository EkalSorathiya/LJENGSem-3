#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([8,6,4,2,9])
plt.plot(x,y,marker='o',color='green',ms=10)
plt.xlabel("x-axis",size=30,family='serif')
plt.ylabel("y-axis")
plt.title("My Graph")
plt.show()


# In[ ]:





# In[41]:


# line graph for diff class (a1 to a8) vs avg marks of that class
x=np.array(['a1','a2','a3','a4','a5','a6','a7','a8'])
y1=np.array([50,72,72,64,96,71,46,90])
y2=np.array([39,36,82,84,35,91,67,90])
plt.subplot(1,2,1)
plt.plot(x,y1,"o:m",mec='black',mfc='red')
plt.xlabel("Class")
plt.ylabel("AVG. Marks")
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.xlabel("Class")
plt.ylabel("AVG. Marks")
plt.suptitle("School")
plt.show()


# In[16]:


# to plot 6 diff sub plot with two rows and 3 columns 
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y1=np.array([6,7,8,9,10])
y2=np.array([5,3,8,9,10])
y3=np.array([6,7,8,7,3])
y4=np.array([6,5,8,9,10])
y5=np.array([6,2,8,9,1])
y6=np.array([6,7,8,1,8])
plt.subplot(2,3,1)
plt.plot(x,y1)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-1")
plt.subplot(2,3,2)
plt.plot(x,y2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-2")
plt.subplot(2,3,3)
plt.plot(x,y3)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-3")
plt.subplot(2,3,4)
plt.plot(x,y4)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-4")
plt.subplot(2,3,5)
plt.plot(x,y5)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-5")
plt.subplot(2,3,6)
plt.plot(x,y6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph-6")
plt.suptitle("My Graph")
plt.tight_layout()
plt.savefig("My Graph")
plt.show()


# In[33]:


import numpy as np
import matplotlib.pyplot as plt

x=np.array(['ps','de','fsd','py','etc'])
y1=np.array([91,83,70,84,50])
y2=np.array([94,80,60,60,80])
y3=np.array([97,97,89,70,0])
plt.plot(x,y1,"o-r",label="STD-1")
plt.plot(x,y2,"x:b",label="STD-2")
plt.plot(x,y3,"o--m",label="STD-3")
plt.legend()
plt.show()


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
d={'a':30,'b':40,'c':40,'d':50,'e':60}
x=list(d.keys)
y=list(d.values)


# In[46]:


# to plot a bar graph of sell department and purchase department emp detailsgiven in dict apply xlabe ylabel title
# legend in graph
purchase={"101":10000,"120":20000,"140":32000,"108":45000}
sales={"128":25000,"118":21000,"145":30000,"107":48000}
x=list(purchase.keys())6
y=list(purchase.values())
plt.bar(x,y)
x1=list(sales.keys())
y1=list(sales.values())
plt.bar(x1,y1)
plt.scatter(x1,y1)
plt.legend()
plt.axis('off')
plt.show()


# In[47]:


data=[1,2,4,9,8,5,2,3,4,6,2,5,4,7,8,5,3,2,5]
plt.hist(data)


# In[25]:


import numpy as np
import matplotlib.pyplot as plt

data={'Apple':35,'Banana':30,'Cherry':26,'Grapes':40,'Oranges':35}
x=list(data.values())
mylabel=list(data.keys())
plt.pie(x,labels=mylabel,colors=['red','orange','green','yellow','brown'],autopct='%0.1f%%',explode=[0,0,0,0.1,0])
plt.title("Fruits")
plt.legend()
plt.show()


# In[3]:


#write a python to create class called matrix  which contain constructor to initialize rows and columns it has method that has no. 
# of rows get no. od columns set elements of matrix  add method to add two matrix
# multi method to multi 2 matrix if the martix can not be added or multi display operation not possible
# use operator overloading 
import numpy as np
class Matrix:
    def __init__(self,row,clm):
        self.matrix=np.zeros((row,clm))
        self.row=row
        self.clm=clm
    def get_row(self):
        return self.row
    def get_clm(self):
        return self.clm
    def set_element(self,i,j,value):
        self.matrix[i][j]=value
    def __add__(self,other):        
        if self.row!=other.row or self.clm!=other.clm:
            print("Operation Not Possible")
            return
        result =Matrix(self.row,self.clm)
        result.matrix=np.add(self.matrix,other.matrix)
        return result
    
    def __str__(self):
        return str(self.matrix)
    
m1=Matrix(2,2)
m1.set_element(0,0,1)
m1.set_element(0,1,2)
m1.set_element(1,0,3)
m1.set_element(1,1,4)
m2=Matrix(2,2)
m2.set_element(0,0,1)
m2.set_element(0,1,2)
m2.set_element(1,0,3)
m2.set_element(1,1,4)
print(m1,'\n',m2)
print(m1+m2)


# In[ ]:




