#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Olly_pizza:
    def __init__(self):
        self.item=[]
        self.price=[]
        self.size()
        
    def topping(self):
        print("-----------------")
        print("1 - corn")
        print("2 - tomato")
        print("3 - onion")
        print("4 - capsicum")
        print("5 - mushroom")
        print("6 - olives")
        print("7 - broccoli")
        print("8 - Add Cheese")
        print("0 - cancel Order")
        print("-----------------")
        choice=int(input("Enter Your Choice: "))
        
        if choice==1:
            self.price.append(20)
            self.item.append("Topping-Corn     -20")
            self.topping()
        if choice==2:
            self.price.append(20)
            self.item.append("Topping-Tomato   -20")
            self.topping()
        if choice==3:
            self.price.append(20)
            self.item.append("Topping-Onion    -20")
            self.topping()
        if choice==4:
            self.price.append(20)
            self.item.append("Topping-Capsicum -20")
            self.topping()            
        if choice==5:
            self.price.append(50)
            self.item.append("Topping-Mushroom -50")
            self.topping()
        if choice==6:
            self.price.append(50)
            self.item.append("Topping-Olives   -50")
            self.topping()
        if choice==7:
            self.price.append(50)
            self.item.append("Topping-Broccoli -50")

            self.topping()
        if choice == 8:
            self.cheese()
        if choice==0:
            print("You Canclled Your Order")
        
    def cheese(self):
        print("-----------------")
        print("1 - mozzarella")
        print("2 - feta")
        print("3 - cheddar")
        print("4 - Bill")
        print("0 - cancel Order")
        print("-----------------")
        choice=int(input("Enter Your Choice: "))
        
        if choice==1:
            self.price.append(50)
            self.item.append("Cheese-Mozzarella -50")
            self.cheese()
        if choice==2:
            self.price.append(50)
            self.item.append("Cheese-Feta       -50")
            self.cheese()
        if choice==3:
            self.price.append(50)
            self.item.append("Cheese-Cheddar    -50")
            self.cheese()
        if choice==4:
            self.bill()
        if choice==0:
            print("You Canclled Your Order")
        
        
    def size(self):
        print("Welcome To Olly's Pizza")
        print("1 - small pizza")
        print("2 - medium pizza")
        print("3 - large pizza")
        print("0 - Exit")
        print("-----------------")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            self.price.append(50)
            self.item.append("Small Pizza    -50")
            self.topping()
        if choice==2:
            self.price.append(100)
            self.item.append("Medium Pizza   -100")
            self.topping()
        if choice==3:
            self.price.append(200)
            self.item.append("Large Pizza    -200")
            self.topping()

    def bill(self):
        TotalPrice=0
        for i in self.price:
            TotalPrice += i
        for i in self.item:
            print(i)
            print()
        print("Your Total Price For Pizza Is: ",TotalPrice)
        print("Thank You For Visiting😊")

        
class Order:
    def __init__(self,name,ids):
        self.name=name
        self.ids=ids
        self.order()
        
    def order(self):
        self.pizza=[]
        no=int(input("Enter Number of pizza You Want: "))
        for i in range(no):
            self.pizza.append(Olly_pizza())


name=input("Enter Your Name: ")
ids=71
print("Your Order Id Is: ",ids)
o=Order(name,ids)
    

