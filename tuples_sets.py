# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create a tuple. leave trailing comma if only one value

fruits = ('apples', 'oranges', 'grapes')
fruits2 = tuple(('bananas',))

print(fruits, fruits2)

# get value
fruits[1]

# cant change tuple values

#fruits[0] = 'steven'

# delete tuple
del fruits2

#get length

len(fruits)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set with {}

fruits_set = {'Apples', 'Oranges', 'Mango'}

#check if something is in set

print('Apples' in fruits_set)

#add to set
fruits_set.add('Grape')

#remove from set
fruits_set.remove('Grape')

#clear set **different from delete
fruits_set.clear()

#delete
del fruits2