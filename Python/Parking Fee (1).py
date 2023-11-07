#!/usr/bin/env python
# coding: utf-8

# In[22]:


#wap calculate parking fees 
'''
hr<3                   hr>3
truck or bus =20       truck or bus =30
car=10                 car=20 
2wh= 5                 2 wh=10 '''

hr=int(input("Enter Entry Hour:"))
mi=int(input("Enter Entry Minute:"))
hrexit=int(input("Enter Exit Hour:"))
miexit=int(input("Enter Exit Minute:"))
print("1-truck or bus \n2-car\n3-bike")
choice=int(input("Enter Your choice:"))

if hrexit<hr:
    hrexit=hrexit+24 
hr_parking_time=hrexit-hr
min_parking_time=miexit-mi

if(hr_parking_time<=3 and min_parking_time<=0) or(hr==hrexit) or (min_parking_time<=0 and hr_parking_time==3):
    if(choice==1):
        rate=20
    elif(choice==2):
        rate=10
    elif(choice==3):
        rate=5
    else:
        print("Invalid Input")
elif (hr_parking_time>3) or (hr_parking_time==3 and min_parking_time>0) :
    if(choice==1):
        rate=30
    elif(choice==2):
        rate=20
    elif(choice==3):
        rate=10
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
    
    
print("choice=",choice)
print("Entry hour=",hr)
print("Entry minute=",mi)
print("Exit hour=",hrexit)
print("Exit minute=",miexit)
print("Rate=",rate)


