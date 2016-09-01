
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L2-2 Errors and Practice
# 
# Learner objectives for this lesson
# * Practice arithmetic in Python

# ## Programming Errors
# Rarely will you write a program that is free of errors. You'll need to diagnose and correct three kinds of errors:
# 1. Syntax errors (code violates syntax rules for a proper Python program)
#     * Detected at compile time
#     * Program will not run unless they're corrected
#     * Examples
#         * Undeclared identifiers
#         * Invalid identifiers (e.g. a space in a variable name)
#         * Failure to close a comment or string properly
#         * Incorrect indenting (we will learn about indenting when we learn about functions)
# 2. Run-time errors
#     * Cause the program to "crash": an error is reported, and control is turned over to the operating system
#     * Examples
#         * Division by zero
#         * Getting into an infinite loop, which may ultimately cause a "stack overflow"
# 3. Logic Errors
#     * Cause the program to compute incorrect results
#     * Often go unnoticed, at least at first
#     * Examples
#         * Your algorithm is wrong because you misunderstand the problem
#         * You do not obtain input data properly, so your computations work on the wrong data.
# 
# ## Software Development Method
# Equivalent to the "Scientific Method" in the sciences and the "Systems Approach" in business.
# 
# Six basic steps:
# 1. Specify problem requirements
# 1. Analyze the problem
# 1. Design an algorithm to solve the problem
# 1. Implement the algorithm
# 1. Test and verify the completed program
# 1. Maintain and update the program
# 
# Developing software is an iterative process, your first solution is generally not your best. Your understanding of software your required to build evolves as you understand the problem more. At this point don't be afraid to make mistakes!
# 
# ## Practice Problems
# Note: Some problem descriptions have been taken from Chapter 2 of Hanly & Koffman's Problem Solving and Program Design in C (7th Edition)

# ### Problem #1 Tax
# Write a program to compute the total price for a purchase after sales tax. Prompt the user to enter the purchase amount and the sales tax percent. Display the total price (to the nearest 2 decimal places) after adding the sales tax to the purchase amount.
# 
# Example output:
# 
# ```
# Please enter the purchase price: 9.00
# Please enter the sales tax as a percent (%): 7.8
# Total purchase price after tax: $9.70
# ```

# In[4]:

purchase = float(input("Please enter the purchase price: "))
tax_percent = float(input("Please enter the sales tax as a percent (%): "))

tax = purchase * (tax_percent / 100.0)
purchase += tax

print("Total purchase price after tax: $%.2f" %(purchase))


# ### Problem #2 Mileage Reimbursement
# Write a program that calculates mileage reimbursement for a salesperson at the rate of \$.35 per mile. 
# 
# Example output:
# 
# ```
# MILEAGE REIMBURSEMENT CALCULATOR
# Please enter the beginning odometer reading: 13505.2
# Please enter the ending odometer reading: 13810.6
# You traveled 305.4 miles. At $0.35 per mile, your reimbursement is $106.89
# ```

# In[1]:

print("MILEAGE REIMBURSEMENT CALCULATOR")
odo_begin = float(input("Please enter the beginning odometer reading: "))
odo_end = float(input("Please enter the ending odometer reading: "))

dist_traveled = odo_end - odo_begin
reimbursement = dist_traveled * .35
print("You traveled %.1f miles. At $0.35 per mile, your reimbursement is $%.2f" %(dist_traveled, reimbursement))


# ### Problem #3 Pythagoras
# The Pythagorean theorem states that the sum of the squares of the sides of a right triangle is equal to the square of the hypotenuse.
# 
# $$side1^{2} + side2^{2} = hypotenuse^{2}$$
# 
# For example, if two sides of a right triangle have lengths 3 and 4, then the hypotenuse must have a length of 5. Together the integers 3, 4, and 5 form a Pythagorean triple. There are an infinite number of such triples. Given two positive integers `m` and `n`, **where `m`> `n`**, a Pythagorean triple can be generated by the following formulas:
# 1. side1 = $m^2 – n^2$
# 1. side2 = $2mn$
# 1. hypotenuse = $m^2 + n^2$
# 
# Write a program that takes the values for `m` and `n` as input and displays the values of the Pythagorean triple generated by the formulas above.
# 
# Example output:
# 
# ```
# Please enter an m value: 4
# Please enter an n value: 2
# Pythagorean triple: 12^2 + 16^2 = 20^2
# ```

# In[11]:

m = int(input("Please enter an m value: "))
n = int(input("Please enter an n value: "))

side1 = m ** 2 - n ** 2
side2 = 2 * m * n
hypotenuse = m ** 2 + n ** 2

print("Pythagorean triple: %d^2 + %d^2 = %d^2" %(side1, side2, hypotenuse))


# In[1]:

# check the output
print(12 * 12 + 16 * 16)
print(20 * 20)


# ## TODO
# 1. To get good at programming you have to write code. Solve all of the practice problems above. Sketch out a pseudocode solution first on paper, then code them up in Python. 
# 2. Work on PA1.
# 
# ## Next Lesson
# We will learn how to write our own functions.
# 
# Note: No class on Monday because of Labor Day, see you Wednesday! (or Tuesday if you have lab on Tuesday)