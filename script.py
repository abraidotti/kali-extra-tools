#!/bin/python3

# Variables and methods

quote = "All is fair in love and war."

print(quote.upper())
print(quote.lower())
print(quote.title())
print("There are " + str(len(quote)) + " characters in the quote.")

name = "Buddy" # string
age = 30 # int
gpa = 3.2 # float

print(int(age))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1

print(age)

birthday = 1
age += birthday

print(age)

print('\n')

# functions

def who_am_i(): # this is a function definition
	name = "Buddy"
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i() # this is a function invocation

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def n_l():
	print('\n')

n_l()

# boolean expressions 

print("Boolean expressions: ")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))

# Relational and Boolean operators

greater_than = 7 > 5 # True
less_than = 5 < 7 # True
greater_than_or_equal_to = 7 >= 7 # True
less_than_or_equal_to = 7 <= 7 # True

test_and = (7 > 5) and (5 < 7) # True and True == True
test_and2 = (7 > 5) and (5 > 7) # True and False == False
test_or = (7 > 5) or (5 < 7) # True or True == True
test_or2 = (7 > 5) or (5 > 7) # True or False == True

test_not = not True # False
test_not2 = not False # True

n_l()

# Conditional Statements

def drink(money):
	if money >= 2:
		return "You've got yourself a drink."
	else:
		return "No drink for you."

print(drink(3))
print(drink(1))

n_l()

def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return "We're getting a beer."
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, youngin'."
	else:
		return "You're too young and too poor."

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 4))

# Lists - they have brackets

movies = ["Aliens", "Aliens Jr.", "Micio Buns", "Meshes in the Afternoon"]
print(movies)
print(movies[0])
print(movies[1])
print(movies[3])
print(movies[1:3]) # exclusive
print(movies[1:4])
print(movies[1:]) # 1 and everything else
print(movies[:2]) # grab the first 2
print(movies[-1]) # grab the last

print(len(movies))
movies.append("Jank Jaw")
print(movies[-1])

movies.pop() # delete last item
print(movies)

movies.pop(0) # delete item in slot
print(movies)

n_l()

# Tuples - immutable, parentheses

grades = ("a", "b", "c", "d", "f")
print(grades)
print(grades[1])

n_l()

# Looping

# For loops - start to finish of an iterable
vegetables = ["cucumber", "spinach", "zanahoria"]

for vegetable in vegetables:
	print(vegetable)

# While loops - execute when True

i = 1

while i <= 10:
	print(i)
	i += 1

