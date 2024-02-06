#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Vehicle:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
    def fuel(self):
        print("Diesel")
        
class Car(Vehicle):
    def fuel(self):
        print("Petrol")
        
c=Car("BMW")
c.display()
c.fuel()


# In[ ]:


def 

