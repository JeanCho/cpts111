
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# #  Midterm #1 Solutions

# In[21]:

2nd_place = 5


# In[22]:

second_place = 5


# In[23]:

second_place! = 5


# In[24]:

numStudents = 5


# In[25]:

num_students1 = 5


# In[26]:

_num_students = 5


# In[27]:

__numstudents2 = 5


# In[28]:

num students = 5


# In[29]:

Input = 5


# In[30]:

def = 5


# In[31]:

print(11 // 5)
print(22 % 7)


# In[33]:

import math
print("%.4f" %math.pi)
print(round(math.pi, 4))


# Predicate function: Function that returns True or False. Covered in L5-2 and L6-1.

# In[20]:

print(7 / 15 == 9 and 7 * 5 % 2 > 3 or 9 / 19 <= 2)


# Original: (not b and y >= 0) and (5 < z or x == y)
# 
# Complemented: not((not b and y >= 0) and (5 < z or x == y))
# 
# Simplified by DeMorgan's Laws: (b or y < 0) or (5 >= z and x != y)
# 
# Proof of equivalence with a truth table (columns (not b and y >= 0) and (5 < z or x == y) and not((b or y < 0) or (5 >= z and x != y)) match):
# 
# |b|y >= 0|5 < z|x == y|not b and y >= 0|5 < z or x == y|(not b and y >= 0) and (5 < z or x == y)|b or y < 0|5 >= z and x != y|(b or y < 0) or (5 >= z and x != y)|not((b or y < 0) or (5 >= z and x != y))|
# |-|-|-|-|-|-|-|-|-|-|-|
# |0|0|0|0|0|0|0|1|1|1|0|
# |0|0|0|1|0|1|0|1|0|1|0|
# |0|0|1|0|0|1|0|1|0|1|0|
# |0|0|1|1|0|1|0|1|0|1|0|
# |0|1|0|0|1|0|0|0|1|1|0|
# |0|1|0|1|1|1|1|0|0|0|1|
# |0|1|1|0|1|1|1|0|0|0|1|
# |0|1|1|1|1|1|1|0|0|0|1|
# |1|0|0|0|0|0|0|1|1|1|0|
# |1|0|0|1|0|1|0|1|0|1|0|
# |1|0|1|0|0|1|0|1|0|1|0|
# |1|0|1|1|0|1|0|1|0|1|0|
# |1|1|0|0|0|0|0|1|1|1|0|
# |1|1|0|1|0|1|0|1|0|1|0|
# |1|1|1|0|0|1|0|1|0|1|0|
# |1|1|1|1|0|1|0|1|0|1|0|

# In[3]:

def func1(x):
   x = x + 3 
   return 3
y = func1(9)
print(y, type(y))


# In[4]:

def f(x):
   return x // 4
y = f(13)
print(y, type(y))


# In[6]:

number = input("Enter a number: ")
number = int(number)# line #2
result = 5 + number


# In[1]:

def get_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    # at this point, we know num1 is not the max
    if num2 >=  num3:
        return num2
    return num3
    
    '''
    if num1 > num2:
        if num1 > num3:
            return num1
        else: # num2 < num1 <= num3
            return num3
    elif num2 > num3: # num1 <= num2
        return num2
    else:
        return num3
    '''


print(get_max(3.14, 2.5, -1.1))
print(get_max(0, 2, 2))
print(get_max(2, 0, 0))
print(get_max(2, 2, 0))
print(get_max(2, 2, 2))
print(get_max(0, 1, 2))
print(get_max(0, 2, 1))
print(get_max(2, 1, 0))


# In[2]:

def code_block(x, y):
    if x <= 0:
        if y > 0:
            print("Strawberry")
            if x < 5:
                print("pie")
            elif y < 2:
                print("Burger")
            else:
                print("with fries")
        else:
            print("Coffee")
            if x == 0:
                print("with cream")
            elif y > 0:
                print("with sugar")
# a.
# not possible because y must be <= 0 to enter the coffee else block. y must > 0 to print "with sugar"
# b.
# not possible because "pie" and "fries" belong to the same if-elif-else block, of which the bodies are mutually exclusive
# c.
code_block(-1, 2)
print()
# d. 
code_block(0, -1)


# In[16]:

speed = int(input("Please enter an integer speed: "))
if speed < 45:
    print("Too slow")
elif speed > 65:
    print("Too fast")
else:
    print("Just right")


# In[49]:

x = 5
print(x * x)
print(x ** 2)
print(pow(x, 2))
x *= x
print(x)

