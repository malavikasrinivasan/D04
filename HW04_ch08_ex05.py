# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.


def limits(c):
    """ Returns the ord of a and z based on whether the character is an upper or lower case character
    """
    if c.islower():
        return(ord('a'), ord('z'))
    else:
        return(ord('A'), ord('Z'))


def rotate_word(word, rotate_by_this_much):
    rotated_word = ''
    for letter in word:
        a_ord = limits(letter)[0]
        z_ord = limits(letter)[1]
        moved_ord = ord(letter) + rotate_by_this_much

        if moved_ord > z_ord:
            new_ord = a_ord + (moved_ord - z_ord) - 1
            rotated_word += chr(new_ord)
        elif moved_ord < a_ord:
            new_ord = z_ord - (a_ord - moved_ord) + 1
            rotated_word += chr(new_ord)
        else:
            rotated_word += chr(moved_ord)
    return rotated_word

def main():

    print(rotate_word("zzz",4))
    print(rotate_word("HeLlo",2))
    print(rotate_word("az",-5))

if __name__ == '__main__':
    main()