# Exercises: Level 1

# Declare a first name variable and assign a value to it
name = "Gautam"

# Declare a last name variable and assign a value to it
sur_name = "Gupta"

# Declare a full name variable and assign a value to it
full_name = name + sur_name

# Declare a country variable and assign a value to it
country = "India"

# Declare a city variable and assign a value to it
city = "Mumbai"

# Declare an age variable and assign a value to it
age = 22

# Declare a year variable and assign a value to it
year = 2026

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variable on one line
j, k, = 4, "Hello"

#Exercises: Level 2

#Check the data type of all your variables using type() built-in function
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

# Using the len() built-in function, find the length of your first name
print(len(d))

# Compare the length of your first name and your last name
if len(name) > len(sur_name):
    print(f"Length of name is greater - {len(name)}")
else:
    print(f"Length of sur_name is greater - {len(sur_name)}")

# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_onṇe and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30
pi = 3.14

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * radius**2
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*pi*radius
print(circum_of_circle)

# Take radius as user input and calculate the area.
r = int(input("Enter the radius : "))
area = pi*r**2
print(area)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
f_name = input("Enter your first name : ")
s_name = input("Enter your last name : ")
c_name = input("Enter your country name : ")
Age = int(input("Enter your age : "))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# Skipping this questions as its basic.