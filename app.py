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
# print("Sending a message") many times

# for number in range(3):
#     print("Attempt", number + 1)
#Attempt 1 Attempt 2 Attempt 3

# for number in range(1, 4):
#     print("Attempt", number, (number) * ".")
# Attempt 1 . 
# Attempt 2 ..
# Attempt 3 ...

# PRACTICE 'FOR LOOP'\
# 1



# for item in range(3):
#     print("Item:", item)

# Passing 3rd Argument as a Step
# for number in range(1, 10, 2):
#     print("Attempt", number, (number) * ".")

# Attempt 1 . 
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........

########################################
# FOR ELSE
# ########################################
# successful = True

# for number in range(3): 
#     print("Attempt")

#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")
# Attempt
# Attempt
# Attempt
# Attempted 3 times and failed

# FOR/ELSE PRACTICE EXAMPLE
# stop = True

# for number in range(3):
#     print("Can I go yet?")

#     if stop:
#         print("Stop!!!")
#         break

# else:
#     print("The light is f&*(ing broken...")

########################################
# NESTED LOOPS
# ########################################

# PRACTICE EXAMPLE - NESTED LOOPS
# for x in range(7):
#     for y in range(2):
#         print(f"({x}, {y})")

# runs inner loop 3 times first, then outer loop 5 times.
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
# (3, 0)
# (3, 1)
# (3, 2)
# (4, 0)
# (4, 1)
# (4, 2)

########################################
# ITERABLES
# ########################################
# print(type(5)) # <class 'int'>

# print(type(range(5))) #<class 'range'>

# # Iterable
# for x in "Python":
#     print(x)
# # P
# # y
# # t
# # h
# # o
# # n

# # Another Iterable Type
# for x in [1, 2, 3, 4]:
#     print(x)

# 1
# 2
# 3
# 4

########################################
# WHILE LOOPS
# ######################################
# PRACTICE EX:
# num1 = 200
# while num1 > 0: 
#     print(num1)
#     # num1 = num1 // 2
#     num1 //= 2



# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# 100
# 50
# 25
# 12
# 6
# 3
# 1

# command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

########################################
# INFINITE LOOPS
# ######################################
# Always want a way to Break Out of them
# while True:
#     command = input(">"0)
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

########################################
# EXERCISE: check for 1-10 for even
# ######################################
# count = 0

# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers.")
# 2
# 4
# 6
# 8
# We have 4 even numbers

########################################
# EXERCISE: check for 1-10 for ODD NUMS
# ######################################
# count = 0 

# for num in range(1, 10):
#     if num % 2 == 1:
#         count += 1
#         print(num)
# print(f"We have {count} odd numbers.")

# 1
# 3
# 5
# 7
# 9
# We have 5 odd numbers.



# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Kim", "Carpico")
# greet("John", "Smith")

############################################
# Better to do this bc we can reuse
############################################
# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Mosh")

############################################
# KEYWORD ARGUMENTS
############################################
# def increment(number, by):
#     return number + by


# print(increment(2, 1)) # 3

# # 'by=1' is a KeyWord Argument, used to make code cleaner
# print(increment(2, by=1)) # 3

# # Practice EXAMPLE #1
# def step_increment(number, by):
#     return number * by


# print(step_increment(2, by=10))

# # Practice EXAMPLE #2
# def halved(num, by):
#     return num / by


# print(halved(10, by=2))


############################################
# How to Make the 'by' Parameter Optional
############################################
# def increment(number, by=1):
#     return number + by


# print(increment(2)) 


############################################
# XARGS
############################################
# def multiply(x, y):
#     return x * y

# # If you want to pass > 2 arguments
# multiply(2, 3, 4, 5)


# #
# def multiply(*numbers):
#     print(numbers)


# multiply(2, 3, 4, 5) # (2, 3, 4, 5)

# Lists: [2, 3, 4, 5] => [] to create Lists
# (2, 3, 4, 5) => () to create Tuples, collection of objects that CANNOT BE MODIFIED

# def multiply(*numbers):
#     for number in numbers:
#         print(number)


# multiply(2, 3, 4, 5)
# 2
# 3
# 4
# 5


# Example using XARGS
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5)) # 120

# Example #2 using XARGS
# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total


# print(add(2, 3, 4, 5)) # 14

############################################
# XXARGS => 
############################################
# # Printing a string in Reverse
# for char in reversed("Python"):
#     print(char)


# # WRITE prgm to print Prime #'s between 100-200
# for num in range(1, 100):
#     if all(num % i != 0 for i in range(2, num)):
#         print(num)

# Sort a list
# list = [1, 33, 123, 67, 68]
# list.sort(reverse = True)
# print(list)

# # SAME AS ABOVE WITHOUT THE SORT FUNCTION
# data_list = [1, 33, 123, 67, 68]
# new_list = []

# while data_list:
#     minimum = data_list[0]
#     for x in data_list: 
#         if x > minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)


############################################
# CREATING A CLASS IN PYTHON
# ############################################
# class employee:

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#         self.email = self.first_name + "." + self.last_name + "@kite.com"


#     # Setter Function: Let's us change the Salary of an Employee
#     def giveRaise(self, salary):
#         self.salary = salary




############################################
# DATATYPES: list, tuple, set, dictionary
# ############################################
# #LIST: [] square braces
# list1 = ["Computer", "Printer", "TV", "Camera", 89, 33.3]
# list1[0] = "PC"
# print(list1) # ['PC', 'Printer', 'TV', 'Camera', 89, 33.3]

# #TUPLE: () rounded braces, immutable - CANNOT change items in a tuple
# tuple1 = ("Computer", "Printer", "TV", "Camera", 89, 33.3)
# list1[0] = "PC"
# print(tuple1) # ('Computer', 'Printer', 'TV', 'Camera', 89, 33.3)


# # SET: uses the 'set' keyword, you CANNOT change its items, but you can ADD new Items
# set1 = set(["Computer", "Printer", "TV", "Camera", 89, 33.3])
# print(set1) # {33.3, 'Computer', 'Camera', 'TV', 89, 'Printer'}

# # DICTIONARY: {} curly braces: orders, changeable and does NOT allow duplicates
# # made up of key/value pairs
# dict1 = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(dict1)




 ##############################################
# XARGS: {}
###############################################
# def multiply(x, y):
#     return x * y


# print(multiply(2, 3))

# Change the above to this:
# def multiply(*numbers):
#     print(numbers)


# multiply(2, 3, 4, 5)

# CHANGE ABOVE TO GET THE FOLLOWING:
# def multiply1(*numbers):
#     for number in numbers:
#         print(number)


# multiply1(2, 3, 4, 5)
# 2
# 3
# 4
# 5


# def multiply2(*numbers):
#     total = 1
#     for number in numbers:
#         # total = total * number
#         total *= number
#     return total


# print(multiply2(2, 3, 4, 5)) # 120

# # # PRACTICE PROBLEM: 
# def add1(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total


# print(add1(2, 3, 4, 5)) # 14


# ##############################################
# # XXARGS: {} -> can pass multiple key/value pairs
# # ############################################

# # dictionary: {}

# def save_user(**user):
#     print(user)


# save_user(id=1, name="John", age=22)
# {'id': 1, 'name': 'John', 'age': 22} -> this is called a dictionary.

# def save_user(**user):
#     print(user["name"]) #John


# save_user(id=1, name="John", age=22)


####################################################
# SCOPE
####################################################
# message = in this Example is only accessible within this function
# def greet():
#     message = "a"


# def send_email(name):
#     message = "b"


# greet("Mosh")


## OPPOSED TO GLOBAL SCOPE - best to NOT use GLOBAL VARIABLES
# message = "a"

# def greet(name):
#     message = "b"


# greet("Mosh")
# print(message) # a

# # *** AVOID THIS *** bc it is possible to have multiple functions that rely on this function
# message = "a"

# def greet(name):
#     global message
#     message = "b"


# greet("Mosh")
# print(message)

##################################################



##################################################
# DEBUGGING
##################################################
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         return total


# print("Start")
# print(multiply(1, 2, 3))

##################################################
# FIZZ BUZZ
##################################################
def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    return input


print(fizz_buzz(5))

