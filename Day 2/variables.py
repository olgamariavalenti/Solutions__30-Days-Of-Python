## Exercise 1

# Declare multiple variable on one line

first_name, last_name, age = 'Carlo', 'Bloem', 30
print(age)

## Exercise 2

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(age))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print('The word', first_name, 'is longer than', last_name)
else:
    print('The word', first_name, 'is shorter than', last_name)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4 

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_two / num_one

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_one % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_divison = num_two // num_two

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
r = 30
area = math.pi*(r**2)
print(round(area))

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_circle = 2*math.pi*r
print(circum_circle)

# Take radius as user input and calculate the area.
print('Inpur radius:')
r = input()
print(area)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = input("Enter your name:")
last_name = input('Enter your last name: ')
print(f'Your name is {name} and your last name is {last_name}')   

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or 
help('keywords')