#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports


# Body


def eval_loop():
    input_string = " "
    while input_string.lower() != 'done':
        try:
            input_string = input("Enter the expression you want to evaluate on the Python interpreter. Enter Done if you want to exit.\n")
            if input_string.lower() != 'done':
                result = eval(input_string)
                print("Result :", result)

        except:
            print("Not a valid expression!")

###############################################################################


def main():
    eval_loop()

if __name__ == '__main__':
    main()
