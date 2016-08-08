#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint

# Body


def generate_random():
    return randint(1, 25)


def get_user_input():
    try:
        guess = int(input("Enter guess "))
        return guess
    except:
        print("Sorry, you lost a guess because that was not a valid integer!")
        return False


def evaluate_user_guess(magic_number, guess):
    if magic_number > guess:
        print("Nope, that's low!")
        return False
    elif magic_number < guess:
        print("Nope, that's high!")
        return False
    else:
        print("Bingo! You got it!")
        return True


###############################################################################


def main():
    tries = 0
    magic_number = generate_random()
    print("Welcome to the magic-number game! Try and guess the magic number in my head within five guesses.")
    print("To keep it simple, I've chosen a number between 1 and 25. Good luck!")
    while tries < 5:
        tries += 1
        print("Try "+str(tries), end=" ")
        guess = get_user_input()
        if guess:
            if evaluate_user_guess(magic_number, guess):
                break
            else:
                continue
    else:
        print("The magic number was "+str(magic_number))

if __name__ == '__main__':
    main()