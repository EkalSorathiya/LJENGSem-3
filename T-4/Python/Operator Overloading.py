#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return Book(self.pages+other.pages)
b1=Book(100)
b2=Book(200)
b3=Book(400)
t=b1+b2+b3
print(t.pages)


# In[20]:


class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return Book(self.pages+other.pages)

    def __str__(self):
        return f"{self.pages}"
    
b1=Book(100)
b2=Book(200)
b3=Book(400)
t=b1+b2+b3
print(t)


# In[19]:


class A:
    def __str__(self):
        return f"object"

a=A()
print(a)


# In[5]:


# using mul ol cal total salary. emp class has name and salary per day time sheet class has attribut name no of days

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
        
    def __mul__(self,e):
        return self.days*e.salary
    
e=Employee("Ekal",500)
t2=TimeSheet("jaynish",500)
print(t2*e)


# In[6]:


# to add to fraction numbers using + ol

class Fraction:
    def __init__(self,n,d):
        self.n=n        
        self.d=d
    def __add__(self,other):
        n=self.n*other.d+self.d*other.n
        d=self.d*other.d
        return f"{n}/{d}"
    
c1=Fraction(1,2)
c2=Fraction(1,3)
print(c1+c2)


# In[8]:


class A:
    pass
class B:
    pass
class C(A,B):
    pass
c=C()
C.mro()

