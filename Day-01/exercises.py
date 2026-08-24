# Exercise - Level 1

# Q1. Check the python version you are using
# Ans. python --version

# Q2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
''' adddition(+) , subtraction(-) , multiplication(*) , modulus(%) , division(/) , exponential(**) , floor division operator(//) '''
a, b = 4, 3
print(f"Addition : {a+b}")
print(f"Subtraction : {a-b}")
print(f"Multiplication : {a*b}")
print(f"Division : {a/b}")   # this takes ans of quotient
print(f"Modulus : {a%b}")    # this takes ans of remainder
print(f"Exponential : {a**b}")
print(f"Floor Division : {a//b}")  # this takes ans of quotient in integer

# Q3. Write strings on the python interactive shell. The strings are the following:
''' Your name, Your family name, Your country, I am enjoying 30 days of python. '''
name = 'Gautam'
Family_name = 'Gupta' 
Country = 'India'
print(f"My Name is {name} & family name is {Family_name}. I live in {Country}. I am enjoying this course. ")

# Q4. Check the data types of the following data:
''' 10, 9.8, 3.14, 4 - 4j, ['Asabeneh', 'Python', 'Finland'], Your name, Your family name, Your country '''
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(Family_name))
print(type(Country))

# Exercise - Level 2

# Q1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
# Skipping the answer.

# Exercise - Level 3

# Q1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
a, b, c = 1, 2.0, 1-4j
d, e, f = "Gautam", a == 1, ["h", 1, 2.0, "y"]
g, h, i = (8, 5, "hello"), {8, 5, 3, "h"}, {"key" : "value"} 
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))

# Q2. Find an Euclidean distance between (2, 3) and (10, 8)
# Formula : euclidean distance = √((x1-x2)^2 + (y1-y2)^2)
import math

x1, y1 = 2, 3
x2, y2 = 10, 8
euclidean_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f"equilidean distance : {euclidean_distance} ")