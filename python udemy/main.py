sentence = "%s is %d years old"

print(sentence % ("tanvir", 18))


#format strings

name = "tanvir"
print(f"hello,{name}")


x = 20
y = 20

print(f"the sum of X & y is {x+y}")



#task:

#1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.

x = 15
y = 30
z = x+y
print(z/2)
print(z/2)


#2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

#3. Create a variable called name and store your name in it as a string.

name = "tanvir"

print(f"hello, {name}")


#4. Create three variables in one line and assign each one a different food item.

x, y, z = "apple", "banana", "orange"
print() #x,y,z


#5. Print out "Hello" ten times using arithmetic operators.

print("helllo"*10)

#6. Set your name and age variables in one line with multiple assignment

name, age = "Tanvir", 18

print(f"my name is {name}, & I am {age} years old")

sentence = "my name is %s and Iam %d years old"
print(sentence % ("tanvir", 18))







#2.1. Create a list of names and print the second item.

list = ["apple", "banana", "orange"]

print(list[1])

#2.2. Create a list of sports and then replace the second item with another sport.

sports = ["cricket", "football", "tennis"]

sports[1] = "badminton"

print(sports)


#2.3. Create a list containing numbers and delete the fifth number from the array.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del numbers[4]

print(numbers)

#2.4. Create two lists of numbers and merge them.

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [12, 22, 32, 42, 52, 62, 72, 82, 92,]


numbers_1.extend(numbers_2)

print(numbers_1)

#2.5. Create a list of numbers and find the length, minimum, and maximum.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22, 32, 42, 52, 62, 72, 82, 92]


print(len(nums))
print(max(nums))
print(min(nums))

#2.6. Create a dictionary of students and scores and print out a student’s score.


student_scores = {
    "abdullah": 95,
    "abdur-rahman": 89,
    "muhammad": 78
}

print(student_scores["abdur-rahman"])

#2.7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.

name_age =  {
    "Munna" : 34,
    "Tanjir" : 27,
    "Tanvir" : 18
}

del name_age["Tanjir"]

print(name_age)

#2.9. Create a tuple of your favorite movies

movie = ("Breaking Bad", "Messiah", "Annabelle")

print(movie)

#2.10. Create a tuple and print all the items from the first to third index.

movie = ("Breaking Bad", "Messiah", "Annabelle", "Conjuring", "IT", "Willy wonka and the chocolate factory")

print(movie[0:3])