# 💻 Exercises: Day 7
# # sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies_2 = {'Meta', 'SAP'}
print(it_companies.union(it_companies_2))
it_companies.pop()
print(it_companies)

# Exercises: Level 2
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely
print(f'A is {A}')
print(f'B is {B}')
print(f'A union B is: {A.union(B)}')
print(f'A intersection B is: {A.intersection(B)}')
print(f'A is a subset of B: {A.issubset(B)}')
print(f'Symmetics difference bw A and B is: {A.symmetric_difference(B)}')
del A
del B

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(f'The lenght of the list is: {len(age)}')
print(f'The lenght of the set is: {len(set(age))}')

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
phrase = 'I am a teacher and I love to inspire and teach people.'
phrase_a = phrase.split()
print(len(set(phrase_a)))
# 🎉 CONGRATULATIONS ! 🎉