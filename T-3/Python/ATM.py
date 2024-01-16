#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ATM init menue method for creat pin change pin to check balance widthdraw exit  

class ATM:
    
    def __init__(self):
        self.pin=""
        self.balance=50000
        self.menu()
        
    def menu(self):
        print("-----ATM-----")
        print("1-create pin")
        print("2-Change pin")
        print("3-Check Balance")
        print("4-withdrawal")
        print("0-Exit")
        print("-------------")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            pin=input("Enter Your pin: ")
            createPin(pin)
        elif choice ==2:
            changePin()
        elif choice==3:
            checkBalance()
        elif choice==4:
            amount=int(input("Enter Amount To Withdraw: "))
            withdraw(amount)
        
    def createPin(self,pin):
        if len(pin)==4:
            self.pin=pin
            print("Pin Create Successfully")
            self.menu()
        else:
            print("Enter 4 Digit Pin")
            self.menu()
            
    def changePin(self):
        opin=input("Enter Old Pin: ")
        if opin==self.pin:
            npin=input("Enter New Pin")
            createPin(npin)
        else:
            print("Incorrect Pin")
            self.menu()
    def checkBalance(self):
        print("Your Current Balance is - ",self.balance)
        self.menu()
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("You Need More Fund To Withdraw")
            self.menu()
        else:
            


# In[ ]:




