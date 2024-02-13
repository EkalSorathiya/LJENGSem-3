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

