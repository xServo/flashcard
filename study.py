# github.com/xServo
# flashcard

import random
import os
import sys

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

os.system("clear")
operation = input("1. Edit flashcards\n2. Study \n")

# edit cards
i = 0
os.system("clear")
while operation == "1":
    # print items
    print("ITEMS")
    while i < len(front):
        print(str(i) + ":", front[i])
        print("  ", back[i])
        i += 1
    operation = input("\n\nOPTIONS\n1. Clear all\n2. Add items\n")

    # clear items
    if operation == "1":
        open("./cards.txt", "w").close()
        front = []
        back = []
        os.system("clear")

    # add items
    while operation == "2":
        os.system("clear")
        # print items
        print("ITEMS")
        i = 0
        while i < len(front):
            print(str(i) + ":", front[i])
            print("  ", back[i])
            i += 1
        fa = open("./cards.txt", "a")
        write = input("\nEnter question text.\nType 'done' to exit. \n")
        if write == "done":
            fa.close()
            sys.exit()
        elif write != "done":
            fa.write(write)
            os.system("clear")
        write = input("\nEnter the answer text of that question.\n")
        fa.write("\n" + write + "\n") 

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
