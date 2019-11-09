import random
import sys
word_bank = ["apple", "kiwis", "water", "chips"]
x = random.choice(word_bank)
tries = 0


print("The secret word begins with a: " + " " + x[0])

while tries < 10:
    y = input("input a five letter word: ")
    if x == y:
        sys.exit("Good job! You are one with the source :)")
    if len(y) !=5 and len(y) != 0:
        print("0 1 2 3 4 that's how we count to five")
    if len(y) ==0:
        tries + 1
        print("You wasted a guess =P")
    if len(y) ==5:
        if x[0] != y[0]:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ, try again")
        if x[0] == y[0]:
            tries = tries +1
            print("you have " + str(10-tries) + " guesses left")
    if tries == 10:
        sys.exit("You lose :(")

