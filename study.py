# github.com/xServo
# flashcard

import random
import os

# get cards
front = []
back = []
fr = open("./cards.txt", "r")
line = fr.readline()
while line:
    front.append(line.strip())
    line = fr.readline()
    back.append(line.strip())
    line = fr.readline()
fr.close()

operation = input("1. Edit flashcards\n2. Study ")

# edit cards
while operation == "1":
    print("edit")

# study cards
while operation == "2":
    os.system("clear")
    index = random.randint(0, len(front) - 1)
    question = front[index]
    answer = back[index]
    print(question)
    input("\nPress enter to see answer. ")
    os.system("clear")
    print(f"{question}:")
    print(answer)
    input("\nPress enter to see new question. ")
