# #function

# a = 9
# b = 8

# c = sum((a,b)) #built-in function
# print(c)

# def function1():
#     print("Hello, you are in function 1")

# print(function1()) none because it doesn't contain return statement.

# def avg(a,b):
#     """this is a function which will calculate the average of two number"""
#     average = (a + b)/2
#     print(average)
#     return average

# v = avg(4,6)
# print(v)

# print(avg.__doc__)

#-----------------------------------------------------------------

# n! = n * n-1 * n-2 * n-3............1
# n! = n * (n-1)!

def factorial_iterative(n):
    """
    parameter n: integer
    return : n * n-1 * n-2 * n-3................1
    """
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

def factorial_recursive(n):
    """ 
    param n : integer
    return : n * n-1 * n-2 * n-3 ......1
    """

    if n == 1:
        return 1
    else:
        return n* factorial_recursive(n-1)

number = int(input("Enter the number :"))
print("Factorial Using Iterative method",factorial_iterative(number))
print("Factorial Using Recursive Method",factorial_recursive(number))