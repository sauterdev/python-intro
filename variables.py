# A variable is a container for a value, which can be of various types

'''
This is a multiline comment or 'docstring'. can be single or double quotes
'''

"""
Variable Rules:
-Variable names are case sensitive
-must start with a letter or underscore
-can have numbers but cant start with one
"""

x = 1  #int integer
y = 2.4 #float floating point number
name = 'Chris' # str string
is_cool = True # bool boolean. True needs to be capitalized

#Multiple assignment
x, y, name, is_cool =(1, 2.5, 'Chris', True)

print("Hello")
print(x, y, is_cool)

#Basic Math
a = x + y
print(a)

#check type
print(type(x))

#Casting - change variable type

x = str(x)
y = int(y)

print(type(x))
print(type(y), y)
print(y)

z = float(y)
print(type(z), z)
