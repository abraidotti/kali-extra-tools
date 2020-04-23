#!/bin/python3

import sys # bring in system functions and parameters

from datetime import datetime as dt # bring in just one and give it an alias

print(sys.version)

print(dt.now())

my_name = "Buddy Boo"
print(my_name[0]) # print first char of str
print(my_name[-1]) # last

sentence = "This is a sentence."
print(sentence[:4]) # This
print(sentence[-9:-1]) # Sentence
print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money.'"
print(quote)

quote2 = "He said, \"give me all your money.\""
print(quote2)

too_much_space = "                       Hey, bud.    "
print(too_much_space.strip())

print("A" in "Apple") # True, A exists in Apple

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) # this can handle more use cases

movie = "Executioner Granny"
print("My favorite movie is {}.".format(movie))

# Dictionaries - key/value pairs using {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Beeeeer": 3}

print(drinks)

employees = {"Finance": ["Billy", "Jane", "Zhora"], "IT": ["Timmy", "Amber", "Johnny Bird"], "Business Intelligence": ["Brian", "Kyle", "Karen"]}
print(employees)

employees["Legal"] = ["Alan", "Dot", "Mazzy"]
print(employees)

employees.update({"Finance": ["Billy", "Cheezy", "Zhora"]})
print(employees)

drinks["White Russian"] = 8
print(drinks)

print(drinks.get("White Russian"))
