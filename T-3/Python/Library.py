#!/usr/bin/env python
# coding: utf-8

# In[ ]:


add book
display books 
title auther name and publisher name 


# In[24]:


class Library:

    def __init__(self):
        self.bname=[]       
        self.aname=[]        
        self.pname=[]
        
        
    def book(self):
        name=input("Enter Title")
        author=input("Enter Auther Name")
        publisher=input("Enter Publisher Name ")
        self.bname.append(name)
        self.aname.append(author)        
        self.pname.append(publisher)
    def display(self):
        for i in range(1):
            print("Book Name: ",self.bname[i])
            print("Book Author: ",self.aname[i])            
            print("Book Publisher: ",self.pname[i])  


b1=Library()
b1.book()
b1.display()


# In[ ]:




