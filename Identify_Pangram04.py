#Design a function that determines whether a given string is a pangram.

#import string which contains constants that will be useful to deal with strings
#such as string.ascii_lowercase that contains all alphabet in lowercase

import string
def is_pangram(input):
    alphabet_set = set(string.ascii_lowercase)

    #set the input string to lowercase
    input_set = set(input.lower())

#check if alphabet_set is a subset or equal to input_set
    return alphabet_set<=input_set

print(is_pangram("abacadabra"))
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))