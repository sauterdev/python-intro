# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Paul", "Ringo", "George"]

# simple for loop
for person in people:
    print(f"Current person: {person}")

# Break
for person in people:
    if person == "Ringo":
        break
    print(f"Current person: {person}")

# Continue skips condition and then completes the loop
for person in people:
    if person == "Ringo":
        continue
    print(f"Current person: {person}")

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f"Number: {i}")

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f"Count: {count}")
    count += 1
