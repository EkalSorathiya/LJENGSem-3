#!/usr/bin/env python
# coding: utf-8

# In[3]:


# name acc no balance 
# constructoe acc no name and balance 
# deposit method which manage deposit action 
# withdrawl method 
# diasplay method 


# In[7]:


class BankAccount:    
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
        
    def deposit(self,damount):
        self.balance=self.balance+damount
        print("Your Total Balance Is :",self.balance)
    print("---------------------")
        
    def withdraw(self,withdraw):
        if withdraw>self.balance:
            print("You have Insufficient Amount")
            print("---------------------")    
        else:
            self.balance=self.balance-wamount
            print("Your Total Balance Is :",self.balance)
            print("---------------------")
            
        
    def display(self):
        print("Account Number :",self.accno)        
        print("Name :",self.name)        
        print("Balance :",self.balance)
        print("---------------------")
        
while True:
    print("---------------------")
    print("1 - Create Account")
    print("2 - Deposit Amount")
    print("3 - Withdraw Amount")
    print("4 - View Your Bank Details")
    print("5 - Exit")
    print("---------------------")
    
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        accno=int(input("Enter 4 Digit Account Number"))
        name=input("Enter Your Name: ")
        balance=int(input("Enter Initial Balance: "))
        b1=BankAccount(accno,name,balance)
    if choice == 2:
        damount=int(input("Enter Deposit Amount: "))
        b1.deposit(damount)
        
    if choice == 3:
        wamount=int(input("Enter Withdraw Amount: "))
        b1.withdraw(wamount)
        
    if choice==4:
        b1.display()
    
    if choice == 5:
        break
    
    else:
        print("Invalid Choice")

