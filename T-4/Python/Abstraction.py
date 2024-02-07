#!/usr/bin/env python
# coding: utf-8

# In[7]:


from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,name):
        self.name=name
       
    @abstractmethod
    def draw(self):
        print("Hii")
        
class Circle(Shape):
    def __init__(self):
        super().__init__("Circle")
    
    def draw(self):
        super().draw()
        print(self.name)
        print("Draw A Circle")
        
c=Circle()
c.draw()


# In[ ]:


class Employee(ABC):
    def getEmployee(self):
        self.name=input()        
        self.id=input()        
        self.salary=int(input())
        
    def printEmployeeDetails()

