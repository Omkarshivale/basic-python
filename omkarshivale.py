#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)


# In[2]:


if 5>2:
    print('five is greater than two')
    print('five is greater than two')


# In[3]:


if 10>2:
    print('ten is greater than two')


# In[4]:


if 10 > 2:
    print("ten is greater than two!")
    if 10 > 2:
        print("ten is greater than two!")


# In[5]:


if 5>2:
    print("five is greater than two!")
    print("five is greater than two")
    


# In[6]:


if 10>2:
 print("ten is greater than two!")
    


# In[7]:


print("cheers ,mate!")


# In[8]:


x = 10
y="lint"
print(x)
print(y)


# In[9]:


x


# In[10]:


y


# In[11]:


x=4 #x is of type int
x="sally" #x is now of type str
print(x)


# In[12]:


x=str(3)
y=int(3)
z=float(3)


# In[13]:


x=str(3)
y=int(3)
z=float(3)

print(type(x))
print(type(y))
print(type(z))


# In[14]:


x,y,z ="orange","banana","cherry"
print(x)
print(y)
print(z)


# In[15]:


x=y=z="orange"
print(x)
print(y)
print(z)


# In[16]:


fruits = ["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


# In[17]:


x=("i love python")
print(x)


# In[18]:


x="i"
y="love"
z="python"
print(x,y,z)


# In[19]:


x=500
y=500
print(x+y)


# In[20]:


x=5
y="john"
print(x,y)


# global variable variable that are created outside of a function
# 
# global variable can be used by everyone,both inside of function and outside.
# 

# In[21]:


x = "awesome"

def myfunc():
  print("python is "+ x)
   
    
myfunc()


# ### built in data types
# 

# In[22]:


'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	No
'''


# ### setting the data type:
# in python ,the data type is set when you assign a value to a variable:
# 

# In[23]:


x="hello world"
print(type(x))


# In[24]:


x=200
print(type(x))


# In[25]:


x = 20.1
print(type(x))


# In[26]:


x = 1j
print(type(x))


# In[27]:


x = ['apple']
print(type(x))


# In[28]:


x = ('apple','cherry')
print(type(x))


# In[29]:


x = range(3)
print(type(x))


# In[30]:


x = {'apple','cherry'}
print(type(x))


# In[31]:


x = {'Name':'JJ', 'Age':42}
print(type(x))


# In[32]:


x = frozenset({'apple','cherry'})
print(type(x))


# In[33]:


x = True
print(type(x))


# ### boolean values
# in programing you often need to know if an expression is true or false.
# you can evaluate any expression in python,and get one of two answers,true or false.
# when you are compare two values,the expression is evaluated and python returns the boolean 
# answer:

# In[34]:


print(10>9)
print(10==9)
print(10<9)


# In[35]:


a=200
b=33
 
if b>a:
  print("b is greater than a")
else:
 print("b is not greater than a")
          
          


# In[36]:


lis = [1,2,3,4]
tup = (1,2,3,4)
se ={1,2,3,4,5,6}


# In[37]:


se={1,2,3,4,5,6}
print(se)


# In[38]:


my_dictionary={'key':20}
print(my_dictionary)


# ### ** List **
# 
# 1. It is a collection of Data Type/Data Structure (Element)
# 2. It consists of Homogeneous and heterogenous data type
# 3. List is of Mutable(changeable) structure
# 4. It can contaion duplicate elements
# 5. It is of ordered type with 0 base index

# ### ** Operations on list **
# 
# Insert operation
# (a) insert (b) append (c) extend

# In[39]:


#1.insert
py_list=['python','java',33,44]


# In[40]:


#insert(index,element)
py_list.insert(2,'ml')
py_list


# In[41]:


# 2. append
py_list.append('AI')
py_list


# In[42]:


# 3. extend
py_list.extend([1,2,3,4,5])
py_list


# ### extend is used to insert multiple element at the end of the list

# ### 2. delete opretion
# a)remove b)pop c)clear

# In[43]:


# 1.remove
py_list.remove(44)
py_list


# In[44]:


dup_list = [1,2,3,4,5,6,1,2,3,4,5,6]
dup_list.remove(1)
dup_list


# In[45]:


# 2.pop

py_list.pop(2)
py_list


# pop is used to delet element by using its index number.
# pop will remove the last element if not given any index number
# 

# In[46]:


# 3. clear
dup_list.clear()
dup_list


# In[47]:


###copy


# In[48]:


p1=[1,2,3,4,5,6,]
py2=p1.copy()
py2


# ### tuple
# 1.it is collection of element5
# 
# 2.immutable data structure(cannot add,insert,delet)
# 
# 3.orderd type with 0 based index
# 
# 
# 

# ### tuple operation
# 1.index
# 2.count

# #### set operations
# 1.insert operations
# a)add

# In[49]:


# Add is used to insert a single element
loan = {'akash','om'}
loan.add('Anshul')
loan


# In[50]:


loan.add(999)
loan


# ### delete operation
# a) remove

# In[51]:


t={1,2,3,4,5,6,7,}
t.remove(3)
t


# update-->The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

# In[52]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,'a'}

set1.update(set2)
print(set1)


# union-->method returns a new set with all items from both sets.
# 

# In[53]:


l1 = {1,4,6}
l2 = {'a','b','c'}
l1.union(l2)


# In[54]:


# Join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# Symmetric Differences-->The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# It is the opposite of intersection

# In[55]:


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


# In[56]:


# Use ^ to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)


# ### ** Frozenset **
# 
# frozenset is an immutable version of a set.
# 
# Like sets, it contains unique, unordered, unchangeable elements.
# 
# Unlike sets, elements cannot be added or removed from a frozenset.

# In[57]:


# Create a frozenset and check its type:

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


# ###### DICTIONARY
# 1.it is collection of item
# 
# 2. it is mutable type but only value can be changed
# 
# 3.key can never be duplicate
# 
# Key: immutable type
# 
# value: mutable type

# In[58]:


my_dict = {'Name':'omkar|','Salary':75000,'City':'vadhu'}
my_dict


# In[59]:


thisdict =dict(name = "omkar",age = 21, country = "india")
print(thisdict)


# ##### dictionary operations/method
# 1.get

# In[60]:


my_dict.get("Name")


# In[61]:


my_dict.keys()


# In[62]:


my_dict.values()


# In[63]:


my_dict.items()


# #### 2. to insert

# In[64]:


my_dict['age']=25
my_dict


# In[65]:


my_dict.update({'a':1,'b':2,'c':3})
my_dict


# my_dict.update([('d',4),('e',5)})
# my_dict

# In[66]:


my_dict.update([('d',4),('e',5)])
my_dict


# 2. Delete
# 
# (a) pop---> using the key the item can be deleted
# 
# (b) popitem--> it removes the last item
# 
# my_dict.pop('a')

# In[67]:


my_dict.pop('a')
my_dict


# In[68]:


my_dict.popitem()
my_dict


# #### 3. fromkeys()
# 
# fromkeys()method returns a dictionary with the specified keys and the specified value
# 
# **syntax** dict.fromkeys(key,value)

# In[69]:


k1=('key1','key2','key3')
k2=0
thisdict = dict.fromkeys(k1,k2)
print(thisdict)


# In[70]:


k = ('name','age','salary')
l= dict.fromkeys(k)
l


# In[71]:


my_dict.setdefault('d',4)
my_dict


# In[72]:


my_dict.setdefault('l',5)
my_dict


# #### 4. clear 

# In[73]:


thisdict


# In[74]:


thisdict.clear()
thisdict


# #### nested dictinories

# In[75]:


# create a dictionary that contain three dictionaries:

myfamily = {
   "child1":{
       "name":"omkar",
    "year":2005 
},
    "child2":{
    "name":"yash",
    "year":2006
},
"child3":{
    "name":"soham",
    "year":2007
}
}
myfamily
   


# In[76]:


print(myfamily["child2"]["name"])


# In[ ]:





# ##### Strings
# 
# in python are surrounded by either single quotation marks, or double quotation marks.
# 
# 'hello' is the same as "hello".
# 
# You can display a string literal with the print() function:

# In[77]:


print("hello")
print("hello")


# In[78]:


print("It's alright")
print("He is called 'omkar'")
print('He is called "omkar"')


# In[79]:


## loop through the letters in the word "banana":
for x in "banana":
    print(x)


# ###### String Length
# 
# To get the length of a string, use the len() function.
# 

# In[80]:


a="hello world!"
print(len(a))


# ##### ** Slicing Strings **
# 
# By Slicing You can return a range of characters by using the slice syntax.
# 
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# In[81]:


b = "Hello, World!"
print(b[2:7])


# In[82]:





# In[83]:


b = "hello,world!"
print(b[2:])


# #### modify strings

# In[84]:


# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


# In[85]:


# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())


# #####  Remove Whitespace
# 
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space

# In[86]:


##example
a = "    Hello, World!    "
print(a.strip()) # returns "Hello, World!"


# ##### Split String
# 
# The split() method returns a list where the text between the specified separator becomes the list items

# In[87]:


a = "Hello, World!"
print(a.split(","))


# 
# 
# 

# #### String Concatenation
# 
# To concatenate, or combine, two strings you can use the + operator.

# In[88]:


a = "i love you"
b = " i love you too"
c = a+b
print(c)


# In[89]:


# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


# #### format string
#  as we learned in the python variables, we cannot combine strings and number like this:

# In[90]:


age=36
print("my name is omkar",age)


# In[ ]:






# #####  F-Strings
# 
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# 
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# In[103]:


age = 36
print= (f"My name is John,i am {age}")
print


# In[107]:


price = 59
text=(f"The price is {price} dollars")


#  A placeholder can include a modifier to format the value.
# 
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# In[110]:


# Display the price with 2 decimals:

price = 59
txt = (f"The price is {price:.2f} dollars")
txt


# In[113]:


txt = f"The price is {20 * 59} dollars"
print


# In[ ]:




