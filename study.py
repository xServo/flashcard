# github.com/xServo
# flashcard

import random
import os

# get cards
cards = {
    "The capitol of FL": "tallahasse",
    "Color of  an apple": "red",
    "Does this work": "yes",
}

# sort cards
keys = []
for key in cards:
    keys.append(key)

# Study loop
operation = input("1. Edit flashcards\n2. Study")
while operation == "1":
    print("edit")
while operation == "2":
    os.system("clear")
    question = keys[random.randint(0, len(keys) - 1)]
    answer = cards[question]
    print(question)
    input("\nPress enter to see answer. ")
    print(answer)
    input("\nPress enter to see new question. ")
