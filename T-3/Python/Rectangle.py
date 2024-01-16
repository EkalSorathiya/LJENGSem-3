#!/usr/bin/env python
# coding: utf-8

# In[1]:


# rectangle class which has attribute length and width create perimeter method to return pereofrect area 
# display length width area pere


# In[11]:


class Rectangle:
    count=0
    def __init__(self,length,width):
        self.length=length
        self.width=width
        Rectangle.count+=1
    def perimeter(self):
        return (2*(self.length+self.width))
    
    def area(self):
        return (self.length*self.width)
        
    def display(self):
        print("Total Rectangle: ",Rectangle.count)
        print("Length: ",self.length)
        print("Width: ",self.width)              
        print("Area: ",self.area())              
        print("Perimeter: ",self.perimeter())              
              
r1=Rectangle(10,20)
r2=Rectangle(20,20)
Rectangle(10,10).display()
r2.display()


# In[ ]:




