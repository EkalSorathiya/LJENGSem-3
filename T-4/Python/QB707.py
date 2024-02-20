#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Respondent:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.rank=3
        self.free=True
    
    def recive_call(self):
        print("Call Recived By ",self.name)
        self.free=False
        
    def end_call(self):
        print("Call Ended")
        self.free=True
        
    def is_free(self):
        return self.free
        
    def get_rank(self):
        return 3
        
        
class Manager:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.rank=2
        self.free=True
        
    def recive_call(self):
        print("Call Recived By ",self.name)
        self.free=False
        
    def end_call(self):
        print("Call Ended")
        self.free=True
        
    def is_free(self):
        return self.free
        
    def get_rank(self):
        return 2
        
        
class Director:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.rank=1
        self.free=True
    
    def recive_call(self):
        print("Call Recived By ",self.name)
        self.free=False
        
    def end_call(self):
        print("Call Ended")
        self.free=True
        
    def is_free(self):
        return self.free
        
    def get_rank(self):
        return 1
        
        
        
class Call:
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.assigned=False

class CallHandler:
    
    respondents=[]
    manager=[]
    directors=[]
    
    def add_employee(self,employee):
        if employee.get_rank()==3:
            self.respondents.append(employee)
        elif employee.get_rank()==2:
            self.manager.append(employee)
        elif employee.get_rank()==1:
            self.directors.append(employee)
        
    def dispatch_call(self,Call):
        
        for i in self.respondents+self.manager+self.directors:
            if i.is_free():
                i.recive_call()
                Call.assigned=True
                break
                
        else:
            print("Sorry! All employees are currently busy.")
                
                
                
r1=Respondent(1,"Ekal")
r2=Respondent(2,"Jaynish")
r3=Respondent(3,"Hetali")

m1=Manager(4,"Aknsha")
m2=Manager(5,"Vraj")
                
d1=Director(6,"Chirag")
    
    
callhandler=CallHandler()
callhandler.add_employee(r1)
callhandler.add_employee(r2)
callhandler.add_employee(r3)
callhandler.add_employee(m1)
callhandler.add_employee(m2)
callhandler.add_employee(d1)



call1 = Call(101, "John Doe")
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)
callhandler.dispatch_call(call1)


# In[ ]:




