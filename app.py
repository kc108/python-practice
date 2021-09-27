import math

# to see all functions you can type => 'math.'

# course = "Python Programming"
# print(len(course))

# print(course[0])
# print(course[-1])

# # Pyt
# print(course[0:3]) 

# # Python Programming
# print(course[0:]) 

# #Pyt
# print(course[:3])

# #Python Programming
# print(course[:])

# course = "Python \"Programming"
# print(course) # Python "Programming

# course1 = "Python \nProgramming"
# print(course1)
# #Python
# #Programming

########################################
# Formatted Strings
# ########################################
# first = "Mosh"
# last = "Hamedani"

# full = first + " " + last
# print(full) #Mosh Hamedani

# # BETTER PRACTICE
# first1 = "Mosh"
# last1 = "Hamedani"

# full1 = f"{len(first1)} {last1}"
# print(full1)

########################################
#  String Methods
########################################
# course3 = "Python Programming"
# print(course3.upper())
# print(course3)
# # ORIGINAL string is not mutated

# print(course3.lower())
# print(course3.title()) #Python Programming


# course4 = "  python programming"
# print(course4.strip()) # removes whitespaces from left and right

# print(course4.lstrip()) #left strip
# print(course4.rstrip()) #right strip removes whitespaces

# print(course4.find("pro")) # Shows index of "pro" in "python programming". This is case sensitive

# print(course4.replace("p", "j")) # replaces p with j, "jython jrogramming"

# print("pro" in course4) # checks if "pro" is in variable as a 'true' or 'false'. Whereas '.find' checks the index of the identified variables

# print("swift" not in course4) # true

########################################
#  Numbers
########################################
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3) #3.3333333
# print(10 // 3) #3
# print(10 % 3)
# print(10 ** 3) # 1_000

# # Augmented Assignment Operator
# x = 10
# x = x + 3

# # augmented operator
# x += 3

########################################
#  Working with Numbers
########################################

# print(round(2.9)) #3
# print(abs(-2.9)) #2.9

# ########################################
# #  Math Module
# ########################################
# # MUST IMPORT IT AT TOP OF FILE
# print(math.ceil(3.9)) # 4

########################################
#  Type Conversion
########################################

# # To Get Input from the User you Use the Input()
# x = input("x: ")
# # print(type(x)) # <class 'str'>
# y = int(x) + 1

# print(f"x: {x}, y: {y}") # x: 1, y: 2

# y = x + 1
# "1" + 1 => will result in an error because they are of different types

# int(x)
# float(x)
# bool(x)
# str(x)

# FALSEY values in Python => Falsy, "", 0, None (represents the absence of a value)


########################################
#  Conditional Statements
########################################
# the print statement that is not indented will run regardless of if statement
# temperature = 35
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# print("Done")

# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

########################################
#  Ternary Operators
########################################
# age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# # *** TERNARY OPERATOR ***
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

########################################
# LOGICAL OPERATORS
# ########################################
# AND, OR & NOT

# high_income = True
# good_credit = True
# student = True

# if high_income and good_credit:
#     print("Eligible") # Eligible 
# else:
#     print("Not eligible")


# if high_income or good_credit:
#     print("Eligible") # Eligible 
# else:
#     print("Not eligible")

# *** NOT Operator ***
# if not student:
#     print("Eligible") 
# else:
#     print("Not eligible") # Not eligible

# # *** MORE COMPLICATED EXAMPLE ***
# if (high_income or good_credit) and not student:
#     print("Eligible") 
# else:
#     print("Not eligible") # Not eligible

########################################
# SHORT-CIRCUIT EVALUATION
# ########################################
# high_income = False
# good_credit = True
# student = True 

# This is an Example of 'Short-Circuiting' bc it stops processing bc the 'and' part of the argument is 'false'
# if high_income and good_credit and not student: 
#     print("Eligible")

# Same concept with the 'or' operator
# if high_income or good_credit or not student: 
#     print("Eligible")

########################################
# CHAINING COMPARISON OPERATORS
# ########################################
# age should be between 18 and 65
# age = 22
# # if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligible")

# # In Math we write it like this => 18 <= age < 65
# # In Python: lines 217 & 218 are exactly the same

# # What will you see on the screen?
# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# # print c

########################################
# FOR LOOPS
# ########################################
