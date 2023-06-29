# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list

numbers = [1,3,4,6,2,7,9]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# use constructor

numbers2 = list((1,2,3,4,5,6))

print(numbers, numbers2)

# get a value
print(fruits[1])

# get length
print(len(fruits))

# append to end of list
fruits.append('mangos')

#remove from list
fruits.remove('grapes')

#insert to specific position
fruits.insert(2, 'bananas')

#change a value
fruits[0] = 'blueberries'

#remove  from specific position
fruits.pop(2)

#reverse list
fruits.reverse()

#Sort list or reverse sort
fruits.sort()
fruits.sort(reverse=True)

print(fruits)