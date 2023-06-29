# If/ Else conditions are used to decide to do something based on something being true or false

x = 50
y = 50



# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#simple if
if x > y :
    print(f'{x} is greater than {y}')

 #if/else
if x > y :
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#elif (else if)
if x > y :
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#nested If
if x > 2:
    if x <= 10:
        print(f'{x} is greated than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

#and
if x > 2 and x <=10: 
    print(f'{x} is greated than 2 and less than or equal to 10')

#or
if x > 2 or x <=10: 
    print(f'{x} is greated than 2 or less than or equal to 10')

#not
if not(x == y):
    print(f'{x} isnot equal to {y}')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object




# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location: