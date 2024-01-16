#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Stack Queue it should contain following method init holds list shift which return the first 
# element and remove the element unshift pushes a new element at front of list push add a new element at the end of list 
# pop method  returns the last element and remove from the last displayt mentid returns the 
# content of the list generate custom exception shift and pop method if there are no element in the list
class StackQueue:
    def __init__(self):
        self.sq=["Ekal","Jaynish","chirag"]
        
    def shift(self):
        if len(self.sq)==0:
            raise Exception("List Is Empty") 
        try:
            print(self.sq[0])
            self.sq.pop(0)
        except Exception:
            print(Exception)
            
    def unshift(self,element):
        self.sq[0]=element
        print(self.sq)
        
    def push(self,element):
        self.sq.append(element)
        print(self.sq)
        
    def pop(self):
        if len(self.sq)==0:
            raise Exception("List Is Empty") 
        try:
            print(self.sq[-1])
            self.sq.pop()
        except Exception:
            print(Exception)
            
    def display(self):
        print(self.sq)
        

s1=StackQueue()
s1.shift()
s1.display()
s1.unshift("ABC")
s1.display()


# In[ ]:




