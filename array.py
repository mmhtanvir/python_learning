fruits = ['apple', 'banana', 'mango']
fruits.append("jackfruit")
fruits.pop(1)

print(fruits)

#alphabet
fruits = ['apple', 'banana', 'mango']
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

combined_array = fruits + letters

for i in combined_array:
    print(i)

#number
fruits = ['apple', 'banana', 'mango']
numbers = list(range(1, 11))

combined_array = fruits + numbers

for i in combined_array:
    print(i)