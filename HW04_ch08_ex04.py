#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """This function returns True/False after evaluating the first letter, which will
        cause it to fail if a word has the first letter in uppercase followed by all lower letters, for example.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """This function evaluates if the lowercase letter c is a lowercase letter, instead of each character in s
        and will always return True irrespective of the string
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This function checks if every character in s is a lowercase character and sets flag to True if it is, but
        the flag is returned only after the for loop ends - which means that value in flag when it is being 
        returned is set is based on the last character in the string. This function fails when the the last character
        is an uppercase character, inspite of s having other lowercase characters
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This function sets flag to True even if one lowercase letter is present in the word because of the 'or' operator
        It will return False only for an all uppercase letter'd string
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """This function returns False when an uppercase letter is found, returns True only if all the letters in the string 
        are lowercase
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("Hello!"))

    print(any_lowercase2("HELLO"))

    print(any_lowercase3("hellO"))

    print(any_lowercase5('hEllO'))


if __name__ == '__main__':
    main()
