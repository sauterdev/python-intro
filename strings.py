# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Chris'
age = 37

#Concatenate
# print('Hello, my name is ' + name + ' and I am ' + age)
print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings
print(f'Hello again, my name is still {name} and I am still {age}')


# String Methods

s = 'hello world'

#capitalize string
print(s.capitalize())

#make all upper case
s.upper()
# make all lower case
s.lower()
# swap case
s.swapcase()
#get length
len(s)
#replace
print(s.replace('world', 'everyone'))
# count substrings in string
sub = 'h'
print(s.count(sub))
#Starts with or ends with, returns boolean
s.startswith('hello')
s.endswith('d')

#split into a list (array)
print(s.split())

# find position of character
print(s.find('r'))

#is alphanumeric returns boolean
s.isalnum()

#is alphabetic returns boolean
s.isalpha()

#is all numeric returns boolean
s.isnumeric()

