#Write a recursive function to calculate the factorial of a number
#Using if else to carry out recursion to calculate the factorial of a number
#the base case is if number is 0 then it returns 1 since 0!=1.This is actually the terminating condition.

def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
    
print (factorial(9))    