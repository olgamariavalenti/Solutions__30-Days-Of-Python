# Exercise: Level 1

## Check the python version you are using
import sys
print(sys.version)

### Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition(+)
print(3 + 4)

#subtraction(-)
print(3 - 4)

#multiplication(*)
print(3 * 4)

#modulus(%)
print(3 % 4)

#division(/)
print(3 / 4)

#exponential(**)
print(3 ** 4)

# floor division operator(//)
print(3 // 4)

# Write strings on the python interactive shell. The strings are the following:
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python
print("My name is Tigre, ", "I am Italina", "bla bla")

# Check the data types of the following data:
# 10
# 9.8
# 3.14
# 4 - 4j
# ['Asabeneh', 'Python', 'Finland']
# Your name
data_types = (10, 9.8, 4-4j, ['Asabeneh', 'Python', 'Finland'], "Tigre", (3 == 3))
for i in data_types:
    print(i, type(i))

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Find an Euclidian distance between (2, 3) and (10, 8)

from math import sqrt

a = (2, 3)
b = (10, 8)

diffx = (b[0] - a[0]) ** 2
diffy = (b[1] - a[1]) ** 2

euclidean = sqrt(diffx + diffy)
print(euclidean)

