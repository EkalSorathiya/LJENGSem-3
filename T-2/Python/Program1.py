#!/usr/bin/env python
# coding: utf-8

# In[8]:


#to return anothr string similar to the input string with case inverted use of swap case function is prohabitated

s=input("Enter String")
s1=""
for i in s:
    if i.islower():
        s1=s1+i.upper()
    else:
        s1=s1+i.lower()
    
print(s1)


# In[22]:


#to create saerar encryption  it is type of subtution syfer in which each later in the string is replaced by 
#a latter sum fixed no. of position down the alphabet 

m=input("Enter Alphabet Only")
m=m.upper()
n=int(input("Enter Shift"))
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=""
for i in m:
    if i in a:
        index=(a.find(i)+n)%len(a)
        s=s+a[index]
    else:
        s=s+i
        

print(s)


# In[25]:


#to create saerar decryption  it is type of subtution syfer in which each later in the string is replaced by 
#a latter sum fixed no. of position down the alphabet 

m=input("Enter Alphabet Only")
m=m.upper()
n=int(input("Enter Shift"))
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=""
for i in m:
    if i in a:
        index=(a.find(i)-n)%len(a)
        s=s+a[index]
    else:
        s=s+i
        

print(s)


# In[6]:


# to convert no. into words upto thousand
def n_w(num):

    d={0:'',
      1:'One',
      2:'Two',
      3:'Three',
      4:'Four',
      5:'Five',
      6:'Six',
      7:'Seven',
      8:'Eight',
      9:'Nine',
      10:'Ten',
      11:'Eleven',
      12:'Twelve',
      13:'Thirteen',
      14:'Fourteen',
      15:'Fifteen',
      16:'Sixteen',
      17:'Seventeen',
      18:'Eighteen',
      19:'Nineteen',
      20:'Twenty',
      30:'Thirty',
      40:'Forty',
      50:'Fifty',
      60:'Sixty',
      70:'Seventy',
      80:'Eighty',
      90:'Ninety',}

    if num<=20:
        return(d[num])
    elif num<100:
        if num%10==0:
            return(d[num])
        else:
            return(d[(num//10)*10]+d[num%10])
    elif num<1000:
        if num%100==0:
            return(d[num//100]+' Hundred ')
        else:
            return(d[num//100]+' Hundred '+n_w(num%100))
        
        
num=int(input("Enter Number"))
print(n_w(num))

