# import math
# from collections import deque
# from array import array
# from sys import getsizeof
# from pprint import pprint
from timeit import timeit

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
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input


# print(fizz_buzz(15))


##################################################
# LISTS => [], can be strings
##################################################
letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 100
# print(zeros)

# zeros1 = [0] * 5
# combined = zeros1 + letters
# print(combined) # [0, 0, 0, 0, 0, 'a', 'b', 'c']

# numbers = list(range(20))
# chars = list("Hello")
# print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# print(chars) # ['H', 'e', 'l', 'l', 'o']
# print(len(chars)) # 5

##################################################
# ACCESSING ITEMS
##################################################
# letters = ["a", "b", "c", "d", "e"]
# letters[0] = "A"
# print(letters[0])
# print(letters[0:3]) # ['A', 'b', 'c']
# print(letters[::2]) # ['A', 'c', 'e']
# print(letters) # ['A', 'b', 'c', 'd', 'e']

# nums = list(range(20))
# print(nums[::-1]) # reverses list
# print(nums[::2]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ## This is Identical to the below
# numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

## SAME AS ABOVE
# numbers = [1, 2, 3]
# first, second, third = numbers # list must have the same number of variables


# Storing in an Other List: prints everything after the second item
# numbers1 = [1, 2, 3, 4, 5]
# first, second, *other = numbers1
# print(first) # 1
# print(other) # [3, 4, 5]


# numbers2 = [1, 2, 3, 4, 5, 9]
# first, *other, last = numbers2
# print(first, last) # 1 9
# print(other) # [2, 3, 4, 5]


##################################################
# LOOPING OVER LISTS
##################################################
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

# a
# b
# c

# letters1 = ["a", "b", "c"]
# for letter in enumerate(letters1):
#     print(letter[0], letter[1])

# 0 a
# 1 b
# 2 c

# can unpack
# letters = ["a", "b", "c"]

#################################
# ** don't need this anymore
#################################
#################################
# items = (0, "a")
# index, letter = items
#################################
#################################
# for index, letter in enumerate(letters1):
#     print(index, letter)

# Returns a Tuple (returns read only, cannot add new items)
# (0, 'a')
# (1, 'b')
# (2, 'c')


#################################################
# ADDING/REMOVING ITEMS
#################################################
# ADD
# letters = ["a", "b", "c"]

# letters.append("d")
# letters.insert(0, "-")
# print(letters) # ['a', 'b', 'c', 'd']

# # REMOVE
# letters.pop ()
# print(letters) # ['-', 'a', 'b', 'c']
# letters.pop(0)
# print(letters) # ['a', 'b', 'c']
# letters.remove("b")
# print(letters) # removes the 1st occurence of "b" -> ["a", "c"]
# del letters[0]
# print(letters) # ["c"]
# # ** can also deleted a range 
# letters.insert(-1, "b") #["b", "c"]
# letters.insert(2, "d")
# print(letters) # ["b", "c", "d"]
# # Delete a range
# del letters[0:1]
# print(letters) # ["c", "d"]

# # CLEAR LIST
# letters.clear()
# print(letters) # []


#################################################
# FINDING ITEMS
#################################################
# letters1 = ["a", "b", "c"]
# # print(letters.index("a")) # 0 

# # returns number of times occurs in list
# print(letters1.count("d")) # 0 


# print(letters.index("d")) # returns error since it does not exist to prevent this we should check if something exists


# if "d" in letters1: 
#     print(letters1.index("d"))

#################################################
# SORTING LISTS
#################################################
# numbers = [3, 51, 2, 8, 6]

# numbers.sort()
# print(numbers) # [2, 3, 6, 8, 51]

# to return in DESCENDING ORDER
# ** WILL 'NOT' MODIFY THE ORIGINAL LIST
# numbers.sort(reverse=True) # [2, 3, 6, 8, 51]
# print(numbers.sort(numbers, reverse=True))
# print(numbers)

# SORTED FUNCTION ** MODIFIES THE ORIGINAL LIST **
# sorted(numbers) #[51, 8, 6, 3, 2]
# print(numbers) # [51, 8, 6, 3, 2]

# items = [
#     ("Product1", 10), 
#     ("Product2", 9), 
#     ("Product3", 12), 
# ]

# *** NOTHING CHANGES HERE *** MUST DEVELOP A FUNCTION TO SORT LISTS
# items.sort()
# print(items)

# # FUNCTION TO SORT LISTS
# def sort_item(item):
#     return item[1]

# # this is one way, there is a better way coming up...
# items.sort(key=sort_item)
# print(items)

#################################################
# LAMBDA FUNCTIONS
#################################################
# items1 = [
#     ("Product1", 10), 
#     ("Product2", 9), 
#     ("Product3", 12), 
# ]


# def sort_item(items1):
#     return items1[1]

# IMPROVE THIS FUNCTION BY USING A LAMBDA
# items1.sort(key=sort_item)
# print(items1)

# below is comment
# items1.sort(key=lambda parameters:expression)
# print(items1)

# next step..
# items1.sort(key=lambda item:item[1])
# print(items1)


###############################################
# EXERCISE: WRITE A LAMBDA EXAMPLE
###############################################
# Want to transform this list into seeing only lists of prices 
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# to show prices using for loop -> More elegent solution below
# prices = []
# for item in items: 
#     prices.append(item[1])


# map(lambda)

# print(prices) # [10, 9, 12]




################################################
# LAMBDA -> functions without names
################################################
# def square(a):
#     return a * a

# result = square(5)
# print(result)


# # using a lambda 
# f = lambda a, b : a + b
# result = f(5, 6)
# print(result)


# # Normal Function
# def f(x):
#     return 3*x + 1

# print(f(2)) # 7

# Lambda, Anonymous function
# Write your inputs followed by the function
# LAMBDA is a keyword that displays that the function is an ANONYMOUS FUNCTION
# g = lambda x: 3*x + 1
# g(2) # 7

# exercise: create lambda
# cats = lambda x: 2*x + 3
# print(cats(2)) # 7

# # LAMBDA WITH MORE THAN ONE INPUT
# full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title() 
# print(full_name("  kim", "cArPico")) # Kim Carpico

# # USING LAMBDA W/O VARIABLE
# scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H.G. Wells", "Leigh Brackett"]

# # help(scifi_authors.sort)
# scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
# print(scifi_authors)

# ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H.G. Wells']


################################################
# (CONTINUE) WITH VIDEO: MAP FUNCTION
################################################
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# REPLACE THE FOLLOWING 3 LINES WITH THE MAP FNCT BELOW
# prices = []
# for item in items: 
#     prices.append(item[1])

# x = map(lambda item: item[1], items)
# print(x) # <map object at 0x7fac03031f70>, WHICH IS ANOTHER ITERABLE

# to get item you do the following:
# x = map(lambda item: item[1], items)
# for item in x:
#     print(item) 

# 10
# 9
# 12

# # ** ALTERNATIVELY, YOU CAN CONVERT THIS INTO A LIST OBJECT LIKE SO:
# prices = list(map(lambda item: item[1], items))
# print(prices) # [10, 9, 12]

################################################
# LAMBDA & FILTER FNCT
################################################
# items = [
#     ("Product", 10),
#     ("Product", 9),
#     ("Product", 12),
# ]

# x = filter(lambda item: item[1] >= 10, items)
# print(x) # <filter object at 0x7f8d27131f70>

# ** THEN DO THE FOLLOWING:
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered) # [('Product', 10), ('Product', 12)]


################################################
# LIST COMPREHENSIONS
################################################
# map() & filter() above are used, but can also use the following. This is unique to Python
# [] define the list, inside write a Comprehension Expression
# items1 = [
#     ("Product", 10),
#     ("Product", 9),
#     ("Product", 12),
# ]

# *** FORMULA FOR LIST-COMPREHENSIONS *** PREFERRED WAY IN PYTHON TO MAP OR FILTER *** UNIQUE TO PYTHON ***
# # [expression for item in items]
# [item[1] for item in items]

# # same as the following, but the above is cleaner
# prices = list(map(lambda item: item[1, items]))


#######################################################
#######################################################
# RE-WRITING THE FILTER ABOVE WRITTEN AGAIN BELOW:
# filtered = list(filter(lambda item: item[1] >= 10, items))

# # USING A LIST-COMPREHENSION same as above
# filtered = [item for item in items if item[1] >= 10]


#######################################################
# ZIP FUNCTION
#######################################################
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # LIST []
# # tuple ()
# [(1, 10), (2, 20), (3, 30)]

# print(zip(list1, list2)) # <zip object at 0x7fd87313cac0>

# # ITERABLE SO USE BUILT-IN LIST()
# print(list(zip(list1, list2))) # [(1, 10), (2, 20), (3, 30)]
# print(list(zip("abc", list1, list2))) # can also spread list across tuples -> [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]


#######################################################
# STACKS -> "last in, first out"
#######################################################
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session) # [1, 2, 3]
# last = browsing_session.pop()
# print(last) # 3
# print(browsing_session) # [1, 2]
# print("redirect", browsing_session[-1]) # redirect 2

# FALSEY VALUES: 0, "", []
# if not browsing_session:
#     print("disable")

# # RECAP
# browsing_session = []
# browsing_session.append(1) # add to top of stack
# browsing_session.pop() # remove the last element
# # check if it is empty or not
# if not browsing_session:
#     browsing_session[-1] # used to get the 'index' on top of the stack


#######################################################
# QUEUES -> FIFO, first in, first out: resembles queue in a restaurant. The first person, is the first that would get in
#######################################################
# [] can use a list in PYTHON to do this
# [1, 2, 3, 4]
# at top need to import the following
# from collection import deque
# Instead of queue = [] we do the following:
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue) # deque([2, 3])
# #If the queue is empty print "empty"
# if not queue:
#     print("empty")



#######################################################
# TUPLE: read-only list, use (), IMMUTABLE, *** use this when you do NOT want to MODIFY IT. 
#######################################################
# point = (1, 2)
# # Can also Exclude the ()like so:
# point = 1, 2
# print(type(point)) # <class 'tuple'>

# # concatinating two > tuples
# point = (1, 2) + (3, 4)
# print(point) # (1, 2, 3, 4)

# point1 = tuple([1, 2])
# print(point1) # (1, 2, 1, 2, 1, 2)

# point3 = (1, 2) * 3
# print(point3)

# # String Tuples
# point4 = tuple("Hello World")
# print(point4) # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
# print(point4[0]) # H
# print(point4[0:2]) # ('H', 'e')


# Can also do the following:
point5 = (1, 2, 3)
print(point5[0:2])
x, y, z = point5
if 10 in point5:
    print("exists")


# # *** tuples are IMMUTABLE
# point[0] = 10 # results in ERROR

#######################################################
# SWAPPING VARIABLES 
#######################################################
# x = 10
# y = 11

# z = x
# x = y
# y = z

# print("x", x) # x 11
# print("y", y) # y 10

# Python  you can do this:
# x, y = y, x
# # can set variables like this:
# a, b = 1, 2

# print("x", x) # x 11
# print("y", y) # y 10



#######################################################
# ARRAYS
#######################################################
# [] -> LIST
# [1, 2, 3] 

# TO USE ARRAYS MUST IMPORT FROM MODULE LIKE SO:
# from array import array
# # Google Python3 typecode, this shows the 'one character' to use for the type of list being handled
# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# print(numbers) # array('i', [1, 2, 3, 4])
# # Also have .pop(), insert() and remove() similar to LISTS
# # numbers[0] # must be the same type of object



#######################################################
# SETS: collection with NO DUPLICATES
# *** SETS SHINE IN COMPLICATED MATH OPERATIONS ***
#######################################################
# Remove DUPLICATES BY CONVERTING LIST TO A SET
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)
# print(uniques) # {1, 2, 3, 4}

# print(first | second) # {1, 2, 3, 4, 5} -> returns COMBINED SETS

# # Can also get the intersection of 2 sets
# print(first & second) # {1} -> returns all values in BOTH SETS

# print(first - second) # returns the ADD set of NUMBERS NOT in the 1st SET
# print(first ^ second) # returns items either in the 1st or 2nd set BUT NOT both

# print(first[0]) # ERROR **** IF YOU NEED TO ACCESS ITEMS BY INDEX YOU NEED TO USE A LIST 

# # can check if something exists in a set
# if 1 in first: 
#     print("yes")


#######################################################
# DICTIONARIES: Used to map key'value pairs 
#######################################################
# # Example: Phone Book (name -> contact)
# point6 = {"x": 1, "y": 2}
# # can use above or this syntax, *prefer the below
# point6 = dict(x=1, y=2)
# print(point6["x"]) # 1
# # CANNOT USE THIS SYNTAX: point6[0] with DICTIONARIES


# point6["x"] = 10
# point6["z"] = 20
# # print(point6) # {'x': 10, 'y': 2, 'z': 20}

# # If an Invalid key is used you will get an Error
# # print(point6["a"])

# # *** WORK AROUND TO THIS ERROR ***
# if "a" in point6:
#     print(point6["a"])
# # Can pass a 'default' value as a second argument
# print(point6.get("a", 0)) # None

# # OTHER SOLUTION:
# print(point6.get("a")) # returns NONE -> means key does NOT exist

# del point6["x"]
# print(point6)

# # LOOPING OVER DICTIONARIES
# for x in point6:
#     print(x)

# # y
# # z

# # *** BETTER PRACTICE to rename KEY instead of 'x'
# for key in point6:
#     print(key, point6[key]) 
# # y 2
# # z 20

# #
# for x in point6.items():
#     print(key, point6[key]) 
# # EACH ITERATION GET A TUPLE
# # ('y', 2)
# # ('z', 20)

# # BETTER PRACTICE -> same result
# for key, value in point6.items():
#     print(key, value)

# # ('y', 2)
# # ('z', 20)

#######################################################
# DICTIONARY COMPREHENSIONS
#######################################################
# values = []
# for x in range(5):
#     values.append(x * 2)


# # LIST COMPREHENSION
# # *** [expression for item in items]***
# # SAME AS THE FNCT ABOVE 
# values = [x * 2 for x in range(5)]

# # list comprehension for a DICTIONARY
# values1 = {x * 2 for x in range(5)}
# print(values) # {0, 2, 4, 6}

# # *** SETS: {1, 2, 3, 4} -> JUST HAVE VALUES
# # *** DICTIONARIES: {1: "a", 2: "b"} -> KEY/VALUE PAIRS 
# #DICTIONARY
# values2 = {x: x * 2 for x in range(5)}
# print(values2) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


# # LIST COMPREHENSIONS WITH TUPLES
# values3 = (x * 2 for x in range(5))
# print(values3) # <generator object <genexpr> at 0x7fdebb6e3a50>


#######################################################
# GENERATOR EXPRESSIONS
#######################################################
# If you are working with LARGE DATA SETS DON'T DO THIS. WILL TAKE TO MUCH MEMORY. INSTEAD USE A 'GENERATOR OBJECTS'
# values108 = [x * 2 for x in range(10)]
# for x in values108:
#     print(x)

# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18


# # AT TOP IMPORT: from sys import getsizeof
# # changed [] for () to create a generator object 
# values1081 = (x * 2 for x in range(10))
# for x in values1081:
#     print(x) # GET THE SAME RESULT AS ABOVE, HOWEVER VALUES IS NO LONGER A LIST IT IS A GENERATOR OBJECT

# print(getsizeof("generator",values1081))

#######################################################
# UNPACKING OPERATOR
#######################################################
# numbers = [1, 2, 3]
# print(numbers) # [1, 2, 3]
# # To print individual numbers
# print(1, 2, 3) # 1 2 3

# ## To do this we use the Unpacking Operator
# print(*numbers) # 1 2 3

# # # create a list of #'s 1-5
# # values = list(range(5))
# # print(values) # [0, 1, 2, 3, 4]

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values) # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# #
# first = [1, 2]
# second = [3]
# values = [*first, "a", * second, *"Hello"]
# print(values) # [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']


# # UNPACKING DICTIONARIES 
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)

#######################################################
# EXERCISE:
#######################################################
# sentence = "This is a common interview question"

# WRITE A PROGRAM TO SHOW THE MOST REPEATED CHARACTER IN THE TEXT
# how many times is each character repeated, what data structure -> dictionary

# *** TO MAKE IT READABLE IMPORT: from pprint import pprint
# Set it to an Empty Dictionary
# char_frequency = {}
# for char in sentence:
#     #check if char in sentence
#     if char in char_frequency:
#         # increment value by 1
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1)

#Next need to convert Dict to Tuple and then to a List
# *** DICTIONARY'S CANNOT BE SORTED, ONLY LISTS CAN BE

# RETURNS KEY'VALUE PAIRS AS TUPLES
# print(sorted(char_frequency.items()))

# then pass 2nd argument
# print(sorted(char_frequency.items(), key=lambda kv: kv[1]))

# # THEN, reverse the sorting
# char_frequency_sorted = (sorted(
#     char_frequency.items(), 
#     key=lambda kv: kv[1], 
#     reverse=True))
# #[0] bc it's in Descending order 
# print(char_frequency_sorted[0])


#######################################################
# HANDLING EXCEPTIONS
#######################################################
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.") # You didn't enter a valid age.
#     # print(ex)
#     # print(type(ex))
# else:
#     print("No exceptions were thrown.")
# print("Execution continues")


# HANDLING ZERODIVISION ERRORS
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.") # You didn't enter a valid age.
# # except ZeroDivisionError:
# #     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# OPENING AND CLOSING FILES 
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.") # You didn't enter a valid age.
# # except ZeroDivisionError:
# #     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()


# the 'WITH STATEMENT' automatically release external resources, closes the file for the USER
# try:
#     with open("app.py") as file:
#         print("File opened.")
#         file.__
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.") # You didn't enter a valid age.
# # except ZeroDivisionError:
# #     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


# *** GOOGLE: PYTHON3 BUILT-IN EXCEPTIONS TO SEE LIST 
# *** NOT A GOOD PRACTICE, JUST SHOWING IN CASE YOU SEE IN OTHER PEOPLE'S CODE
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# above import 'from timeit import timeit'
# calculates execution time of code
# this speeds up code:
# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10 / age

# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """
# # Second param is the # of times you want to execute the code
# print("first code=", timeit(code1, number=10000))
# print("first code=", timeit(code2, number=10000))