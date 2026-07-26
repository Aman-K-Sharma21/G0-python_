# . Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a > b and a>c :
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > b :
        return c


a = int(input("enter the number :"))
b = int(input("enter the number :"))
c = int(input("enter the number :"))

print(greatest(a,b,c))

