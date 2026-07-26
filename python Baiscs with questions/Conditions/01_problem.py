#  Write a program to find the greatest of four numbers entered by the user. 

num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
num3 = int(input("enter the third number :"))
num4 = int(input("enter the fourth number :"))

if (num1 > num2) and (num1 > num3) and (num1 > num4) :
    print(num1, "is the greatest number")
elif (num2 > num1) and (num2 > num3) and (num2 > num4) :
    print(num2, "is the greatest number")
elif (num3 > num1) and (num3 > num2) and (num3 > num4 ):
    print(num3, "is the greatest number ")
else:
    print(num4, "is the greatest number")