#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Word play init that holds list of words it should havbe following method word with 
# length return a list of all words of given length start with end with 
# palindrome avoid 


# In[20]:


class WordPlay:
    
    def __init__(self):
        self.wordList=["ekal",'jaynish',"chirag","varj","Krashna","nandini","maam"]
    
    def word_length(self,length):
        l1=[]
        for i in self.wordList:
            if len(i)==length:
                l1.append(i)
        print("Word Length:",l1)
            
    def start_with(self,sw):
        l1=[]
        for i in  self.wordList:
            if i.startswith(sw):
                l1.append(i)
        print("Word Start With:",l1)
                
                
    def ends_with(self,ew):
        l1=[]
        for i in  self.wordList:
            if i.endswith(ew):
                l1.append(i)
        print("Word ends With:",l1)
    def only(self,only):
        l1=[]
        
        for i in self.wordList:
            if set(only)==set(i):
                l1.append(i)
        print("Only:",l1)
        
    def avoid(self,avoid):
        l1=[]
        for i in self.wordList:
            if set(i) & set(avoid)==set():
                l1.append(i)
        print("Avoid :",l1)
        
    def pali(self):
        l1=[]
        for i in self.wordList:
            if i == i[::-1]:
                l1.append(i)
        print("Palindrome: ",l1)
        
wp=WordPlay()

wp.word_length(4)
wp.ends_with("i")
wp.start_with("j")
wp.only("ekal")
wp.avoid("j")
wp.pali()

