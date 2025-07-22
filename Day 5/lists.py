# 💻 Exercises: Day 5
# Exercises: Level 1
# Declare an empty list
# Declare a list with more than 5 items
# Find the length of your list
# Get the first item, the middle item and the last item of the list
list = []
list_5 = [1,2,3,4,5,6,7]
print(len(list_5))
print(list_5[0])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_daya_types = ('Olga', 30, 173, True, 'Utrecht')
print(mixed_daya_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# Print the list using print()
# Print the number of companies in the list
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)
print(len(companies))

# Print the first and last company
# Print the list after modifying one of the companies
print(f'The first company is {companies[0]} the last company is {companies[-1]}')
companies[0] = 'Snowflake'
print(f'The first company is now {companies[0]}')

# Add an IT company to it_companies
# Insert an IT company in the middle of the companies list
# Change one of the it_companies names to uppercase (IBM excluded!)
print(companies[0].upper())

# Join the it_companies with a string '#;
lista_str = []
for  i in companies:
    lista_str.append(i + '#')
print(lista_str)
   
# Check if a certain company exists in the it_companies list.
# Sort the list using sort() method
# Reverse the list in descending order using reverse() method
companies.append('Databricks')
print(companies)
middle_index = len(companies) // 2
companies.insert(middle_index, 'TEST')
print(companies)

# Slice out the first 3 companies from the list
# Slice out the last 3 companies from the list
# Slice out the middle IT company or companies from the list
print(companies[:3])
print(companies[-3:])
print(companies[middle_index])

# Remove the first IT company from the list
companies.pop(0)
print(companies)

# Destroy the IT companies list
del companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort(reverse=False)
print(f'The min age is {ages[0]} and the max age is {ages[-1]}')

# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
i = len(ages)
if i % 2 == 0 :
    median = ((ages[i//2 - 1] + ages[i//2]) / 2)
else: 
    median = ages[i//2]
print(median)

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
n = len(countries)
if n%2 == 0:
    value = int(len(countries)/2)
else:
    value = int(((len(countries))+1)/2)

print(value)

first_half = countries[:value]
print(first_half)
second_half = countries[value:]
print(second_half)

# Unpack the first three countries and the rest as scandic countries.
other_countries = countries[:3]
scandic_countries = countries[3:]
print(other_countries)
print(scandic_countries)
# 🎉 CONGRATULATIONS ! 🎉