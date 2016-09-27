
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L6-1 If Statements
# 
# Learner objectives for this lesson
# * Understand `if` statements

# Algorithms are composed of three different kinds of statements:
# 1. Sequence: the ability to execute a series of instructions, one after the other.
# 1. Conditional: the ability to execute an instruction contingent upon some condition.
# 1. Iteration: the ability to execute one or more instructions repeatedly.
# 
# If statements are conditionals: the ability to **execute some code IF some condition is true**. 
#  
# ## The `if` Statement
# The if statement supports conditional execution in Python:
# ```
# if <test>:
#     <body>
# ```
# 
# `<test>` must be an expression that can be evaluated to either `True` or `False` (non-zero or zero), i.e. `<test>` is a **Boolean condition**
# `<body>` is one or more Python statements that are **indented** 4 spaces (or one tab, depending on your text editor)

# In[1]:

x = 5

if x == 5:
    print("x is 5!!")
    
if x == 7:
    print("x is 7!!")


# Python also defines an `if`-`else` statement:
# ```
# if <test>:
#     <body-if-test-is-true>
# else:
#     <body-if-test-is-false>
# ```
# 
# **Only one of the two `<body>` blocks can be executed each time through this code**. In other words, they are "mutually exclusive".
# 
# Note: the `else` has no `<test>` condition. The `else` body executes when the complement of `<test>` is True (i.e. `<test>` is False).

# In[2]:

temperature = 10

if temperature > 32:
    print("It is warm out!")
else: # temperature <= 32
    print("Brrrrr...")


# In[3]:

x = y = z = 0
y = y + 4
z = z * x

if z > y:  
    print("Z: %d" %(z + 1))
else: # z <= y
    print("X: %d" %(x - 1))


# ## Predicate Functions Revisited
# Let's rewrite `is_even()` to use `if-else` statements:

# In[4]:

def is_even(x):
    '''
    
    '''
    flag = False
    if x % 2 == 0:
        # only sets flag to True when x is even
        flag = True
    return flag

def is_even_revised(x):
    '''
    This function does not use a flag, instead it has multiple return statements
    '''
    if x % 2 == 0:
        return True
    else:
        return False
    
print(is_even(5))
print(is_even_revised(5))
print(is_even(8))
print(is_even_revised(8))


# ## Common Mistakes with `if` Statements
# * Using = (assignment) instead of == (logical equality) 
# * Using if-else when if-if should be used
#     * Remember else does not have an explicit condition associated with it
# * Using logical `and` instead of logical `or` and vice versa
# 

# ## TODO
# 1. Get started on PA3
# 
# ## Next Lesson
# 1. Multiple alternative `if` statements and nested `if` statements.
