# 💻 Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty'
b= 'Days'
c ='Of'
d = 'Python'
sentence = '{} {} {} {}'.format(a,b,c,d)
print(sentence)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize)
print(company.swapcase)

# Cut(slice) out the first word of Coding For All string.
print(company.split()[1:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.rfind('Coding')) ## Returns the index of the first occurrence of a substring, if not found returns -1

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Eating'))

# Change Python for Everyone to Python for All using the replace method or other methods.
python = 'Python for all'

print(python.replace('Python', 'SQL'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# Split at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
print(f'{company[0]} and {company[-1]}')

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
letter = 'C'
print(company.index(letter))
print(company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
coding = 'Coding For All People'
print(coding.rfind('l'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
spaces = '   Coding For All      '
print(spaces)
spaces_1 = company.strip()
print(spaces_1)

# Which one of the following variables return True when we use the method isidentifier():
a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(f'a = {a.isidentifier()}')
print(f'b = {b.isidentifier()}')

# The following list contains the names of some of python libraries: Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
joined = '# '.join(libraries)
print(joined)

# Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\n\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('{:<10}{:<10}{:<10}{:<10}'.format('Name', 'Age', 'Country', 'City'))
print('{:<10}{:<10}{:<10}{:<10}'.format('Asabeneh', '250', 'Finland', 'Helsinki'))

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print('{} + {} = {}'.format(a,b, a + b))
print('{} % {} = {}'.format(a,b, a % b))
print('{} // {} = {}'.format(a,b, a // b))
print('{} ** {} = {}'.format(a,b, a ** b))