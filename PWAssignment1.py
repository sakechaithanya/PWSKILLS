#!/usr/bin/env python
# coding: utf-8

# ####Assignment1

# In[ ]:


Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple


# In[1]:


sake =['pwskills',[1,2,3],5.2,(0,1,2)]


# In[2]:


sake


# #Q2. Given are some following variables containing data:
# var1 =‘ ‘
# var2 = ‘[ DS , ML , Python]’
# var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# var4 = 1.
# #What will be the data type of the above given variable.

# In[7]:


var1 =‘ ‘               #format be ---> ('')
type(var1)


# In[8]:


var2 = ‘[ DS , ML , Python]’
type(var2)


# In[9]:


var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
type(var3)


# In[10]:


var4 = 1.
type(var4)


# Q3. Explain the use of the following operators using an example:
# (i) /
# (ii) %
# (iii) //
# (iv) **

# In[11]:


a=10
b=2


# In[13]:


a/b  #'/' division symbol generates float value 


# In[15]:


a%b  #'%' modulus symbol generates remainder


# In[16]:


a//b # '//' symbol generates integer


# In[17]:


a**b #'**' power symbol gives a power  of b


# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

# In[21]:


sake =['pwskills',[1,2,3],5.2,(0,1,2),1,2,3,True,False,'ds']
print(len(sake))
for i in sake:
    print(i,type(i))


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[1]:


A=20
B=5
i=0
while(A%B)==0:
    print('number A is purely divisible by number B ')
    i+=1
    print(i)  #runs infinite times


# In[ ]:





# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

# In[24]:


list1=[]
for i in range(1,26):
    list1.append(i)


# In[26]:


for i in list1:
    if (i%3)==0:
        print(i,'element is divisible by 3')
    else:
        print(i,' element is not divisible by 3')


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# Mutable Objects	
# A mutable object can be changed after it is created	
# Examples : List, Set, Dictionary

# In[28]:


l=[1,2,3]
l


# In[31]:


l[1]=0   # see here we can change value by index
l


# Immutable Objects
# An immutable object cannot be changed after it is created
# Exg: tuples, int, float, bool, frozenset.

# In[32]:


t=(1,2,3)
t


# In[33]:


t(0)=0   # it generates error due to its immutable property


# In[ ]:

GOOGLE COLAB LINK:https://colab.research.google.com/drive/1Qdpo4xLARQnDEY_rxlEjurvrB4QALxpv


