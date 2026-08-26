# 💻 Exercises - Day 3

# Declare your age as integer variable
age = 23

# Declare your height as a float variable
height = 174.65

# Declare a variable that store a complex number
complex_num = 5 + 5j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Enter base: 20, Enter height: 10, The area of the triangle is 100
length = int(input("Enter the base : "))
breadth = int(input("Enter the height : "))
area = 0.5 * length * breadth
print(area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5, Enter side b: 4, Enter side c: 3, The perimeter of the triangle is 12
a = int(input("Enter a: "))
perimeter = length + breadth + a
print(perimeter)

# Get length and width of a rectangle using pbreadthompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
area = length * breadth
perimeter = + 2 * (length + breadth)
print(area, "&", perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = int(input("Enter the radius : "))
area = pi * r ** 2
circumference = 2 * pi * r
print(area)
print(circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y = mx + c - formula
m = 2
c = -2
y_intercept = c
x_intercept = -c / m
slope = m
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = y2 - y1 / x2 - x1 
euclid_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"Slope is {slope}. ")
print(f"Euclid distance is {euclid_distance}. ")

# Compare the slopes in tasks 8 and 9.
if m == slope:
    print("Both slope are equal.")
else:
    print("Both slope are equal.")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-20, 21):
    y = x**2 + 6*x + 9

    if y == 0:
        print("y becomes 0 when x =", x)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
py, hy = "python", "dragon"
print(len(py))
print(len(hy))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in py and "on" in hy:
    print("its present")
else:
    print("its not present")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if "jargon" in "I hope this course is not full of jargon":
    print("its present")
else:
    print("its not present")

# Find the length of the text python and convert the value to float and convert it to string
con = len(py)
con1 = float(con)
con2 = str(con1)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# we can use this method to check its even or not : num % 2 == 0 .
 
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
num = 7//3
p = int(2.7)
if num == p :
    print("its equal")
else:
    print("its not equal")

# Check if type of '10' is equal to type of 10
if type('10') == type(10) :
    print("its equal")
else:
    print("its not equal")

# Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print("its equal")
else:
    print("its not equal")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40, Enter rate per hour: 28, Your weekly earning is 1120
hour = int(input("enter your hours: "))
rate = int(input("enter your rate per hour: "))
weekly = hour * rate
print(weekly)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100, You have lived for 3153600000 seconds.
year = int(input("enter the year: "))
live = 60 * 60 * 24 * year
print(f"You have lived {live} this much of seconds of your life.")
      
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)