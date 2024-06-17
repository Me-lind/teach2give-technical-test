# Design a function that takes a sentence as input and returns a new
#sentence with the words reversed in the same order that Master Yoda would use

#the function takes string as input
#using split() method to split the input to words identifing them by whitespace
#using python slicing [::-1]to rearrange them in reverse
#using join() to reconstruct the sentence separating the words using single spaces

def reverse_words(sentence):
    words=sentence.split()
    reversed_words=words[::-1]

    return ' '.join(reversed_words)


print(reverse_words("I loving coding so much"))