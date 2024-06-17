#Design a function that reverses the digits of an integer. For example, 50 should become 5 and -12 should become -21.
#convert the digits to string and to its absolute value if negative
#using python slicing reverse the string
#convert string back to int

def reverse_digit(x):
    if x==0:
        return 0
    #if digit is positive
    elif x>0:
        return int(str(x)[::-1])
    #if digit is negative
    elif x<0:
        return int('-' + str(abs(x))[::-1])
    
print (reverse_digit(56))