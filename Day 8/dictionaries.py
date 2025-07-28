# 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = {}
print(type(dog))
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Benny'
dog['breed'] = 'Who knows'
dog['legs'] = 2
dog['age'] = 13
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Angelo',
    'last_name' : 'Coole',
    'gender' : 'M',
    'marital_status' : 'Single',
    'skills' : {
        'IT' : ['Python', 'Scala', 'R'],
        'sport' : 'Football'
    },
    'country' : 'NLD', 
    'city' : 'Amsterdam'
    }

print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of IT and check the data type, it should be a list
print(type(student['skills']))
print(student.get('skills'))

# Modify the skills values by adding one or two skills
student['skills']['IT'].append('Java')
print(student)

# Get the dictionary keys as a list
print(list(student.keys()))

# Get the dictionary values as a list
print(list(student.values()))

# Change the dictionary to a list of tuples using items() method
student.items()
print(student)

# Delete one of the items in the dictionary
student.pop('skills')
print(student)

# Delete one of the dictionaries
del student

# 🎉 CONGRATULATIONS ! 🎉

