# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#use constructor
person2 = dict(first_name="Sara", last_name="Williams", age=25)

print(person2, type(person2))

#get value
person['first_name']
person.get('last_name')

#add key/value

person['phone'] = '867-5309'

# get dict keys
person.keys()

#get dict items gives the key/value pairs
person.items()

#copy dict
person3 = person.copy()

print(person, type(person))

# remove item
del(person['age'])
person.pop('phone')

#clear 
person.clear()

#get length
len(person)

#list of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

#access list items
print(people[1]['name'])

print(type(people), people)