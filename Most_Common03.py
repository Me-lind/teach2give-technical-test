#Design a function that takes a string or sequence of characters as input 
#and returns the character that appears most frequently.

#Using the module collections in python import couter which is a subclass designed to count objects
# the function takes input as a string

from collections import Counter

def most_common_str(input):
    num_appear=Counter(input)
#since most_common() function returns all the counts in descendion order 
#the count 1 shows that we want the single most common
#the first index[0] would return both the interger and its count hence the second returns only the iterger from the tuple
    return num_appear.most_common(1)[0][0]

print(most_common_str("11134"))
print(most_common_str("abracadabra"))
