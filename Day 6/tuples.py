# 💻 Exercises: Day 6

# Exercises: Level 1
# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
empty = ()
print(type(empty))
sisters = ('Carla', 'Paola')
brother = ('Matteo', 'Fedez')
siblings = sisters + brother
numb_siblings = (len(siblings))
print(f'I have {numb_siblings} siblings')

# Exercises: Level 2
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Unpack siblings and parents from family_members
parents = ('Giuseppe', 'Carolina')
family_members = siblings + parents
only_parents = family_members[4:]
print(only_parents)

# Delete the family_members tuple completely
del family_members

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)